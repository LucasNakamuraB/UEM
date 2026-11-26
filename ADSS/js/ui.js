import { cardLabel, hasFlor } from './cards.js';

const $ = (id) => document.getElementById(id);

export function showScreen(name) {
  document.querySelectorAll('.screen').forEach((el) => el.classList.add('hidden'));
  $(`screen-${name}`).classList.remove('hidden');
}

export function setUserBadge(nickname) {
  const el = $('user-badge');
  if (!nickname) {
    el.classList.add('hidden');
    return;
  }
  el.textContent = nickname;
  el.classList.remove('hidden');
}

export function toast(message, type = 'info') {
  const root = $('toast-root');
  const div = document.createElement('div');
  div.className = `toast ${type}`;
  div.textContent = message;
  root.appendChild(div);
  setTimeout(() => div.remove(), 3500);
}

export function openModal(innerHtml) {
  const root = $('modal-root');
  root.innerHTML = `<div class="modal-box">${innerHtml}</div>`;
  root.classList.remove('hidden');
  root.onclick = (e) => {
    if (e.target === root) closeModal();
  };
}

export function closeModal() {
  $('modal-root').classList.add('hidden');
  $('modal-root').innerHTML = '';
}

export function renderRoomList(rooms, onJoin) {
  const list = $('room-list');
  const empty = $('room-list-empty');
  list.innerHTML = '';
  if (rooms.length === 0) {
    empty.classList.remove('hidden');
    return;
  }
  empty.classList.add('hidden');
  for (const room of rooms) {
    const li = document.createElement('li');
    li.innerHTML = `<span>${escapeHtml(room.name)} <span class="muted">(${room.playerCount}/${room.maxPlayers})</span></span><span class="muted">${room.code}</span>`;
    li.addEventListener('click', () => onJoin(room.code));
    list.appendChild(li);
  }
}

export function renderRoomScreen(info, selfId, isHost, canStart) {
  $('room-code-display').textContent = info.code;
  const cfg = info.config;
  $('room-config-summary').innerHTML = [
    `${cfg.numPlayers} jogadores`,
    cfg.variant === 'mineiro' ? 'Truco Mineiro' : 'Truco Paulista',
    cfg.flor ? 'Com flor' : 'Sem flor',
    `${cfg.pointsToWin} pontos`,
    `${cfg.timePerPlay}s por jogada`,
    info.private ? 'Privada' : 'Pública',
  ].map((t) => `<span>${t}</span>`).join('');

  const list = $('room-players-list');
  list.innerHTML = '';
  info.players.forEach((p) => {
    const li = document.createElement('li');
    li.className = `team-${p.team}`;
    li.innerHTML = `<span>${escapeHtml(p.nickname)}${p.id === selfId ? ' (você)' : ''}${p.isBot ? ' 🤖' : ''}</span><span class="muted">Dupla ${p.team === 0 ? 'A' : 'B'}</span>`;
    list.appendChild(li);
  });

  $('room-host-controls').classList.toggle('hidden', !isHost);
  $('room-wait-msg').classList.toggle('hidden', isHost);
  $('btn-start-match').disabled = !canStart;
  $('btn-add-bot').disabled = info.players.length >= cfg.numPlayers;
}

export function renderGame(state, selfId, handlers) {
  const { hand } = state;
  $('score-a').textContent = state.scores[0];
  $('score-b').textContent = state.scores[1];
  $('points-to-win-label').textContent = `(até ${state.config.pointsToWin})`;

  if (!hand) return;

  const me = state.players.find((p) => p.id === selfId);
  const mySeat = me.seat;
  const myTeam = me.team;

  $('vira-card').textContent = cardLabel(hand.vira);
  $('manilha-rank').textContent = hand.manilhaRank;
  $('hand-value').textContent = hand.value;

  renderOpponents(state, mySeat);
  renderRounds(hand, state.players);
  renderTurnIndicator(state, me);
  renderPendingBox(state, me, handlers);
  renderMyHand(state, me, handlers);
  renderActionBar(state, me, handlers);
  renderLog(state.log);
}

