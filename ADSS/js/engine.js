import {
  buildDeck, shuffle, manilhaRankFromVira, compareCards,
  envidoValue, florValue, hasFlor,
} from './cards.js';

const TRUCO_LEVELS = [
  { key: 'truco', label: 'Truco', value: 3 },
  { key: 'seis', label: 'Seis', value: 6 },
  { key: 'nove', label: 'Nove', value: 9 },
  { key: 'doze', label: 'Doze', value: 12 },
];

const ENVIDO_LEVELS = [
  { key: 'envido', label: 'Envido', addValue: 2 },
  { key: 'realEnvido', label: 'Real Envido', addValue: 3 },
  { key: 'faltaEnvido', label: 'Falta Envido', addValue: null },
];

function other(team) {
  return team === 0 ? 1 : 0;
}

export class TrucoEngine {
  constructor(config, players, onChange) {
    this.config = config;
    this.players = players; // [{id, nickname, isBot, seat, team}]
    this.onChange = onChange || (() => {});
    this.scores = [0, 0];
    this.dealerSeat = 0;
    this.status = 'waiting';
    this.hand = null;
    this.winnerTeam = null;
    this.log = [];
  }

  playerBySeat(seat) {
    return this.players.find((p) => p.seat === seat);
  }

  playerById(id) {
    return this.players.find((p) => p.id === id);
  }

  teamOf(playerId) {
    const p = this.playerById(playerId);
    return p ? p.team : null;
  }

  pushLog(msg) {
    this.log.push(msg);
    if (this.log.length > 60) this.log.shift();
  }

  emit() {
    this.onChange(this.getState());
  }

  start() {
    if (this.status !== 'waiting') return;
    this.status = 'playing';
    this.dealerSeat = 0;
    this.pushLog('Partida iniciada.');
    this.startHand();
  }

  nextSeat(seat) {
    const n = this.players.length;
    return (seat + 1) % n;
  }

  startHand() {
    const n = this.players.length;
    const deck = shuffle(buildDeck());
    const handsBySeat = {};
    for (let i = 0; i < n; i++) handsBySeat[i] = [];
    for (let c = 0; c < 3; c++) {
      for (let i = 0; i < n; i++) {
        handsBySeat[i].push(deck.pop());
      }
    }
    const vira = deck.pop();
    const manilhaRank = manilhaRankFromVira(vira.rank);
    const firstSeat = this.nextSeat(this.dealerSeat);

    this.hand = {
      vira,
      manilhaRank,
      handsBySeat,
      table: [], // array of rounds: each round is array of {seat, card}
      currentRoundCards: [],
      currentRound: 0,
      leaderSeat: firstSeat,
      turnSeat: firstSeat,
      firstSeatOfHand: firstSeat,
      value: 1,
      pendingTruco: null,
      lastTrucoLevelIndex: -1,
      envido: { resolved: false, pendingCall: null, lastLevelIndex: -1 },
      flor: { declarations: {} },
      roundWinners: [], // seat/team per completed round, null = tie
      finished: false,
    };
    this.pushLog(`Nova mão. Vira: ${vira.rank}${vira.suit}. Manilha: ${manilhaRank}.`);
    this.emit();
  }

  getState() {
    return {
      config: this.config,
      players: this.players,
      scores: this.scores.slice(),
      dealerSeat: this.dealerSeat,
      status: this.status,
      winnerTeam: this.winnerTeam,
      log: this.log.slice(-15),
      hand: this.hand
        ? {
          vira: this.hand.vira,
          manilhaRank: this.hand.manilhaRank,
          handsBySeat: this.hand.handsBySeat,
          table: this.hand.table,
          currentRoundCards: this.hand.currentRoundCards,
          currentRound: this.hand.currentRound,
          turnSeat: this.hand.turnSeat,
          leaderSeat: this.hand.leaderSeat,
          firstSeatOfHand: this.hand.firstSeatOfHand,
          value: this.hand.value,
          pendingTruco: this.hand.pendingTruco,
          envido: this.hand.envido,
          flor: this.hand.flor,
          roundWinners: this.hand.roundWinners,
          canCallEnvido: this.canCallEnvidoNow(),
          canCallFlor: this.canCallFlorNow(),
          finished: this.hand.finished,
        }
        : null,
    };
  }

