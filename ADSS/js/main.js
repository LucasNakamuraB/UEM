import { compareCards } from './cards.js';
import { TrucoEngine, viewStateFor } from './engine.js';
import { RoomDirectory, RoomChannel, genId, genRoomCode } from './network.js';
import {
  botChooseCard, botTrucoDecision, botTrucoResponse,
  botEnvidoDecision, botEnvidoResponse, botShouldDeclareFlor,
} from './bot.js';
import * as ui from './ui.js';

const self = { id: genId(), nickname: null };

let roomCode = null;
let isHost = false;
let channel = null;
let engine = null;
let roomName = '';
let roomInfoLocal = null; // client-side mirror {code, config, players, private, hostId}
let joinRetryTimer = null;
let heartbeatTimer = null;
let handAdvanceScheduled = false;
let botActionScheduled = false;
let matchEndShown = false;

const BOT_NAMES = ['Bot Ana', 'Bot Beto', 'Bot Caco', 'Bot Duda'];

function botName(seat) {
  return BOT_NAMES[seat] || `Bot ${seat}`;
}

// ---------------- LOBBY ----------------

function refreshLobby() {
  const rooms = RoomDirectory.listPublic().map((r) => ({
    code: r.code, name: r.name, playerCount: r.playerCount, maxPlayers: r.maxPlayers,
  }));
  ui.renderRoomList(rooms, (code) => joinRoom(code));
}

RoomDirectory.subscribe(refreshLobby);

function enterLobby() {
  ui.showScreen('lobby');
  refreshLobby();
}

// ---------------- ROOM / HOST ----------------

function dirFields(players, config) {
  return { name: roomName, maxPlayers: config.numPlayers, playerCount: players.length, private: !!config.isPrivate };
}

function createRoom(config, name) {
  roomCode = genRoomCode();
  roomName = name || `Sala de ${self.nickname}`;
  isHost = true;
  matchEndShown = false;

  const hostPlayer = { id: self.id, nickname: self.nickname, isBot: false, seat: 0, team: 0 };
  roomInfoLocal = { code: roomCode, config, hostId: self.id, private: !!config.isPrivate, players: [hostPlayer] };

  channel = new RoomChannel(roomCode, self.id);
  channel.on(handleHostIncoming);

  if (!config.isPrivate) {
    RoomDirectory.upsert(roomCode, dirFields(roomInfoLocal.players, config));
    heartbeatTimer = setInterval(() => {
      if (roomInfoLocal) RoomDirectory.upsert(roomCode, dirFields(roomInfoLocal.players, config));
    }, 5000);
  }

  renderRoom();
  ui.showScreen('room');
}

function broadcastRoomUpdate() {
  channel.send('room-update', roomInfoLocal);
  if (!roomInfoLocal.config.isPrivate) {
    RoomDirectory.upsert(roomCode, dirFields(roomInfoLocal.players, roomInfoLocal.config));
  }
  renderRoom();
}

function renderRoom() {
  const canStart = isHost && !engine
    && roomInfoLocal.players.length === roomInfoLocal.config.numPlayers;
  ui.renderRoomScreen(roomInfoLocal, self.id, isHost, canStart);
}

function addBot() {
  if (!isHost || !roomInfoLocal) return;
  if (roomInfoLocal.players.length >= roomInfoLocal.config.numPlayers) return;
  const seat = roomInfoLocal.players.length;
  const team = seat % 2;
  roomInfoLocal.players.push({ id: genId(), nickname: botName(seat), isBot: true, seat, team });
  broadcastRoomUpdate();
}

function startMatch() {
  if (!isHost || !roomInfoLocal) return;
  if (roomInfoLocal.players.length !== roomInfoLocal.config.numPlayers) {
    ui.toast('Aguarde todos os jogadores ou complete com bots.', 'error');
    return;
  }
  if (!roomInfoLocal.config.isPrivate) RoomDirectory.remove(roomCode);
  if (heartbeatTimer) clearInterval(heartbeatTimer);
  engine = new TrucoEngine(roomInfoLocal.config, roomInfoLocal.players, hostOnStateChange);
  channel.send('match-started', {});
  engine.start();
}

