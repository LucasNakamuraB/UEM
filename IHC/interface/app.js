/* =========================================================
   Propaws Petshop - Protótipo de Interface (MVP)
   Persistência simulada via localStorage (não há backend real).
   ========================================================= */

const DB_KEY = 'propaws_db_v1';

const SLOT_TIMES = ['09:00','10:00','11:00','13:00','14:00','15:00','16:00','17:00'];
const MONTH_NAMES = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'];

/* ---------- DB bootstrap ---------- */
function loadDB() {
  const raw = localStorage.getItem(DB_KEY);
  if (raw) return JSON.parse(raw);
  const seeded = {
    clientes: [
      { id: 'c1', nome: 'Maria', sobrenome: 'Souza', telefone: '(44) 99888-1122', email: 'maria@exemplo.com' }
    ],
    funcionarios: [
      { id: 'f1', nome: 'Ana', sobrenome: 'Silva', telefone: '(44) 99777-3344', email: 'ana@propaws.com' }
    ],
    pets: [
      { id: 'p1', clienteId: 'c1', nome: 'Rex', animal: 'cachorro', raca: 'Labrador', cor: 'Caramelo', info: '' }
    ],
    servicos: [
      { id: 's1', nome: 'Banho', custo: 40 },
      { id: 's2', nome: 'Tosa', custo: 50 },
      { id: 's3', nome: 'Completo (Banho + Tosa)', custo: 80 }
    ],
    agendamentos: []
  };
  localStorage.setItem(DB_KEY, JSON.stringify(seeded));
  return seeded;
}

let db = loadDB();
function saveDB() { localStorage.setItem(DB_KEY, JSON.stringify(db)); }
function uid(prefix) { return prefix + '_' + Date.now().toString(36) + Math.random().toString(36).slice(2, 7); }

/* ---------- Sessão ---------- */
let session = { role: null, userId: null };

/* ---------- Navegação (pilha de telas, dá suporte a Voltar - H3/R08) ---------- */
let screenStack = ['screen-welcome'];
const header = document.getElementById('app-header');
const headerTitle = document.getElementById('header-title');

const SCREEN_TITLES = {
  'screen-login-cliente': 'Entrar',
  'screen-cadastro-cliente': 'Cadastro de Cliente',
  'screen-login-funcionario': 'Entrar',
  'screen-home-cliente': 'Início',
  'screen-pets': 'Meus Pets',
  'screen-pet-form': 'Pet',
  'screen-agendar': 'Agendar Serviço',
  'screen-pagamento': 'Pagamento',
  'screen-meus-agendamentos': 'Meus Agendamentos',
  'screen-home-funcionario': 'Início',
  'screen-servico-form': 'Cadastrar Serviço',
  'screen-cadastro-funcionario': 'Cadastrar Funcionário',
  'screen-agenda-dia': 'Agenda do Dia',
  'screen-detalhe-agendamento': 'Detalhe',
  'screen-clientes': 'Clientes',
  'screen-config': 'Configurações'
};

const NO_HEADER_SCREENS = new Set(['screen-welcome']);

function showScreen(id, { push = true, title } = {}) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  document.getElementById('app-content').scrollTop = 0;

  if (NO_HEADER_SCREENS.has(id)) {
    header.style.display = 'none';
  } else {
    header.style.display = 'flex';
    headerTitle.textContent = title || SCREEN_TITLES[id] || '';
  }

  if (push) {
    if (screenStack[screenStack.length - 1] !== id) screenStack.push(id);
  }

  onEnterScreen(id);
}

function goBack() {
  if (screenStack.length > 1) {
    screenStack.pop();
    const prev = screenStack[screenStack.length - 1];
    showScreen(prev, { push: false });
  }
}

function resetStackTo(id) {
  screenStack = [id];
  showScreen(id, { push: false });
}

document.getElementById('btn-back').addEventListener('click', goBack);

/* Called whenever a screen becomes active, to (re)render its data */
function onEnterScreen(id) {
  if (id === 'screen-pets') renderPets();
  if (id === 'screen-meus-agendamentos') renderMeusAgendamentos();
  if (id === 'screen-servico-form') renderServicosCadastrados();
  if (id === 'screen-clientes') renderClientes();
  if (id === 'screen-home-cliente') renderHomeCliente();
  if (id === 'screen-home-funcionario') renderHomeFuncionario();
}