  canCallEnvidoNow() {
    if (!this.hand) return false;
    if (this.players.length !== 2) return false;
    if (this.hand.envido.resolved) return false;
    if (this.hand.currentRound !== 0) return false;
    if (this.hand.currentRoundCards.length !== 0) return false;
    if (this.hand.pendingTruco) return false;
    return true;
  }

  canCallFlorNow() {
    if (!this.hand || !this.config.flor) return false;
    if (this.players.length !== 2) return false;
    if (this.hand.currentRound !== 0) return false;
    return this.hand.table.length === 0 && this.hand.currentRoundCards.length === 0;
  }

  // ---------- CARD PLAY ----------

  playCard(playerId, cardId) {
    const player = this.playerById(playerId);
    if (!player || !this.hand || this.status !== 'playing') return { ok: false, error: 'Estado inválido.' };
    if (this.hand.pendingTruco) return { ok: false, error: 'Responda ao pedido de truco antes de jogar.' };
    if (this.hand.envido.pendingCall) return { ok: false, error: 'Responda ao envido antes de jogar.' };
    if (player.seat !== this.hand.turnSeat) return { ok: false, error: 'Não é sua vez.' };

    const seatHand = this.hand.handsBySeat[player.seat];
    const idx = seatHand.findIndex((c) => c.id === cardId);
    if (idx === -1) return { ok: false, error: 'Carta inválida.' };

    const [card] = seatHand.splice(idx, 1);
    this.hand.currentRoundCards.push({ seat: player.seat, card });
    this.pushLog(`${player.nickname} jogou ${card.rank}${card.suit}.`);

    if (this.hand.currentRoundCards.length === this.players.length) {
      this.resolveRound();
    } else {
      this.hand.turnSeat = this.nextSeat(this.hand.turnSeat);
    }
    this.emit();
    return { ok: true };
  }

  resolveRound() {
    const cards = this.hand.currentRoundCards;
    const { manilhaRank } = this.hand;
    let topEntries = [cards[0]];
    for (let i = 1; i < cards.length; i++) {
      const cmp = compareCards(cards[i].card, topEntries[0].card, manilhaRank);
      if (cmp > 0) topEntries = [cards[i]];
      else if (cmp === 0) topEntries.push(cards[i]);
    }

    let winnerSeat = null;
    let tie = false;
    if (this.players.length === 2) {
      tie = topEntries.length > 1;
      winnerSeat = tie ? null : topEntries[0].seat;
    } else {
      // team mode: best card per team decides; tie if best teams are equal strength
      const byTeam = { 0: [], 1: [] };
      for (const entry of cards) {
        const p = this.playerBySeat(entry.seat);
        byTeam[p.team].push(entry);
      }
      const bestOf = (list) => list.reduce((best, e) => (
        !best || compareCards(e.card, best.card, manilhaRank) > 0 ? e : best
      ), null);
      const best0 = bestOf(byTeam[0]);
      const best1 = bestOf(byTeam[1]);
      const cmp = compareCards(best0.card, best1.card, manilhaRank);
      if (cmp === 0) {
        tie = true;
      } else {
        winnerSeat = cmp > 0 ? best0.seat : best1.seat;
      }
    }

    const winnerTeam = tie ? null : this.playerBySeat(winnerSeat).team;
    this.hand.roundWinners.push({ round: this.hand.currentRound, winnerSeat, winnerTeam, tie });
    this.hand.table.push(cards.slice());

    if (tie) {
      this.pushLog(`Rodada ${this.hand.currentRound + 1} empatou.`);
    } else {
      this.pushLog(`${this.playerBySeat(winnerSeat).nickname} venceu a rodada ${this.hand.currentRound + 1}.`);
    }

    const decision = this.checkHandWinner();
    if (decision !== null) {
      this.finishHand(decision);
      return;
    }

    this.hand.currentRound += 1;
    this.hand.currentRoundCards = [];
    if (!tie) {
      this.hand.leaderSeat = winnerSeat;
      this.hand.turnSeat = winnerSeat;
    } else {
      this.hand.turnSeat = this.hand.leaderSeat;
    }
  }