function handleHostIncoming(msg) {
  if (msg.type === 'join-request') {
    const { id, nickname } = msg.payload;
    if (engine) {
      channel.send('join-denied', { targetPlayerId: id, reason: 'A partida já começou.' });
      return;
    }
    if (roomInfoLocal.players.length >= roomInfoLocal.config.numPlayers) {
      channel.send('join-denied', { targetPlayerId: id, reason: 'Sala cheia.' });
      return;
    }
    if (roomInfoLocal.players.some((p) => p.nickname.toLowerCase() === nickname.toLowerCase())) {
      channel.send('join-denied', { targetPlayerId: id, reason: 'Apelido já em uso nesta sala.' });
      return;
    }
    const seat = roomInfoLocal.players.length;
    const team = seat % 2;
    roomInfoLocal.players.push({ id, nickname, isBot: false, seat, team });
    broadcastRoomUpdate();
  } else if (msg.type === 'action') {
    const { method, playerId, payload } = msg.payload;
    const result = applyEngineAction(method, playerId, payload);
    if (!result.ok) channel.send('error', { targetPlayerId: playerId, message: result.error });
  } else if (msg.type === 'leave') {
    if (!roomInfoLocal) return;
    if (!engine) {
      roomInfoLocal.players = roomInfoLocal.players.filter((p) => p.id !== msg.payload.id);
      roomInfoLocal.players.forEach((p, i) => { p.seat = i; p.team = i % 2; });
      broadcastRoomUpdate();
    }
  }
}

function applyEngineAction(method, playerId, payload) {
  switch (method) {
    case 'playCard': return engine.playCard(playerId, payload.cardId);
    case 'callTruco': return engine.callTruco(playerId);
    case 'respondTruco': return engine.respondTruco(playerId, payload.action);
    case 'callEnvido': return engine.callEnvido(playerId, payload.levelKey);
    case 'respondEnvido': return engine.respondEnvido(playerId, payload.action);
    case 'declareFlor': return engine.declareFlor(playerId);
    case 'runFromHand': return engine.runFromHand(playerId);
    default: return { ok: false, error: 'Ação desconhecida.' };
  }
}

function getBestOnTable(hand) {
  if (hand.currentRoundCards.length === 0) return null;
  let best = hand.currentRoundCards[0].card;
  for (const e of hand.currentRoundCards.slice(1)) {
    if (compareCards(e.card, best, hand.manilhaRank) > 0) best = e.card;
  }
  return best;
}

function scheduleBotAction(fn) {
  botActionScheduled = true;
  setTimeout(() => {
    botActionScheduled = false;
    fn();
  }, 700 + Math.random() * 700);
}