/* ---------- Toast (feedback de ações - H1/R01) ---------- */
let toastTimer = null;
function showToast(msg, type = 'default') {
  const toast = document.getElementById('toast');
  toast.textContent = msg;
  toast.className = 'toast show' + (type === 'error' ? ' toast-error' : type === 'success' ? ' toast-success' : '');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => { toast.className = 'toast'; }, 2600);
}

/* ---------- Loading overlay (feedback de operação demorada - H1/R03) ---------- */
function showLoading(text) {
  document.getElementById('loading-text').textContent = text || 'Processando...';
  document.getElementById('loading-overlay').classList.add('active');
}
function hideLoading() {
  document.getElementById('loading-overlay').classList.remove('active');
}

/* ---------- Modal de confirmação (controle sobre operações críticas - H3/R09, H5/R15) ---------- */
function askConfirm(message, onYes) {
  const modal = document.getElementById('modal-confirm');
  document.getElementById('confirm-message').textContent = message;
  modal.classList.add('active');

  const btnYes = document.getElementById('btn-confirm-sim');
  const btnNo = document.getElementById('btn-confirm-nao');

  function close() {
    modal.classList.remove('active');
    btnYes.removeEventListener('click', yesHandler);
    btnNo.removeEventListener('click', close);
  }
  function yesHandler() { close(); onYes(); }

  btnYes.addEventListener('click', yesHandler);
  btnNo.addEventListener('click', close);
}

/* ---------- Validações (prevenção de erros - H5) ---------- */
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const PHONE_RE = /^[\d\s()+-]{8,20}$/;

function validateRequired(fields) {
  for (const [value, label] of fields) {
    if (!value || !String(value).trim()) return `Preencha o campo "${label}".`;
  }
  return null;
}

/* =========================================================
   WELCOME / LOGIN / CADASTRO
   ========================================================= */

document.getElementById('btn-sou-cliente').addEventListener('click', () => {
  resetStackTo('screen-welcome');
  showScreen('screen-login-cliente');
});

document.getElementById('btn-sou-funcionario').addEventListener('click', () => {
  resetStackTo('screen-welcome');
  showScreen('screen-login-funcionario');
});

document.getElementById('link-cadastro-cliente').addEventListener('click', (e) => {
  e.preventDefault();
  showScreen('screen-cadastro-cliente');
});

/* RF1 - login simplificado de cliente (MVP não possui senha) */
document.getElementById('form-login-cliente').addEventListener('submit', (e) => {
  e.preventDefault();
  const email = document.getElementById('login-cliente-email').value.trim().toLowerCase();
  const err = document.getElementById('err-login-cliente');
  const cliente = db.clientes.find(c => c.email.toLowerCase() === email);
  if (!cliente) {
    err.textContent = 'E-mail não encontrado. Verifique ou cadastre-se abaixo.';
    return;
  }
  err.textContent = '';
  session = { role: 'cliente', userId: cliente.id };
  showToast(`Bem-vindo(a), ${cliente.nome}!`, 'success');
  resetStackTo('screen-home-cliente');
});

/* RF1 - Cadastro de Cliente (Nome, Sobrenome, Telefone, Email) */
document.getElementById('form-cadastro-cliente').addEventListener('submit', (e) => {
  e.preventDefault();
  const nome = document.getElementById('cc-nome').value.trim();
  const sobrenome = document.getElementById('cc-sobrenome').value.trim();
  const telefone = document.getElementById('cc-telefone').value.trim();
  const email = document.getElementById('cc-email').value.trim().toLowerCase();
  const err = document.getElementById('err-cadastro-cliente');

  const reqErr = validateRequired([[nome, 'Nome'], [sobrenome, 'Sobrenome'], [telefone, 'Telefone'], [email, 'E-mail']]);
  if (reqErr) { err.textContent = reqErr; return; }
  if (!EMAIL_RE.test(email)) { err.textContent = 'Informe um e-mail válido.'; return; }
  if (!PHONE_RE.test(telefone)) { err.textContent = 'Informe um telefone válido.'; return; }
  if (db.clientes.some(c => c.email.toLowerCase() === email)) {
    err.textContent = 'Este e-mail já está cadastrado. Faça login.';
    return;
  }

  const cliente = { id: uid('c'), nome, sobrenome, telefone, email };
  db.clientes.push(cliente);
  saveDB();
  err.textContent = '';
  e.target.reset();

  session = { role: 'cliente', userId: cliente.id };
  showToast('Cadastro realizado com sucesso!', 'success');
  resetStackTo('screen-home-cliente');
});

