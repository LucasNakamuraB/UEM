# ATIVIDADE 03

## Parte I

### A. Integridade de dados
> O que significa integridade de dados  em um banco de dados

É a garantida de que os seus dados vão ser sempres consistentes e precisos dentro do seu banco ao serem acessados, é algo a ser ativamente mantido e protegido de coisas como erro humano, corrupção ou agentes mal intencionados.

### B. Integridade de Entidade

> Pesquise o que é integridade de entidade e responda:
- O que ela procura garantir?
- Qual é a relação entre integridade de entidade e chave primária (PK)?
- Uma chave primária pode possuir valores repetidos?
- Uma chave primária pode ser nula?
- O que poderia acontecer se essas regras não fossem respeitadas?

A integridade de entidade determina que, tal qual objetos do mundo real, os objetos representados numa tabela devem ser distinguíveis dos outros objetos ali presentes, mesmo que compartilhem alguns atributos. Para manter essa característica no nosso banco, referenciam-se atributos únicos de uma entidade para que ela possa ser distinguida das outras, o atributo selecionado é chamado de **Chave Primária**, que por não ter repetições na tabela pode ser usada para identificar objetos. A chave primária obviamente não pode ser nula, pois isso seria contraditório à sua função e definição. Caso a integridade de entidade não seja própriamente mantida, entidades podem ser acessadas e alteradas erroneamente, o que prejudicaria a integridade dos dados do projeto

### C