  checkHandWinner() {
    const rw = this.hand.roundWinners;
    const wins = [0, 0];
    for (const r of rw) {
      if (!r.tie) wins[r.winnerTeam] += 1;
    }
    if (wins[0] >= 2) return 0;
    if (wins[1] >= 2) return 1;
    if (rw.length >= 3) {
      // all three rounds done without 2 clean wins -> resolve by rule
      if (wins[0] > wins[1]) return 0;
      if (wins[1] > wins[0]) return 1;
      return this.playerBySeat(this.hand.firstSeatOfHand).team;
    }
    if (rw.length === 2) {
      const [r1, r2] = rw;
      if (r1.tie && !r2.tie) return r2.winnerTeam;
      if (!r1.tie && r2.tie) return r1.winnerTeam;
      if (r1.tie && r2.tie) return null; // go to round 3
    }
    return null;
  }

  finishHand(winningTeam) {
    this.scores[winningTeam] += this.hand.value;
    this.hand.finished = true;
    this.pushLog(`Mão vencida pela dupla ${winningTeam === 0 ? 'A' : 'B'} (+${this.hand.value} pts).`);
    this.checkMatchEnd();
  }

  checkMatchEnd() {
    if (this.scores[0] >= this.config.pointsToWin || this.scores[1] >= this.config.pointsToWin) {
      this.status = 'finished';
      this.winnerTeam = this.scores[0] > this.scores[1] ? 0 : 1;
      this.pushLog(`Partida encerrada! Dupla ${this.winnerTeam === 0 ? 'A' : 'B'} venceu.`);
      return true;
    }
    return false;
  }

  advanceHand() {
    if (this.status !== 'playing') return;
    this.dealerSeat = this.nextSeat(this.dealerSeat);
    this.startHand();
  }

  // ---------- TRUCO ----------

  callTruco(playerId) {
    const player = this.playerById(playerId);
    if (!player || !this.hand) return { ok: false, error: 'Estado inválido.' };
    if (this.hand.pendingTruco) return { ok: false, error: 'Já existe um pedido pendente.' };
    if (this.hand.envido.pendingCall) return { ok: false, error: 'Resolva o envido primeiro.' };
    const nextLevelIndex = this.hand.lastTrucoLevelIndex + 1;
    if (nextLevelIndex >= TRUCO_LEVELS.length) return { ok: false, error: 'Valor máximo já atingido.' };
    const callerTeam = player.team;
    const lastCallerTeam = this.hand.lastTrucoCallerTeam;
    if (lastCallerTeam === callerTeam) return { ok: false, error: 'Aguarde a resposta da dupla adversária.' };

    this.hand.pendingTruco = {
      levelIndex: nextLevelIndex,
      level: TRUCO_LEVELS[nextLevelIndex],
      callerTeam,
      callerPlayerId: playerId,
      targetTeam: other(callerTeam),
      previousValue: this.hand.value,
    };
    this.pushLog(`${player.nickname} pediu ${TRUCO_LEVELS[nextLevelIndex].label}!`);
    this.emit();
    return { ok: true };
  }