/* RF2 (acesso) - login simplificado de funcionário */
document.getElementById('form-login-funcionario').addEventListener('submit', (e) => {
  e.preventDefault();
  const email = document.getElementById('login-funcionario-email').value.trim().toLowerCase();
  const err = document.getElementById('err-login-funcionario');
  const funcionario = db.funcionarios.find(f => f.email.toLowerCase() === email);
  if (!funcionario) {
    err.textContent = 'E-mail não encontrado. Funcionários são cadastrados por outro funcionário.';
    return;
  }
  err.textContent = '';
  session = { role: 'funcionario', userId: funcionario.id };
  showToast(`Bem-vindo(a), ${funcionario.nome}!`, 'success');
  resetStackTo('screen-home-funcionario');
});

function currentCliente() { return db.clientes.find(c => c.id === session.userId); }
function currentFuncionario() { return db.funcionarios.find(f => f.id === session.userId); }

function renderHomeCliente() {
  const c = currentCliente();
  document.getElementById('cliente-nome-home').textContent = c ? `${c.nome} ${c.sobrenome}` : '';
}
function renderHomeFuncionario() {
  const f = currentFuncionario();
  document.getElementById('funcionario-nome-home').textContent = f ? `${f.nome} ${f.sobrenome}` : '';
}

document.getElementById('btn-logout-cliente').addEventListener('click', () => doLogout());
document.getElementById('btn-logout-funcionario').addEventListener('click', () => doLogout());
function doLogout() {
  session = { role: null, userId: null };
  showToast('Você saiu da sua conta.');
  resetStackTo('screen-welcome');
}

/* ---------- RNF1: menu da home leva às abas de cada requisito ---------- */
document.getElementById('card-meus-pets').addEventListener('click', () => showScreen('screen-pets'));
document.getElementById('card-agendar').addEventListener('click', () => iniciarAgendamento());
document.getElementById('card-meus-agendamentos').addEventListener('click', () => showScreen('screen-meus-agendamentos'));
document.getElementById('card-config-cliente').addEventListener('click', () => showScreen('screen-config'));

document.getElementById('card-cadastrar-servico').addEventListener('click', () => showScreen('screen-servico-form'));
document.getElementById('card-agenda-dia').addEventListener('click', () => iniciarAgendaDia());
document.getElementById('card-clientes').addEventListener('click', () => showScreen('screen-clientes'));
document.getElementById('card-cadastrar-funcionario').addEventListener('click', () => showScreen('screen-cadastro-funcionario'));
document.getElementById('card-config-funcionario').addEventListener('click', () => showScreen('screen-config'));

/* =========================================================
   RF3 - PETS (cadastro/edição)
   ========================================================= */

function meusPets() { return db.pets.filter(p => p.clienteId === session.userId); }

function animalLabel(a) { return a === 'cachorro' ? '🐶 Cachorro' : '🐱 Gato'; }

function renderPets() {
  const list = document.getElementById('lista-pets');
  const pets = meusPets();
  if (pets.length === 0) {
    list.innerHTML = `<div class="empty-state"><span class="empty-icon">🐾</span><p>Você ainda não cadastrou nenhum pet.</p></div>`;
    return;
  }
  list.innerHTML = pets.map(p => `
    <div class="card-item" data-pet-id="${p.id}">
      <div class="card-title-row"><span>${escapeHTML(p.nome)}</span><span class="badge">${animalLabel(p.animal)}</span></div>
      <div class="card-sub">${escapeHTML(p.raca)} · ${escapeHTML(p.cor)}</div>
      ${p.info ? `<div class="card-sub">${escapeHTML(p.info)}</div>` : ''}
    </div>
  `).join('');
  list.querySelectorAll('.card-item').forEach(el => {
    el.addEventListener('click', () => openPetForm(el.dataset.petId));
  });
}

document.getElementById('btn-add-pet').addEventListener('click', () => openPetForm(null));

function openPetForm(petId) {
  const form = document.getElementById('form-pet');
  form.reset();
  document.getElementById('err-pet-form').textContent = '';
  document.getElementById('pet-id').value = petId || '';
  document.getElementById('pet-form-title').textContent = petId ? 'Editar Pet' : 'Cadastrar Pet';

  if (petId) {
    const pet = db.pets.find(p => p.id === petId);
    document.getElementById('pet-nome').value = pet.nome;
    document.getElementById('pet-animal').value = pet.animal;
    document.getElementById('pet-raca').value = pet.raca;
    document.getElementById('pet-cor').value = pet.cor;
    document.getElementById('pet-info').value = pet.info || '';
  }
  showScreen('screen-pet-form');
}