function runBotsIfNeeded(state) {
  if (state.status !== 'playing' || botActionScheduled) return;
  const hand = state.hand;
  if (!hand || hand.finished) return;

  if (hand.pendingTruco) {
    const targets = state.players.filter((p) => p.team === hand.pendingTruco.targetTeam);
    if (targets.every((p) => p.isBot)) {
      const bot = targets[0];
      scheduleBotAction(() => {
        const cards = engine.hand.handsBySeat[bot.seat];
        const action = botTrucoResponse(cards, engine.hand.manilhaRank, hand.pendingTruco.level.value);
        engine.respondTruco(bot.id, action);
      });
    }
    return;
  }

  if (hand.envido.pendingCall) {
    const targets = state.players.filter((p) => p.team === hand.envido.pendingCall.targetTeam);
    if (targets.every((p) => p.isBot)) {
      const bot = targets[0];
      scheduleBotAction(() => {
        const cards = engine.hand.handsBySeat[bot.seat];
        const action = botEnvidoResponse(cards, hand.envido.pendingCall.level.key);
        engine.respondEnvido(bot.id, action);
      });
    }
    return;
  }

  const current = state.players.find((p) => p.seat === hand.turnSeat);
  if (current && current.isBot) {
    scheduleBotAction(() => {
      const cards = engine.hand.handsBySeat[current.seat];
      if (!cards || cards.length === 0) return;
      const isOpeningMoment = hand.currentRound === 0 && hand.currentRoundCards.length === 0 && hand.value === 1;
      if (isOpeningMoment) {
        if (engine.canCallFlorNow() && botShouldDeclareFlor(cards) && !hand.flor.declarations[current.id]) {
          engine.declareFlor(current.id);
          return;
        }
        if (hand.canCallEnvido && botEnvidoDecision(cards)) {
          engine.callEnvido(current.id, 'envido');
          return;
        }
        if (botTrucoDecision(cards, engine.hand.manilhaRank, hand.value) === 'call') {
          engine.callTruco(current.id);
          return;
        }
      }
      const bestOnTable = getBestOnTable(hand);
      const cardId = botChooseCard(cards, engine.hand.manilhaRank, { bestOnTable });
      engine.playCard(current.id, cardId);
    });
  }
}

function hostOnStateChange(state) {
  roomInfoLocal.players = state.players;

  state.players.forEach((p) => {
    if (p.id !== self.id && !p.isBot) {
      channel.send('state', { targetPlayerId: p.id, state: viewStateFor(state, p.id) });
    }
  });

  ui.showScreen('game');
  ui.renderGame(viewStateFor(state, self.id), self.id, hostHandlers);

  if (state.status === 'finished') {
    showEndModal(state);
  } else if (state.hand && state.hand.finished) {
    if (!handAdvanceScheduled) {
      handAdvanceScheduled = true;
      setTimeout(() => {
        handAdvanceScheduled = false;
        if (engine && engine.status === 'playing') engine.advanceHand();
      }, 2500);
    }
  } else {
    handAdvanceScheduled = false;
  }

  runBotsIfNeeded(state);
}

function showEndModal(state) {
  if (matchEndShown) return;
  matchEndShown = true;
  const winnerLabel = state.winnerTeam === 0 ? 'Dupla A' : 'Dupla B';
  ui.openModal(`
    <h3>Fim de partida!</h3>
    <p>${winnerLabel} venceu com ${state.scores[state.winnerTeam]} x ${state.scores[1 - state.winnerTeam]} pontos.</p>
    <div class="modal-actions"><button class="btn btn-primary" id="btn-end-ok">Voltar ao lobby</button></div>
  `);
  document.getElementById('btn-end-ok').onclick = () => {
    ui.closeModal();
    leaveRoom();
  };
}

const hostHandlers = {
  onPlayCard: (cardId) => toastIfError(applyEngineAction('playCard', self.id, { cardId })),
  onCallTruco: () => toastIfError(applyEngineAction('callTruco', self.id, {})),
  onRespondTruco: (action) => toastIfError(applyEngineAction('respondTruco', self.id, { action })),
  onCallEnvido: (levelKey) => toastIfError(applyEngineAction('callEnvido', self.id, { levelKey })),
  onRespondEnvido: (action) => toastIfError(applyEngineAction('respondEnvido', self.id, { action })),
  onDeclareFlor: () => toastIfError(applyEngineAction('declareFlor', self.id, {})),
  onRun: () => toastIfError(applyEngineAction('runFromHand', self.id, {})),
};

function toastIfError(result) {
  if (!result.ok) ui.toast(result.error, 'error');
}

// ---------------- CLIENT (non-host) ----------------

function sendAction(method, payload) {
  channel.send('action', { method, playerId: self.id, payload });
}