  respondTruco(playerId, action) {
    const player = this.playerById(playerId);
    const pending = this.hand && this.hand.pendingTruco;
    if (!player || !pending) return { ok: false, error: 'Nada pendente.' };
    if (player.team !== pending.targetTeam) return { ok: false, error: 'Não é sua dupla que responde.' };

    if (action === 'accept') {
      this.hand.value = pending.level.value;
      this.hand.lastTrucoLevelIndex = pending.levelIndex;
      this.hand.lastTrucoCallerTeam = pending.callerTeam;
      this.hand.pendingTruco = null;
      this.pushLog(`${player.nickname} aceitou. Mão vale ${this.hand.value} pontos.`);
    } else if (action === 'run') {
      this.scores[pending.callerTeam] += pending.previousValue;
      this.hand.finished = true;
      this.hand.pendingTruco = null;
      this.pushLog(`${player.nickname} correu. Dupla ${pending.callerTeam === 0 ? 'A' : 'B'} ganha ${pending.previousValue} pts.`);
      this.checkMatchEnd();
    } else if (action === 'raise') {
      const nextLevelIndex = pending.levelIndex + 1;
      if (nextLevelIndex >= TRUCO_LEVELS.length) return { ok: false, error: 'Valor máximo já atingido.' };
      this.hand.lastTrucoLevelIndex = pending.levelIndex;
      this.hand.lastTrucoCallerTeam = pending.callerTeam;
      this.hand.pendingTruco = {
        levelIndex: nextLevelIndex,
        level: TRUCO_LEVELS[nextLevelIndex],
        callerTeam: player.team,
        callerPlayerId: playerId,
        targetTeam: other(player.team),
        previousValue: pending.level.value,
      };
      this.pushLog(`${player.nickname} aumentou para ${TRUCO_LEVELS[nextLevelIndex].label}!`);
    }
    this.emit();
    return { ok: true };
  }

  // ---------- CORRER (desistir da mão) ----------

  runFromHand(playerId) {
    const player = this.playerById(playerId);
    if (!player || !this.hand || this.hand.finished) return { ok: false, error: 'Estado inválido.' };
    if (this.hand.pendingTruco && player.team === this.hand.pendingTruco.targetTeam) {
      return this.respondTruco(playerId, 'run');
    }
    const opponentTeam = other(player.team);
    this.scores[opponentTeam] += this.hand.value;
    this.hand.finished = true;
    this.pushLog(`${player.nickname} correu da mão. Dupla ${opponentTeam === 0 ? 'A' : 'B'} ganha ${this.hand.value} pts.`);
    this.checkMatchEnd();
    this.emit();
    return { ok: true };
  }

  // ---------- ENVIDO ----------

  callEnvido(playerId, levelKey) {
    const player = this.playerById(playerId);
    if (!player || !this.hand) return { ok: false, error: 'Estado inválido.' };
    if (this.players.length !== 2) return { ok: false, error: 'Envido disponível apenas em 1x1.' };
    const env = this.hand.envido;
    if (env.resolved) return { ok: false, error: 'Envido já resolvido nesta mão.' };

    const levelIdx = ENVIDO_LEVELS.findIndex((l) => l.key === levelKey);
    if (levelIdx === -1) return { ok: false, error: 'Tipo inválido.' };

    if (env.pendingCall) return { ok: false, error: 'Já existe envido pendente.' };
    if (levelIdx <= env.lastLevelIndex) return { ok: false, error: 'Nível de envido já utilizado.' };
    if (env.lastLevelIndex >= 0 && this.teamOf(playerId) === env.lastCallerTeam) {
      return { ok: false, error: 'Aguarde a resposta da dupla adversária.' };
    }
    if (!this.canCallEnvidoNow() && env.lastLevelIndex === -1) {
      return { ok: false, error: 'Envido só pode ser pedido antes da primeira carta.' };
    }

    env.pendingCall = {
      levelIndex: levelIdx,
      level: ENVIDO_LEVELS[levelIdx],
      callerTeam: player.team,
      callerPlayerId: playerId,
      targetTeam: other(player.team),
    };
    this.pushLog(`${player.nickname} pediu ${ENVIDO_LEVELS[levelIdx].label}!`);
    this.emit();
    return { ok: true };
  }