document.getElementById('btn-cancel-pet').addEventListener('click', () => goBack());

document.getElementById('form-pet').addEventListener('submit', (e) => {
  e.preventDefault();
  const id = document.getElementById('pet-id').value;
  const nome = document.getElementById('pet-nome').value.trim();
  const animal = document.getElementById('pet-animal').value;
  const raca = document.getElementById('pet-raca').value.trim();
  const cor = document.getElementById('pet-cor').value.trim();
  const info = document.getElementById('pet-info').value.trim();
  const err = document.getElementById('err-pet-form');

  const reqErr = validateRequired([[nome, 'Nome'], [animal, 'Animal'], [raca, 'Raça'], [cor, 'Cor']]);
  if (reqErr) { err.textContent = reqErr; return; }

  if (id) {
    const pet = db.pets.find(p => p.id === id);
    Object.assign(pet, { nome, animal, raca, cor, info });
    showToast('Pet atualizado com sucesso!', 'success');
  } else {
    db.pets.push({ id: uid('p'), clienteId: session.userId, nome, animal, raca, cor, info });
    showToast('Pet cadastrado com sucesso!', 'success');
  }
  saveDB();
  err.textContent = '';
  goBack();
  renderPets();
});

/* =========================================================
   RF4 - AGENDAR SERVIÇO (wizard em 5 passos)
   ========================================================= */

let wizard = { step: 1, petId: null, servicoId: null, data: null, horario: null };

function iniciarAgendamento() {
  if (meusPets().length === 0) {
    showToast('Cadastre um pet antes de agendar um serviço.', 'error');
    showScreen('screen-pets');
    return;
  }
  wizard = { step: 1, petId: null, servicoId: null, data: null, horario: null };
  document.getElementById('select-horario').innerHTML = '<option value="">Selecione a data primeiro</option>';
  document.getElementById('data-selecionada-label').textContent = '';
  renderWizardStep();
  renderListaPetsAgendar();
  renderListaServicosAgendar();
  showScreen('screen-agendar');
}

function renderListaPetsAgendar() {
  const list = document.getElementById('lista-pets-agendar');
  list.innerHTML = meusPets().map(p => `
    <div class="card-item ${wizard.petId === p.id ? 'selected' : ''}" data-pet-id="${p.id}">
      <div class="card-title-row"><span>${escapeHTML(p.nome)}</span><span class="badge">${animalLabel(p.animal)}</span></div>
      <div class="card-sub">${escapeHTML(p.raca)} · ${escapeHTML(p.cor)}</div>
    </div>
  `).join('');
  list.querySelectorAll('.card-item').forEach(el => {
    el.addEventListener('click', () => {
      wizard.petId = el.dataset.petId;
      renderListaPetsAgendar();
    });
  });
}

function renderListaServicosAgendar() {
  const list = document.getElementById('lista-servicos-agendar');
  list.innerHTML = db.servicos.map(s => `
    <div class="card-item ${wizard.servicoId === s.id ? 'selected' : ''}" data-servico-id="${s.id}">
      <div class="card-title-row"><span>${escapeHTML(s.nome)}</span><span class="badge">R$ ${s.custo.toFixed(2)}</span></div>
    </div>
  `).join('');
  list.querySelectorAll('.card-item').forEach(el => {
    el.addEventListener('click', () => {
      wizard.servicoId = el.dataset.servicoId;
      renderListaServicosAgendar();
    });
  });
}

function renderWizardStep() {
  document.querySelectorAll('#agendar-stepper .step').forEach(el => {
    const n = Number(el.dataset.step);
    el.classList.toggle('active', n === wizard.step);
    el.classList.toggle('done', n < wizard.step);
  });
  document.querySelectorAll('.wizard-pane').forEach(el => el.classList.remove('active'));
  document.getElementById('pane-step-' + wizard.step).classList.add('active');

  const backBtn = document.getElementById('btn-wizard-voltar');
  const nextBtn = document.getElementById('btn-wizard-avancar');
  backBtn.textContent = wizard.step === 1 ? 'Cancelar' : 'Voltar';
  nextBtn.textContent = wizard.step === 5 ? 'Ir para Pagamento' : 'Avançar';

  if (wizard.step === 5) renderResumoAgendamento();
}

document.getElementById('btn-wizard-voltar').addEventListener('click', () => {
  if (wizard.step === 1) { goBack(); return; }
  wizard.step -= 1;
  renderWizardStep();
});