const clientHandlers = {
  onPlayCard: (cardId) => sendAction('playCard', { cardId }),
  onCallTruco: () => sendAction('callTruco', {}),
  onRespondTruco: (action) => sendAction('respondTruco', { action }),
  onCallEnvido: (levelKey) => sendAction('callEnvido', { levelKey }),
  onRespondEnvido: (action) => sendAction('respondEnvido', { action }),
  onDeclareFlor: () => sendAction('declareFlor', {}),
  onRun: () => sendAction('runFromHand', {}),
};

function joinRoom(code) {
  code = code.trim().toUpperCase();
  if (!code) return;
  roomCode = code;
  isHost = false;
  matchEndShown = false;
  channel = new RoomChannel(code, self.id);
  channel.on(handleClientIncoming);

  ui.showScreen('room');
  document.getElementById('room-code-display').textContent = code;
  document.getElementById('room-config-summary').innerHTML = '<span>Conectando...</span>';
  document.getElementById('room-players-list').innerHTML = '';
  document.getElementById('room-host-controls').classList.add('hidden');
  document.getElementById('room-wait-msg').classList.remove('hidden');
  document.getElementById('room-wait-msg').textContent = 'Conectando à sala...';

  let attempts = 0;
  let joined = false;
  clearInterval(joinRetryTimer);
  const tryJoin = () => {
    attempts += 1;
    channel.send('join-request', { id: self.id, nickname: self.nickname });
    if (attempts >= 6) {
      clearInterval(joinRetryTimer);
      if (!joined) {
        ui.toast('Sala não encontrada ou código inválido.', 'error');
        cleanupNetwork();
        enterLobby();
      }
    }
  };
  tryJoin();
  joinRetryTimer = setInterval(tryJoin, 700);

  function handleClientIncoming(msg) {
    if (msg.type === 'room-update') {
      joined = msg.payload.players.some((p) => p.id === self.id);
      if (joined) clearInterval(joinRetryTimer);
      roomInfoLocal = msg.payload;
      document.getElementById('room-wait-msg').textContent = 'Aguardando o anfitrião iniciar a partida...';
      ui.renderRoomScreen(roomInfoLocal, self.id, false, false);
    } else if (msg.type === 'join-denied' && msg.payload.targetPlayerId === self.id) {
      clearInterval(joinRetryTimer);
      ui.toast(msg.payload.reason, 'error');
      cleanupNetwork();
      enterLobby();
    } else if (msg.type === 'state' && msg.payload.targetPlayerId === self.id) {
      ui.showScreen('game');
      ui.renderGame(msg.payload.state, self.id, clientHandlers);
      if (msg.payload.state.status === 'finished') showEndModal(msg.payload.state);
    } else if (msg.type === 'error' && msg.payload.targetPlayerId === self.id) {
      ui.toast(msg.payload.message, 'error');
    } else if (msg.type === 'room-closed') {
      ui.toast('O anfitrião encerrou a sala.', 'error');
      cleanupNetwork();
      enterLobby();
    }
  }
}

function cleanupNetwork() {
  clearInterval(joinRetryTimer);
  clearInterval(heartbeatTimer);
  if (channel) channel.close();
  channel = null;
  engine = null;
  roomInfoLocal = null;
  roomCode = null;
  isHost = false;
}

function leaveRoom() {
  if (channel) {
    if (isHost) {
      channel.send('room-closed', {});
      if (roomInfoLocal && !roomInfoLocal.config.isPrivate && roomCode) RoomDirectory.remove(roomCode);
    } else {
      channel.send('leave', { id: self.id });
    }
  }
  cleanupNetwork();
  enterLobby();
}

window.addEventListener('beforeunload', () => {
  if (isHost && roomCode) {
    if (roomInfoLocal && !roomInfoLocal.config.isPrivate) RoomDirectory.remove(roomCode);
    if (channel) channel.send('room-closed', {});
  } else if (channel) {
    channel.send('leave', { id: self.id });
  }
});

// ---------------- UI WIRING ----------------