  respondEnvido(playerId, action) {
    const player = this.playerById(playerId);
    const env = this.hand && this.hand.envido;
    const pending = env && env.pendingCall;
    if (!player || !pending) return { ok: false, error: 'Nada pendente.' };
    if (player.team !== pending.targetTeam) return { ok: false, error: 'Não é sua dupla que responde.' };

    if (action === 'decline') {
      const payoff = pending.levelIndex === 0
        ? 1
        : ENVIDO_LEVELS.slice(0, pending.levelIndex).reduce((sum, l) => sum + (l.addValue || 0), 0);
      this.scores[pending.callerTeam] += payoff;
      env.resolved = true;
      env.pendingCall = null;
      this.pushLog(`${player.nickname} não aceitou o envido. Dupla ${pending.callerTeam === 0 ? 'A' : 'B'} ganha ${payoff} pts.`);
      this.checkMatchEnd();
    } else if (action === 'raise') {
      const nextLevelIndex = pending.levelIndex + 1;
      if (nextLevelIndex >= ENVIDO_LEVELS.length) return { ok: false, error: 'Nível máximo.' };
      env.lastLevelIndex = pending.levelIndex;
      env.lastCallerTeam = pending.callerTeam;
      env.pendingCall = {
        levelIndex: nextLevelIndex,
        level: ENVIDO_LEVELS[nextLevelIndex],
        callerTeam: player.team,
        callerPlayerId: playerId,
        targetTeam: other(player.team),
      };
      this.pushLog(`${player.nickname} aumentou para ${ENVIDO_LEVELS[nextLevelIndex].label}!`);
    } else if (action === 'accept') {
      env.lastLevelIndex = pending.levelIndex;
      env.lastCallerTeam = pending.callerTeam;
      this.resolveEnvido(pending);
    }
    this.emit();
    return { ok: true };
  }

  resolveEnvido(finalCall) {
    const env = this.hand.envido;
    const p0 = this.players[0];
    const p1 = this.players[1];
    const v0 = envidoValue(this.hand.handsBySeat[p0.seat]);
    const v1 = envidoValue(this.hand.handsBySeat[p1.seat]);
    let winnerPlayer;
    if (v0 === v1) {
      winnerPlayer = this.playerBySeat(this.hand.firstSeatOfHand);
    } else {
      winnerPlayer = v0 > v1 ? p0 : p1;
    }
    let points;
    if (finalCall.level.key === 'faltaEnvido') {
      const leader = Math.max(this.scores[0], this.scores[1]);
      points = Math.max(this.config.pointsToWin - leader, 1);
    } else {
      points = ENVIDO_LEVELS.slice(0, finalCall.levelIndex + 1)
        .reduce((sum, l) => sum + (l.addValue || 0), 0);
    }
    this.scores[winnerPlayer.team] += points;
    env.resolved = true;
    env.pendingCall = null;
    this.pushLog(`Envido: ${p0.nickname}=${v0} x ${p1.nickname}=${v1}. ${winnerPlayer.nickname} ganha ${points} pts.`);
    this.checkMatchEnd();
  }

  declareFlor(playerId) {
    const player = this.playerById(playerId);
    if (!player || !this.hand) return { ok: false, error: 'Estado inválido.' };
    if (!this.config.flor) return { ok: false, error: 'Flor desativada nesta sala.' };
    if (this.players.length !== 2) return { ok: false, error: 'Flor disponível apenas em 1x1.' };
    const cards = this.hand.handsBySeat[player.seat];
    if (!hasFlor(cards)) return { ok: false, error: 'Você não tem flor.' };
    if (this.hand.flor.declarations[playerId]) return { ok: false, error: 'Flor já declarada.' };
    if (!this.canCallFlorNow()) return { ok: false, error: 'Flor só pode ser declarada antes da primeira carta.' };

    const value = florValue(cards);
    this.hand.flor.declarations[playerId] = value;
    this.scores[player.team] += 3;
    this.hand.envido.resolved = true;
    this.pushLog(`${player.nickname} declarou Flor (${value}) e ganhou 3 pts!`);
    this.checkMatchEnd();
    this.emit();
    return { ok: true };
  }
}

export function viewStateFor(state, viewerPlayerId) {
  if (!state.hand) return state;
  const viewer = state.players.find((p) => p.id === viewerPlayerId);
  const viewerSeat = viewer ? viewer.seat : -1;
  const handsBySeat = {};
  for (const seatKey of Object.keys(state.hand.handsBySeat)) {
    const seat = Number(seatKey);
    const cards = state.hand.handsBySeat[seat];
    handsBySeat[seat] = seat === viewerSeat || state.status === 'finished'
      ? cards
      : cards.map(() => ({ hidden: true }));
  }
  return { ...state, hand: { ...state.hand, handsBySeat } };
}

export { TRUCO_LEVELS, ENVIDO_LEVELS };
