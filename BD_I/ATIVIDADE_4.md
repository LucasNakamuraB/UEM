#### 1) Inserção simples
    o valor de nome foi inserido por mim, já os ids foram gerados pelo SQL

#### 2) Inserido Produtos
    O valor de id_produto for determinado automaticamente, começando no 1 e incrementando em um a cada inserção

#### 3) Inserção Multipla
    Os valores foram inseridos corretamente como esperado

#### 4) Utilizando `DEFAULT` e `RETURNING` 
    1. Foi atribuido 0 ao estoque
    2. Por que ao criar a tabela foi usado o 'DEFAULT 0'
    3. O PostgreSQL
    4. Para retornar a linha adicionada

#### 5) Tentando violar as regras do banco

|Tentativa|Inserção aceita?|Restrição envolvida|Explique o motivo|
|----|----|----|----|
|Produto sem nome|Não|NOT NULL|A restrição não permite que o campo seja nulo|
|Estoque negativo|Não|CHECK (estoque >= 0)|A restrição não permite que o valor seja < 0|
|Categoria inexistente|Não|CONSTRAINT fk_produto_categoria| produto deve ter um fk válida|
|Categoria duplicada|Não|UNIQUE| A restrição não permite que haja repetições nesse campo|

