# Casos de Uso — Plataforma de Truco Online

## Atores
- **Jogador** — usuário identificado por um apelido (nickname), sem necessidade de cadastro, que participa de partidas.
- **Sistema (Motor de Jogo)** — ator de apoio que valida regras e estados.

## UC01 — Acessar a Plataforma
**Ator:** Jogador
**Requisito relacionado:** RF01
**Fluxo principal:**
1. Jogador informa um apelido (nickname).
2. Sistema valida o apelido (disponibilidade na sessão/sala) e libera o acesso ao lobby.
**Exceção:** apelido já em uso na mesma sala → sistema solicita outro apelido.

## UC02 — Criar Sala de Jogo
**Ator:** Jogador
**Requisito relacionado:** RF02, RF10
**Pré-condição:** Jogador informou um apelido.
**Fluxo principal:**
1. Jogador seleciona "Criar Sala".
2. Define configurações (número de jogadores, variante de regras, pontuação, pública/privada).
3. Sistema cria a sala e gera código de convite (se privada).
4. Jogador aguarda demais participantes.

## UC03 — Entrar em Sala
**Ator:** Jogador
**Requisito relacionado:** RF03
**Fluxo principal:**
1. Jogador busca sala pública na lista ou informa código de convite.
2. Sistema verifica vagas disponíveis.
3. Jogador é adicionado à sala.
**Exceção:** sala cheia ou código inválido → sistema informa erro.

## UC04 — Jogar uma Partida
**Ator:** Jogador; **Ator de apoio:** Sistema (Motor de Jogo)
**Requisito relacionado:** RF04, RF05, RF06, RF07, RF09
**Pré-condição:** Sala completa, partida iniciada.
**Fluxo principal:**
1. Sistema distribui as cartas e define a manilha.
2. Sistema indica o jogador da vez (notificação).
3. Jogador escolhe uma carta e joga.
4. Sistema valida a jogada e atualiza o placar/estado da rodada para todos os clientes em tempo real.
5. Repete-se até o fim da rodada/mão; sistema calcula e registra os pontos da sessão.
6. Processo se repete até atingir a pontuação de vitória.
**Extensões:**
- 3a. Jogador pede "truco" (ou aumenta aposta) → oponentes aceitam, recusam ("correm") ou aumentam.
- 3b. Jogador pede "envido"/"flor" → disputa de pontos extras conforme regra.

## UC05 — Pedir Truco / Aumentar Aposta
**Ator:** Jogador
**Requisito relacionado:** RF04, RF09
**Pré-condição:** Partida em andamento, jogador apto a pedir.
**Fluxo principal:**
1. Jogador sinaliza "truco" (ou "seis", "nove", "doze").
2. Sistema notifica os demais jogadores/dupla adversária.
3. Adversário aceita, recusa ou aumenta a aposta.
4. Sistema atualiza o valor da mão conforme decisão.

## UC06 — Desistir da Mão ("Correr")
**Ator:** Jogador
**Requisito relacionado:** RF08
**Fluxo principal:**
1. Jogador seleciona "correr" durante a mão.
2. Sistema encerra a mão e atribui pontos ao adversário conforme a aposta vigente.
3. Sistema inicia a próxima mão.