function renderOpponents(state, mySeat) {
  const row = $('opponents-row');
  row.innerHTML = '';
  const n = state.players.length;
  const others = state.players.filter((p) => p.seat !== mySeat).sort((a, b) => a.seat - b.seat);
  others.forEach((p) => {
    const div = document.createElement('div');
    div.className = 'opponent-slot';
    if (state.hand.turnSeat === p.seat) div.classList.add('active-turn');
    const cardCount = state.hand.handsBySeat[p.seat] ? state.hand.handsBySeat[p.seat].length : 0;
    div.innerHTML = `
      <div class="opponent-name">${escapeHtml(p.nickname)}${p.isBot ? ' 🤖' : ''} <span class="muted">(Dupla ${p.team === 0 ? 'A' : 'B'})</span></div>
      <div class="opponent-cards">${'<div class="card-back"></div>'.repeat(cardCount)}</div>
    `;
    row.appendChild(div);
  });
}

function renderRounds(hand, players) {
  const box = $('rounds-display');
  box.innerHTML = '';
  const nickOf = (seat) => players.find((p) => p.seat === seat)?.nickname || '?';
  const allRounds = hand.table.concat(hand.currentRoundCards.length ? [hand.currentRoundCards] : []);
  allRounds.forEach((round, idx) => {
    const slot = document.createElement('div');
    slot.className = 'round-slot';
    slot.innerHTML = `<div class="muted">Rodada ${idx + 1}</div><div class="cards-played">${round.map((e) => {
      const isManilha = e.card.rank === hand.manilhaRank;
      return `<div class="play-card ${isManilha ? 'manilha' : ''}" title="${escapeHtml(nickOf(e.seat))}">${cardLabel(e.card)}</div>`;
    }).join('')}</div>`;
    box.appendChild(slot);
  });
}

function renderTurnIndicator(state, me) {
  const el = $('turn-indicator');
  const hand = state.hand;
  if (hand.finished) {
    el.textContent = 'Mão encerrada. Preparando próxima mão...';
    return;
  }
  if (hand.pendingTruco) {
    const callerNick = state.players.find((p) => p.id === hand.pendingTruco.callerPlayerId)?.nickname;
    el.textContent = me.team === hand.pendingTruco.targetTeam
      ? `${callerNick} pediu ${hand.pendingTruco.level.label}! Responda.`
      : `Aguardando resposta ao ${hand.pendingTruco.level.label}...`;
    return;
  }
  if (hand.envido.pendingCall) {
    const callerNick = state.players.find((p) => p.id === hand.envido.pendingCall.callerPlayerId)?.nickname;
    el.textContent = me.team === hand.envido.pendingCall.targetTeam
      ? `${callerNick} pediu ${hand.envido.pendingCall.level.label}! Responda.`
      : `Aguardando resposta ao ${hand.envido.pendingCall.level.label}...`;
    return;
  }
  if (hand.turnSeat === me.seat) {
    el.textContent = 'Sua vez de jogar!';
  } else {
    const nick = state.players.find((p) => p.seat === hand.turnSeat)?.nickname;
    el.textContent = `Vez de ${nick}...`;
  }
}

function renderPendingBox(state, me, handlers) {
  const box = $('pending-call-box');
  const hand = state.hand;
  box.innerHTML = '';
  box.classList.add('hidden');

  if (hand.pendingTruco && me.team === hand.pendingTruco.targetTeam) {
    box.classList.remove('hidden');
    box.innerHTML = `
      <div>${hand.pendingTruco.level.label} pedido! O que você faz?</div>
      <div class="pending-call-actions">
        <button class="btn btn-primary btn-sm" data-act="accept">Aceitar</button>
        <button class="btn btn-secondary btn-sm" data-act="raise">Aumentar</button>
        <button class="btn btn-danger btn-sm" data-act="run">Correr</button>
      </div>`;
    box.querySelector('[data-act="accept"]').onclick = () => handlers.onRespondTruco('accept');
    box.querySelector('[data-act="raise"]').onclick = () => handlers.onRespondTruco('raise');
    box.querySelector('[data-act="run"]').onclick = () => handlers.onRespondTruco('run');
    return;
  }

  if (hand.envido.pendingCall && me.team === hand.envido.pendingCall.targetTeam) {
    box.classList.remove('hidden');
    box.innerHTML = `
      <div>${hand.envido.pendingCall.level.label} pedido! O que você faz?</div>
      <div class="pending-call-actions">
        <button class="btn btn-primary btn-sm" data-act="accept">Aceitar</button>
        <button class="btn btn-secondary btn-sm" data-act="raise">Aumentar</button>
        <button class="btn btn-danger btn-sm" data-act="decline">Não aceito</button>
      </div>`;
    box.querySelector('[data-act="accept"]').onclick = () => handlers.onRespondEnvido('accept');
    box.querySelector('[data-act="raise"]').onclick = () => handlers.onRespondEnvido('raise');
    box.querySelector('[data-act="decline"]').onclick = () => handlers.onRespondEnvido('decline');
  }
}