document.getElementById('btn-wizard-avancar').addEventListener('click', () => {
  const stepErrors = {
    1: () => wizard.petId ? null : 'Selecione um pet para continuar.',
    2: () => wizard.servicoId ? null : 'Selecione um serviço para continuar.',
    3: () => wizard.data ? null : 'Selecione uma data para continuar.',
    4: () => wizard.horario ? null : 'Selecione um horário para continuar.'
  };
  if (stepErrors[wizard.step]) {
    const msg = stepErrors[wizard.step]();
    if (msg) { showToast(msg, 'error'); return; }
  }

  if (wizard.step === 5) {
    irParaPagamento();
    return;
  }
  wizard.step += 1;
  renderWizardStep();
});

/* Calendário de seleção de data (RF4) */
document.getElementById('btn-abrir-calendario').addEventListener('click', () => {
  openCalendarModal({
    isDisabled: (dateStr) => isPastDate(dateStr) || getAvailableSlots(dateStr).length === 0,
    onSelect: (dateStr) => {
      wizard.data = dateStr;
      wizard.horario = null;
      document.getElementById('data-selecionada-label').textContent = `Data selecionada: ${formatDateBR(dateStr)}`;
      renderHorarioOptions();
    }
  });
});

function renderHorarioOptions() {
  const select = document.getElementById('select-horario');
  const slots = wizard.data ? getAvailableSlots(wizard.data) : [];
  if (!wizard.data) {
    select.innerHTML = '<option value="">Selecione a data primeiro</option>';
    return;
  }
  if (slots.length === 0) {
    select.innerHTML = '<option value="">Nenhum horário disponível neste dia</option>';
    return;
  }
  select.innerHTML = '<option value="">Selecione...</option>' + slots.map(h => `<option value="${h}">${h}</option>`).join('');
}

document.getElementById('select-horario').addEventListener('change', (e) => {
  wizard.horario = e.target.value || null;
});

function renderResumoAgendamento() {
  const pet = db.pets.find(p => p.id === wizard.petId);
  const servico = db.servicos.find(s => s.id === wizard.servicoId);
  document.getElementById('resumo-agendamento').innerHTML = `
    <div class="summary-row"><span>Pet</span><span>${escapeHTML(pet.nome)}</span></div>
    <div class="summary-row"><span>Serviço</span><span>${escapeHTML(servico.nome)}</span></div>
    <div class="summary-row"><span>Data</span><span>${formatDateBR(wizard.data)}</span></div>
    <div class="summary-row"><span>Horário</span><span>${wizard.horario}</span></div>
    <div class="summary-row"><span>Custo</span><span>R$ ${servico.custo.toFixed(2)}</span></div>
  `;
}

/* RF4 - após confirmar, direciona para aba de pagamento (não funcional) */
function irParaPagamento() {
  const pet = db.pets.find(p => p.id === wizard.petId);
  const servico = db.servicos.find(s => s.id === wizard.servicoId);
  document.getElementById('resumo-pagamento').innerHTML = `
    <div class="summary-row"><span>Pet</span><span>${escapeHTML(pet.nome)}</span></div>
    <div class="summary-row"><span>Serviço</span><span>${escapeHTML(servico.nome)}</span></div>
    <div class="summary-row"><span>Data</span><span>${formatDateBR(wizard.data)}</span></div>
    <div class="summary-row"><span>Horário</span><span>${wizard.horario}</span></div>
    <div class="summary-row"><span>Total</span><span>R$ ${servico.custo.toFixed(2)}</span></div>
  `;
  showScreen('screen-pagamento');
}

/* Pagamento ilustrativo: simula espera (H1/R03) e confirma o agendamento */
document.getElementById('btn-confirmar-pagamento').addEventListener('click', () => {
  showLoading('Confirmando pagamento...');
  setTimeout(() => {
    const agendamento = {
      id: uid('a'),
      clienteId: session.userId,
      petId: wizard.petId,
      servicoId: wizard.servicoId,
      data: wizard.data,
      horario: wizard.horario,
      estado: 'Agendado',
      dataPagamento: new Date().toISOString()
    };
    db.agendamentos.push(agendamento);
    saveDB();
    hideLoading();
    showToast('Agendamento confirmado com sucesso!', 'success');
    resetStackTo('screen-home-cliente');
  }, 900);
});

/* =========================================================
   RF5 - MEUS AGENDAMENTOS
   ========================================================= */

const ESTADOS_ATIVOS = ['Agendado', 'Em andamento'];

