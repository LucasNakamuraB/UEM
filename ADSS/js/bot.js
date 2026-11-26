import { cardStrength, envidoValue, hasFlor } from './cards.js';

function sortByStrength(cards, manilhaRank) {
  return cards.slice().sort((a, b) => cardStrength(a, manilhaRank) - cardStrength(b, manilhaRank));
}

function handStrengthScore(cards, manilhaRank) {
  return cards.reduce((sum, c) => sum + cardStrength(c, manilhaRank), 0) / cards.length;
}

export function botChooseCard(cards, manilhaRank, context) {
  const sorted = sortByStrength(cards, manilhaRank);
  const { bestOnTable } = context;
  if (!bestOnTable) {
    // leading the round: play a middling card, save the strongest for later
    return sorted[Math.floor(sorted.length / 2)].id;
  }
  const winning = sorted.filter((c) => cardStrength(c, manilhaRank) > cardStrength(bestOnTable, manilhaRank));
  if (winning.length > 0) return winning[0].id;
  return sorted[0].id;
}

export function botTrucoDecision(cards, manilhaRank, currentValue) {
  const score = handStrengthScore(cards, manilhaRank);
  if (score > 70 && currentValue < 3) return 'call';
  return null;
}

export function botTrucoResponse(cards, manilhaRank, pendingLevelValue) {
  const score = handStrengthScore(cards, manilhaRank);
  const threshold = 20 + pendingLevelValue * 6;
  if (score >= threshold + 20) return 'raise';
  if (score >= threshold) return 'accept';
  return 'run';
}

export function botEnvidoDecision(cards) {
  const value = envidoValue(cards);
  if (value >= 28) return 'envido';
  return null;
}

export function botEnvidoResponse(cards, levelKey) {
  const value = envidoValue(cards);
  const thresholds = { envido: 24, realEnvido: 28, faltaEnvido: 31 };
  if (value >= (thresholds[levelKey] || 24)) return 'accept';
  return 'decline';
}

export function botShouldDeclareFlor(cards) {
  return hasFlor(cards);
}