function renderMyHand(state, me, handlers) {
  const box = $('my-hand');
  box.innerHTML = '';
  const hand = state.hand;
  const cards = hand.handsBySeat[me.seat] || [];
  const canPlay = !hand.finished && hand.turnSeat === me.seat && !hand.pendingTruco && !hand.envido.pendingCall;
  cards.forEach((card) => {
    const div = document.createElement('div');
    const isManilha = card.rank === hand.manilhaRank;
    div.className = `play-card ${isManilha ? 'manilha' : ''} ${canPlay ? '' : 'disabled'}`;
    div.textContent = cardLabel(card);
    if (canPlay) div.onclick = () => handlers.onPlayCard(card.id);
    box.appendChild(div);
  });
}

function renderActionBar(state, me, handlers) {
  const bar = $('action-bar');
  bar.innerHTML = '';
  const hand = state.hand;
  if (hand.finished || state.status !== 'playing') return;
  const blocked = !!hand.pendingTruco || !!hand.envido.pendingCall;

  const addBtn = (label, onClick, cls = 'btn-secondary') => {
    const btn = document.createElement('button');
    btn.className = `btn ${cls} btn-sm`;
    btn.textContent = label;
    btn.disabled = blocked;
    btn.onclick = onClick;
    bar.appendChild(btn);
  };

  if (hand.value < 12) {
    addBtn('Truco!', () => handlers.onCallTruco());
  }

  if (hand.canCallEnvido) {
    addBtn('Envido', () => handlers.onCallEnvido('envido'));
  }

  const myCards = (hand.handsBySeat[me.seat] || []).filter((c) => !c.hidden);
  if (hand.canCallFlor && hasFlor(myCards) && !hand.flor.declarations[me.id]) {
    addBtn('Flor!', () => handlers.onDeclareFlor(), 'btn-primary');
  }

  addBtn('Correr', () => handlers.onRun(), 'btn-danger');
}

function renderLog(log) {
  const box = $('game-log');
  box.innerHTML = log.map((l) => `<div>${escapeHtml(l)}</div>`).join('');
  box.scrollTop = box.scrollHeight;
}

export function rulesModalHtml() {
  return `
    <h3>Regras implementadas (Truco Paulista simplificado)</h3>
    <div class="rules-content">
      <p>Baralho de 40 cartas (sem 8, 9 e 10). Força das cartas, da mais fraca à mais forte:
      4, 5, 6, 7, Q, J, K, A, 2, 3. A "vira" define a manilha (carta seguinte na sequência),
      e as 4 manilhas se ordenam por naipe: Paus &gt; Copas &gt; Espadas &gt; Ouros.</p>
      <h4>Mão</h4>
      <p>Cada mão tem até 3 rodadas. Vence quem fizer 2 rodadas; empates passam a decisão
      para a rodada seguinte; se as 3 rodadas empatarem, vence quem jogou primeiro na mão.</p>
      <h4>Truco</h4>
      <p>Qualquer jogador pode pedir Truco (3), Seis (6), Nove (9) ou Doze (12), sempre aumentando
      um nível por vez. A dupla adversária pode aceitar, aumentar ou "correr" (desiste da mão
      e cede o valor anterior à aposta).</p>
      <h4>Correr</h4>
      <p>A qualquer momento um jogador pode desistir da mão atual, cedendo à dupla adversária
      os pontos que a mão vale no momento.</p>
      <h4>Envido / Flor (somente 1x1)</h4>
      <p>Envido pode ser pedido antes da primeira carta jogada na mão, com escalonamento
      Envido (2) → Real Envido (+3) → Falta Envido (pontos restantes para o vencedor da partida).
      Quem tiver 3 cartas do mesmo naipe pode declarar Flor, ganhando 3 pontos automaticamente
      e cancelando o envido daquela mão.</p>
      <h4>Pontuação</h4>
      <p>A partida é configurável para 12 ou 24 pontos; vence a dupla que atingir a pontuação primeiro.</p>
    </div>
    <div class="modal-actions"><button class="btn btn-primary" id="btn-close-rules">Entendi</button></div>
  `;
}

export function escapeHtml(str) {
  const div = document.createElement('div');
  div.textContent = str;
  return div.innerHTML;
}
