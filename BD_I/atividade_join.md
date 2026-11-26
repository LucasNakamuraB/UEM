## Parte 14 — Exercícios práticos

Utilize `categoria` e `produto` criadas no início.

### Nível 1 — INNER JOIN

1. Apresente o nome de cada produto e sua categoria.

| produto  | categoria   |
| -------- | ----------- |
| Notebook | Informática |
| Mouse    | Informática |
| Mesa     | Móveis      |
| Cadeira  | Móveis      |
| Caneta   | Papelaria   |
2. Apresente nome, preço e categoria, em ordem decrescente de preço.

| produto  | preco   | categoria   |
| -------- | ------- | ----------- |
| Notebook | 3500.00 | Informática |
| Mesa     | 900.00  | Móveis      |
| Cadeira  | 600.00  | Móveis      |
| Mouse    | 80.00   | Informática |
| Caneta   | 5.00    | Papelaria   |
3. Consulte somente os produtos de Informática.

| produto  | preco   | categoria   |
| -------- | ------- | ----------- |
| Notebook | 3500.00 | Informática |
| Mouse    | 80.00   | Informática |
4. Apresente produtos com preço superior a R$ 500 e suas categorias.

| produto  | preco   | categoria   |
| -------- | ------- | ----------- |
| Notebook | 3500.00 | Informática |
| Mesa     | 900.00  | Móveis      |
| Cadeira  | 600.00  | Móveis      |
5. Apresente produtos de Informática ou Móveis, em ordem alfabética.

| produto  | preco   | categoria   |
| -------- | ------- | ----------- |
| Notebook | 3500.00 | Informática |
| Mouse    | 80.00   | Informática |
| Mesa     | 900.00  | Móveis      |
| Cadeira  | 600.00  | Móveis      |


### Nível 2 — LEFT JOIN

6. Liste todas as categorias, incluindo as que não possuem produtos.

| id_categoria | nome        |
| ------------ | ----------- |
| 1            | Informática |
| 2            | Móveis      |
| 3            | Papelaria   |
| 4            | Limpeza     |
7. Identifique as categorias sem produtos.

| nome        | produto  |
| Limpeza     | null     |

8. Liste todas as categorias e associe somente produtos com preço superior a R$ 100, preservando categorias sem correspondências.

| nome        | produto  | preco   |
| ----------- | -------- | ------- |
| Móveis      | Cadeira  | 600.00  |
| Móveis      | Mesa     | 900.00  |
| Informática | Notebook | 3500.00 |
| Limpeza     | null     | null    |
| Papelaria   | null     | null    |

### Nível 3 — Comparações

9. Execute uma consulta com `INNER JOIN` e outra com `LEFT JOIN`; compare os resultados.
INNER JOIN mostra apenas os resultados com correspondências, já LEFT JOIN mostra as colunas da esquerda sem correspondência
10. Reescreva uma consulta com `LEFT JOIN` usando `RIGHT JOIN` e preserve o resultado.
Inverte-se a ordem do produto.nome e categoria.nome
11. Execute um `CROSS JOIN` e explique a quantidade de linhas.
CROSS JOIN mostra todas as combinações possíveis entre as tabelas, gerando um grando numero de linhas

### Nível 4 — Modelagem e consulta

12. Crie `cliente` e `pedido` em um relacionamento 1:N. Cadastre três clientes e quatro pedidos, deixando um cliente sem pedidos. Escreva consultas para:

    a. mostrar os pedidos com seus clientes;
    b. mostrar todos os clientes, inclusive os sem pedidos;
    c. mostrar apenas clientes sem pedidos;
    d. ordenar pedidos por data;
    e. mostrar os pedidos de um cliente específico.

---