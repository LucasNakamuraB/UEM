
## Parte 14 — Exercícios

### Nível 1 — Funções básicas

1. Conte todos os produtos.
10
2. Conte as categorias distintas.
3
3. Calcule o total de unidades em estoque.
295
4. Calcule o valor financeiro total do estoque.
47040.00
5. Calcule o preço médio.
159.45
6. Encontre o menor e o maior preço.
maior= 3500.00, menor = 3.00
7. Mostre todos os produtos empatados no menor preço.
Borracha

### Nível 2 — GROUP BY

8. Conte os produtos por categoria.
| categoria   | count |
| ----------- | ----- |
| Móveis      | 3     |
| Papelaria   | 3     |
| Informática | 4     |
9. Calcule o estoque total por categoria.
| categoria   | sum |
| ----------- | --- |
| Móveis      | 17  |
| Papelaria   | 230 |
| Informática | 48  |
10. Calcule preço médio, mínimo e máximo por categoria.
| categoria   | minimo | maximo  | medio   |
| ----------- | ------ | ------- | ------- |
| Móveis      | 600.00 | 1500.00 | 1000.00 |
| Papelaria   | 3.00   | 25.00   | 11.00   |
| Informática | 80.00  | 3500.00 | 1232.50 |
11. Calcule o valor financeiro do estoque por categoria.
| categoria   | sum      |
| ----------- | -------- |
| Móveis      | 14100.00 |
| Papelaria   | 1990.00  |
| Informática | 30950.00 |
12. Liste alfabeticamente os produtos de cada categoria em uma string.
| categoria   | produtos                          |
| ----------- | --------------------------------- |
| Informática | Monitor, Mouse, Notebook, Teclado |
| Móveis      | Armário, Cadeira, Mesa            |
| Papelaria   | Borracha, Caderno, Caneta         |

### Nível 3 — WHERE, HAVING e FILTER

13. Conte por categoria somente produtos com preço acima de R$ 100.
| categoria   | count |
| ----------- | ----- |
| Móveis      | 3     |
| Informática | 3     |
14. Mostre categorias com pelo menos três produtos.
informática
15. Mostre categorias com preço médio acima de R$ 500.
| categoria   |
| ----------- |
| Móveis      |
| Informática |
16. Em uma linha, conte todos os produtos, os de preço acima de R$ 1000 e os com estoque abaixo de 10.
17. Mostre categorias cujo valor total de estoque supera R$ 10.000.
| categoria   |
| ----------- |
| Móveis      |
| Informática |

### Nível 4 — JOIN e agregação

18. Em um esquema normalizado, conte produtos por categoria incluindo categorias vazias.
19. Mostre somente categorias vazias.
20. Calcule quantidade, média e valor do estoque por categoria.
21. Explique por que `COUNT(*)` pode dar resultado incorreto em um `LEFT JOIN`.

### Desafio

22. Modele `cliente`, `pedido` e `item_pedido`. Produza:

    a. total de pedidos por cliente, incluindo clientes sem pedidos;
    b. valor total de cada pedido;
    c. total gasto por cliente;
    d. ticket médio por cliente;
    e. clientes com total gasto acima de R$ 1.000;
    f. produto mais vendido por quantidade, preservando empates.