document.getElementById('login-form').addEventListener('submit', (e) => {
  e.preventDefault();
  const input = document.getElementById('nickname-input');
  const nickname = input.value.trim();
  const errorEl = document.getElementById('login-error');
  if (!nickname) {
    errorEl.textContent = 'Informe um apelido.';
    errorEl.classList.remove('hidden');
    return;
  }
  errorEl.classList.add('hidden');
  self.nickname = nickname;
  ui.setUserBadge(nickname);
  enterLobby();
});

document.getElementById('join-form').addEventListener('submit', (e) => {
  e.preventDefault();
  const input = document.getElementById('join-code-input');
  joinRoom(input.value);
  input.value = '';
});

document.getElementById('btn-refresh-rooms').addEventListener('click', refreshLobby);

document.getElementById('btn-rules').addEventListener('click', () => {
  ui.openModal(ui.rulesModalHtml());
  document.getElementById('btn-close-rules').onclick = ui.closeModal;
});

document.getElementById('btn-open-create').addEventListener('click', () => {
  ui.openModal(`
    <h3>Criar Sala</h3>
    <div class="field-row">
      <label>Nome da sala</label>
      <input type="text" id="cfg-name" maxlength="24" placeholder="Sala de ${ui.escapeHtml(self.nickname || '')}" />
    </div>
    <div class="field-row">
      <label>Número de jogadores</label>
      <select id="cfg-numplayers">
        <option value="2">2 (1x1)</option>
        <option value="4">4 (2x2)</option>
      </select>
    </div>
    <div class="field-row">
      <label>Variante</label>
      <select id="cfg-variant">
        <option value="paulista">Truco Paulista</option>
        <option value="mineiro">Truco Mineiro</option>
      </select>
    </div>
    <div class="field-row">
      <label>Pontuação da partida</label>
      <select id="cfg-points">
        <option value="12">12 pontos</option>
        <option value="24">24 pontos</option>
      </select>
    </div>
    <div class="field-row">
      <label>Tempo por jogada</label>
      <select id="cfg-time">
        <option value="15">15s</option>
        <option value="30" selected>30s</option>
        <option value="45">45s</option>
        <option value="60">60s</option>
      </select>
    </div>
    <div class="checkbox-row">
      <input type="checkbox" id="cfg-flor" />
      <label for="cfg-flor">Jogar com Flor (somente 1x1)</label>
    </div>
    <div class="checkbox-row">
      <input type="checkbox" id="cfg-private" />
      <label for="cfg-private">Sala privada (acesso por código)</label>
    </div>
    <div class="modal-actions">
      <button class="btn btn-ghost" id="btn-cancel-create">Cancelar</button>
      <button class="btn btn-primary" id="btn-confirm-create">Criar</button>
    </div>
  `);
  document.getElementById('btn-cancel-create').onclick = ui.closeModal;
  document.getElementById('btn-confirm-create').onclick = () => {
    const config = {
      numPlayers: Number(document.getElementById('cfg-numplayers').value),
      variant: document.getElementById('cfg-variant').value,
      pointsToWin: Number(document.getElementById('cfg-points').value),
      timePerPlay: Number(document.getElementById('cfg-time').value),
      flor: document.getElementById('cfg-flor').checked,
      isPrivate: document.getElementById('cfg-private').checked,
    };
    const name = document.getElementById('cfg-name').value.trim();
    ui.closeModal();
    createRoom(config, name);
  };
});

document.getElementById('btn-add-bot').addEventListener('click', addBot);
document.getElementById('btn-start-match').addEventListener('click', startMatch);
document.getElementById('btn-leave-room').addEventListener('click', leaveRoom);
document.getElementById('btn-leave-game').addEventListener('click', leaveRoom);

document.getElementById('btn-copy-code').addEventListener('click', async () => {
  const code = document.getElementById('room-code-display').textContent;
  try {
    await navigator.clipboard.writeText(code);
    ui.toast('Código copiado!', 'success');
  } catch {
    ui.toast(code, 'info');
  }
});
