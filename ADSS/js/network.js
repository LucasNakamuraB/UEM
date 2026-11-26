const DIRECTORY_KEY = 'truco:rooms:v1';
const STALE_MS = 15000;

export function genId() {
  return Math.random().toString(36).slice(2, 10) + Date.now().toString(36);
}

export function genRoomCode() {
  const chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
  let code = '';
  for (let i = 0; i < 5; i++) code += chars[Math.floor(Math.random() * chars.length)];
  return code;
}

export const RoomDirectory = {
  readAll() {
    try {
      return JSON.parse(localStorage.getItem(DIRECTORY_KEY) || '{}');
    } catch {
      return {};
    }
  },
  writeAll(rooms) {
    localStorage.setItem(DIRECTORY_KEY, JSON.stringify(rooms));
  },
  upsert(code, info) {
    const rooms = this.readAll();
    rooms[code] = { ...info, code, updatedAt: Date.now() };
    this.writeAll(rooms);
  },
  remove(code) {
    const rooms = this.readAll();
    delete rooms[code];
    this.writeAll(rooms);
  },
  listPublic() {
    const rooms = this.readAll();
    const now = Date.now();
    return Object.values(rooms).filter((r) => !r.private && now - r.updatedAt < STALE_MS);
  },
  get(code) {
    const rooms = this.readAll();
    const r = rooms[code];
    if (!r) return null;
    if (Date.now() - r.updatedAt > STALE_MS) return null;
    return r;
  },
  subscribe(callback) {
    const handler = (e) => {
      if (e.key === DIRECTORY_KEY) callback();
    };
    window.addEventListener('storage', handler);
    return () => window.removeEventListener('storage', handler);
  },
};

export class RoomChannel {
  constructor(roomCode, selfId) {
    this.roomCode = roomCode;
    this.selfId = selfId;
    this.channel = new BroadcastChannel(`truco-room-${roomCode}`);
    this.handlers = [];
    this.channel.onmessage = (ev) => {
      const msg = ev.data;
      if (!msg || msg.senderId === this.selfId) return;
      this.handlers.forEach((h) => h(msg));
    };
  }

  on(handler) {
    this.handlers.push(handler);
    return () => {
      this.handlers = this.handlers.filter((h) => h !== handler);
    };
  }

  send(type, payload) {
    this.channel.postMessage({ type, payload, senderId: this.selfId, ts: Date.now() });
  }

  close() {
    this.channel.close();
  }
}