function renderMeusAgendamentos() {
  const list = document.getElementById('lista-meus-agendamentos');
  const agendamentos = db.agendamentos
    .filter(a => a.clienteId === session.userId && ESTADOS_ATIVOS.includes(a.estado))
    .sort((a, b) => (a.data + a.horario).localeCompare(b.data + b.horario));

  if (agendamentos.length === 0) {
    list.innerHTML = `<div class="empty-state"><span class="empty-icon">🧾</span><p>Nenhum agendamento ativo no momento.</p></div>`;
    return;
  }

  list.innerHTML = agendamentos.map(a => {
    const pet = db.pets.find(p => p.id === a.petId);
    const servico = db.servicos.find(s => s.id === a.servicoId);
    return `
      <div class="card-item" data-agendamento-id="${a.id}">
        <div class="card-title-row"><span>${escapeHTML(servico.nome)}</span>${badgeEstado(a.estado)}</div>
        <div class="card-sub">Pet: ${escapeHTML(pet.nome)}</div>
        <div class="card-sub">${formatDateBR(a.data)} às ${a.horario} · R$ ${servico.custo.toFixed(2)}</div>
        <div class="card-actions">
          ${a.estado === 'Agendado' ? `<button class="btn btn-danger btn-cancelar-agendamento" data-id="${a.id}">Cancelar</button>` : ''}
        </div>
      </div>
    `;
  }).join('');

  list.querySelectorAll('.btn-cancelar-agendamento').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const id = btn.dataset.id;
      askConfirm('Deseja realmente cancelar este agendamento?', () => {
        const a = db.agendamentos.find(x => x.id === id);
        a.estado = 'Cancelado';
        saveDB();
        showToast('Agendamento cancelado.', 'success');
        renderMeusAgendamentos();
      });
    });
  });
}

function badgeEstado(estado) {
  const map = {
    'Agendado': 'badge-agendado',
    'Em andamento': 'badge-andamento',
    'Cancelado': 'badge-cancelado',
    'Concluído': 'badge-concluido'
  };
  return `<span class="badge ${map[estado] || ''}">${estado}</span>`;
}

/* =========================================================
   RF6 - FUNCIONÁRIO CADASTRA SERVIÇO
   ========================================================= */

function renderServicosCadastrados() {
  const list = document.getElementById('lista-servicos-cadastrados');
  list.innerHTML = db.servicos.map(s => `
    <div class="card-item">
      <div class="card-title-row"><span>${escapeHTML(s.nome)}</span><span class="badge">R$ ${s.custo.toFixed(2)}</span></div>
    </div>
  `).join('');
}

document.getElementById('form-servico').addEventListener('submit', (e) => {
  e.preventDefault();
  const nome = document.getElementById('servico-nome').value.trim();
  const custoStr = document.getElementById('servico-custo').value;
  const err = document.getElementById('err-servico-form');

  const reqErr = validateRequired([[nome, 'Nome do Serviço'], [custoStr, 'Custo']]);
  if (reqErr) { err.textContent = reqErr; return; }
  const custo = Number(custoStr);
  if (isNaN(custo) || custo < 0) { err.textContent = 'Informe um custo válido.'; return; }

  db.servicos.push({ id: uid('s'), nome, custo });
  saveDB();
  err.textContent = '';
  e.target.reset();
  showToast('Serviço cadastrado com sucesso!', 'success');
  renderServicosCadastrados();
});

/* =========================================================
   RF2 - FUNCIONÁRIO CADASTRA FUNCIONÁRIO
   ========================================================= */

document.getElementById('form-cadastro-funcionario').addEventListener('submit', (e) => {
  e.preventDefault();
  const nome = document.getElementById('cf-nome').value.trim();
  const sobrenome = document.getElementById('cf-sobrenome').value.trim();
  const telefone = document.getElementById('cf-telefone').value.trim();
  const email = document.getElementById('cf-email').value.trim().toLowerCase();
  const err = document.getElementById('err-cadastro-funcionario');

  const reqErr = validateRequired([[nome, 'Nome'], [sobrenome, 'Sobrenome'], [telefone, 'Telefone'], [email, 'E-mail']]);
  if (reqErr) { err.textContent = reqErr; return; }
  if (!EMAIL_RE.test(email)) { err.textContent = 'Informe um e-mail válido.'; return; }
  if (!PHONE_RE.test(telefone)) { err.textContent = 'Informe um telefone válido.'; return; }
  if (db.funcionarios.some(f => f.email.toLowerCase() === email)) {
    err.textContent = 'Este e-mail já está cadastrado.';
    return;
  }

  db.funcionarios.push({ id: uid('f'), nome, sobrenome, telefone, email });
  saveDB();
  err.textContent = '';
  e.target.reset();
  showToast('Funcionário cadastrado com sucesso!', 'success');
  goBack();
});

