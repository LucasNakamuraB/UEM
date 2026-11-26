export const RANK_ORDER = ['4', '5', '6', '7', 'Q', 'J', 'K', 'A', '2', '3'];
export const SUITS = ['C', 'H', 'S', 'D'];
export const SUIT_SYMBOL = { C: '♣', H: '♥', S: '♠', D: '♦' };
export const SUIT_NAME = { C: 'Paus', H: 'Copas', S: 'Espadas', D: 'Ouros' };
export const MANILHA_SUIT_ORDER = ['D', 'S', 'H', 'C']; // weakest -> strongest
export const RANK_LABEL = { '4': '4', '5': '5', '6': '6', '7': '7', Q: 'Q', J: 'J', K: 'K', A: 'A', '2': '2', '3': '3' };
export const ENVIDO_VALUE = { '4': 4, '5': 5, '6': 6, '7': 7, Q: 0, J: 0, K: 0, A: 1, '2': 2, '3': 3 };

export function buildDeck() {
  const deck = [];
  for (const suit of SUITS) {
    for (const rank of RANK_ORDER) {
      deck.push({ id: `${rank}-${suit}`, rank, suit });
    }
  }
  return deck;
}

export function shuffle(deck) {
  const arr = deck.slice();
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

export function manilhaRankFromVira(viraRank) {
  const idx = RANK_ORDER.indexOf(viraRank);
  return RANK_ORDER[(idx + 1) % RANK_ORDER.length];
}

export function cardStrength(card, manilhaRank) {
  if (card.rank === manilhaRank) {
    return 100 + MANILHA_SUIT_ORDER.indexOf(card.suit);
  }
  return RANK_ORDER.indexOf(card.rank);
}

export function compareCards(a, b, manilhaRank) {
  const sa = cardStrength(a, manilhaRank);
  const sb = cardStrength(b, manilhaRank);
  if (sa > sb) return 1;
  if (sa < sb) return -1;
  return 0;
}

export function isManilha(card, manilhaRank) {
  return card.rank === manilhaRank;
}

export function envidoValue(cards) {
  const bySuit = {};
  for (const c of cards) {
    (bySuit[c.suit] = bySuit[c.suit] || []).push(c);
  }
  let best = 0;
  let foundPair = false;
  for (const suit in bySuit) {
    const group = bySuit[suit];
    if (group.length >= 2) {
      foundPair = true;
      const values = group.map((c) => ENVIDO_VALUE[c.rank]).sort((x, y) => y - x);
      const sum = 20 + values[0] + values[1];
      if (sum > best) best = sum;
    }
  }
  if (!foundPair) {
    best = Math.max(...cards.map((c) => ENVIDO_VALUE[c.rank]));
  }
  return best;
}

export function florValue(cards) {
  const suits = new Set(cards.map((c) => c.suit));
  if (suits.size !== 1) return null;
  const sum = cards.reduce((acc, c) => acc + ENVIDO_VALUE[c.rank], 0);
  return 20 + sum;
}

export function hasFlor(cards) {
  return new Set(cards.map((c) => c.suit)).size === 1;
}

export function cardLabel(card) {
  return `${RANK_LABEL[card.rank]}${SUIT_SYMBOL[card.suit]}`;
}
