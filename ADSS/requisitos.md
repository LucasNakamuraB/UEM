# Requisitos — Plataforma de Truco Online

## Requisitos Funcionais

- **RF01** — O sistema deve permitir que o jogador acesse a plataforma informando apenas um apelido (nickname), sem necessidade de cadastro prévio.
- **RF02** — O sistema deve permitir a criação de salas de jogo (públicas ou privadas, com código de convite).
- **RF03** — O sistema deve permitir que um jogador entre em uma sala existente respeitando o limite de jogadores (2 ou 4, dupla).
- **RF04** — O sistema deve implementar as regras do Truco (Paulista ou Mineiro, configurável): distribuição de cartas, manilhas, rodadas, "truco/seis/nove/doze", "envido"/"flor" (variante), e contagem de pontos.
- **RF05** — O sistema deve validar jogadas de acordo com as regras vigentes, impedindo jogadas inválidas.
- **RF06** — O sistema deve exibir o placar da partida em tempo real.
- **RF07** — O sistema deve registrar o placar/resultado da partida em andamento para os jogadores da sessão atual.
- **RF08** — O sistema deve permitir que o jogador desista da partida ("correr") a qualquer momento, aplicando as regras de pontuação correspondentes.
- **RF09** — O sistema deve notificar os jogadores sobre eventos da partida (sua vez, truco pedido, fim de partida).
- **RF10** — O sistema deve permitir a configuração de regras da sala (com/sem flor, pontuação final, tempo por jogada).

## Requisitos Não Funcionais

- **RNF01** — O sistema deve estar disponível em dispositivos web
- **RNF02** — A interface deve ser minimalista e acessível
- **RNF03** — A interface responsíva quanto a diferentes proporções de monitor

## Restrições

- **R01** — As regras do jogo devem seguir estritamente uma variante oficial definida em configuração (ex.: Truco Paulista), sem ambiguidade de interpretação.