/* =========================================================
   RF7 - AGENDA DO DIA (funcionário)
   ========================================================= */

let agendaDiaSelecionada = null;

function iniciarAgendaDia() {
  agendaDiaSelecionada = null;
  document.getElementById('dia-agenda-label').textContent = '';
  document.getElementById('lista-agenda-dia').innerHTML = `<div class="empty-state"><span class="empty-icon">📅</span><p>Selecione um dia para ver os agendamentos.</p></div>`;
  showScreen('screen-agenda-dia');
}

document.getElementById('btn-abrir-calendario-agenda').addEventListener('click', () => {
  openCalendarModal({
    isDisabled: () => false,
    onSelect: (dateStr) => {
      agendaDiaSelecionada = dateStr;
      document.getElementById('dia-agenda-label').textContent = `Dia selecionado: ${formatDateBR(dateStr)}`;
      renderAgendaDia();
    }
  });
});

function renderAgendaDia() {
  const list = document.getElementById('lista-agenda-dia');
  const agendamentos = db.agendamentos
    .filter(a => a.data === agendaDiaSelecionada && a.estado !== 'Cancelado')
    .sort((a, b) => a.horario.localeCompare(b.horario));

  if (agendamentos.length === 0) {
    list.innerHTML = `<div class="empty-state"><span class="empty-icon">📭</span><p>Nenhum serviço agendado para este dia.</p></div>`;
    return;
  }

  list.innerHTML = agendamentos.map(a => {
    const cliente = db.clientes.find(c => c.id === a.clienteId);
    const servico = db.servicos.find(s => s.id === a.servicoId);
    return `
      <div class="card-item" data-agendamento-id="${a.id}">
        <div class="card-title-row"><span>${a.horario}</span>${badgeEstado(a.estado)}</div>
        <div class="card-sub">Cliente: ${escapeHTML(cliente.nome)} ${escapeHTML(cliente.sobrenome)}</div>
        <div class="card-sub">Serviço: ${escapeHTML(servico.nome)}</div>
      </div>
    `;
  }).join('');

  list.querySelectorAll('.card-item').forEach(el => {
    el.addEventListener('click', () => abrirDetalheAgendamento(el.dataset.agendamentoId));
  });
}

function abrirDetalheAgendamento(agendamentoId) {
  const a = db.agendamentos.find(x => x.id === agendamentoId);
  const cliente = db.clientes.find(c => c.id === a.clienteId);
  const pet = db.pets.find(p => p.id === a.petId);
  const servico = db.servicos.find(s => s.id === a.servicoId);

  document.getElementById('detalhe-agendamento-conteudo').innerHTML = `
    <div class="summary-row"><span>Cliente</span><span>${escapeHTML(cliente.nome)} ${escapeHTML(cliente.sobrenome)}</span></div>
    <div class="summary-row"><span>Telefone</span><span>${escapeHTML(cliente.telefone)}</span></div>
    <div class="summary-row"><span>E-mail</span><span>${escapeHTML(cliente.email)}</span></div>
    <div class="summary-row"><span>Pet</span><span>${escapeHTML(pet.nome)} (${animalLabel(pet.animal)})</span></div>
    <div class="summary-row"><span>Raça / Cor</span><span>${escapeHTML(pet.raca)} / ${escapeHTML(pet.cor)}</span></div>
    ${pet.info ? `<div class="summary-row"><span>Observações</span><span>${escapeHTML(pet.info)}</span></div>` : ''}
    <div class="summary-row"><span>Serviço</span><span>${escapeHTML(servico.nome)}</span></div>
    <div class="summary-row"><span>Custo</span><span>R$ ${servico.custo.toFixed(2)}</span></div>
    <div class="summary-row"><span>Data</span><span>${formatDateBR(a.data)}</span></div>
    <div class="summary-row"><span>Horário</span><span>${a.horario}</span></div>
    <div class="summary-row"><span>Estado</span><span>${a.estado}</span></div>
  `;
  showScreen('screen-detalhe-agendamento');
}

/* =========================================================
   RF8 - CONSULTAR CLIENTES
   ========================================================= */

function renderClientes() {
  const termo = document.getElementById('busca-clientes').value.trim().toLowerCase();
  const somenteComPet = document.getElementById('filtro-com-pet').checked;
  const list = document.getElementById('lista-clientes');

  let clientes = db.clientes.filter(c => `${c.nome} ${c.sobrenome}`.toLowerCase().includes(termo));
  if (somenteComPet) {
    clientes = clientes.filter(c => db.pets.some(p => p.clienteId === c.id));
  }

  if (clientes.length === 0) {
    list.innerHTML = `<div class="empty-state"><span class="empty-icon">🔍</span><p>Nenhum cliente encontrado.</p></div>`;
    return;
  }

  list.innerHTML = clientes.map(c => {
    const petsDoCliente = db.pets.filter(p => p.clienteId === c.id);
    return `
      <div class="card-item">
        <div class="card-title-row"><span>${escapeHTML(c.nome)} ${escapeHTML(c.sobrenome)}</span></div>
        <div class="card-sub">${escapeHTML(c.telefone)} · ${escapeHTML(c.email)}</div>
        <div class="card-meta">${petsDoCliente.length > 0
          ? petsDoCliente.map(p => `<span class="badge">${escapeHTML(p.nome)}</span>`).join('')
          : '<span class="badge">Sem pets cadastrados</span>'}</div>
      </div>
    `;
  }).join('');
}

document.getElementById('busca-clientes').addEventListener('input', renderClientes);
document.getElementById('filtro-com-pet').addEventListener('change', renderClientes);

/* =========================================================
   Disponibilidade de horários / calendário
   ========================================================= */

function todayStr() {
  const d = new Date();
  return `${d.getFullYear()}-${pad2(d.getMonth() + 1)}-${pad2(d.getDate())}`;
}
function pad2(n) { return String(n).padStart(2, '0'); }

function isPastDate(dateStr) {
  return dateStr < todayStr();
}

function getAvailableSlots(dateStr) {
  const ocupados = new Set(
    db.agendamentos
      .filter(a => a.data === dateStr && a.estado !== 'Cancelado')
      .map(a => a.horario)
  );
  return SLOT_TIMES.filter(h => !ocupados.has(h));
}

function formatDateBR(dateStr) {
  if (!dateStr) return '';
  const [y, m, d] = dateStr.split('-');
  return `${d}/${m}/${y}`;
}

/* ---------- Modal de calendário reutilizável ---------- */
let calState = { year: 0, month: 0, isDisabled: null, onSelect: null };

function openCalendarModal({ isDisabled, onSelect }) {
  const today = new Date();
  calState = { year: today.getFullYear(), month: today.getMonth(), isDisabled, onSelect };
  renderCalendar();
  document.getElementById('modal-calendario').classList.add('active');
}

function closeCalendarModal() {
  document.getElementById('modal-calendario').classList.remove('active');
}

document.getElementById('btn-fechar-calendario').addEventListener('click', closeCalendarModal);
document.getElementById('cal-prev').addEventListener('click', () => {
  calState.month -= 1;
  if (calState.month < 0) { calState.month = 11; calState.year -= 1; }
  renderCalendar();
});
document.getElementById('cal-next').addEventListener('click', () => {
  calState.month += 1;
  if (calState.month > 11) { calState.month = 0; calState.year += 1; }
  renderCalendar();
});

function renderCalendar() {
  const { year, month } = calState;
  document.getElementById('cal-month-label').textContent = `${MONTH_NAMES[month]} ${year}`;

  const firstDay = new Date(year, month, 1).getDay();
  const daysInMonth = new Date(year, month + 1, 0).getDate();
  const grid = document.getElementById('cal-grid');

  let html = '';
  for (let i = 0; i < firstDay; i++) html += `<div class="cal-day empty"></div>`;

  for (let day = 1; day <= daysInMonth; day++) {
    const dateStr = `${year}-${pad2(month + 1)}-${pad2(day)}`;
    const disabled = calState.isDisabled(dateStr);
    html += `<div class="cal-day ${disabled ? 'disabled' : ''}" data-date="${dateStr}">${day}</div>`;
  }
  grid.innerHTML = html;

  grid.querySelectorAll('.cal-day:not(.disabled):not(.empty)').forEach(el => {
    el.addEventListener('click', () => {
      calState.onSelect(el.dataset.date);
      closeCalendarModal();
    });
  });
}

/* ---------- Util ---------- */
function escapeHTML(str) {
  if (str == null) return '';
  return String(str)
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');
}

/* ---------- Init ---------- */
resetStackTo('screen-welcome');
