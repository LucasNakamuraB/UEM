from __future__ import annotations

class Arvore:
    '''
    Representa um nó em uma árvore binaria de busca
    '''
    item : int
    esq : Arvore | None
    dir : Arvore | None

    def __init__(self, item):
        self.item = item
        self.esq = None
        self.dir = None



class Conjunto:
    '''Um conjunto de números inteiros
    Exemplos
    >>> c1 = Conjunto()
    >>> c1.adiciona(2)
    >>> c1.adiciona(3)
    >>> c1.adiciona(4)
    >>> c1.str()
    '{2, 3, 4}'
    >>> c2 = Conjunto()
    >>> c2.adiciona(1)
    >>> c2.adiciona(2)
    >>> c2.adiciona(4)
    >>> c2.str()
    '{1, 2, 4}'
    >>> c3 = c1.uniao(c2)
    >>> c3.str()
    '{1, 2, 3, 4}'
    >>> c3.eh_uniao(c1, c2)
    True
    >>> c4 = Conjunto()
    >>> c4.adiciona(5)
    >>> c4.adiciona(8)
    >>> c3.eh_uniao(c1, c4)
    False
    >>> O = Conjunto()
    >>> c3.eh_uniao(c3, O)
    True
    
    Teste de comutatividade
    >>> c34 = c3.uniao(c4)
    >>> c43 = c4.uniao(c3)
    >>> c34.str() == c43.str()
    True

    '''
    
    abb : Arvore | None
    
    def __init__(self) -> None:
        '''Cria um novo conjunto vazio.'''
        self.abb = None
    def inserir(self, tree : Arvore | None , valor: int) -> Arvore:

        '''
        retorn uma nova raiz da arvore com o elemento com *valor* inserido
        '''
        new = Arvore(valor)
        if tree is None:
            return new
        elif valor == tree.item:
            return tree
        else:
            if valor > tree.item:
                tree.dir = self.inserir(tree.dir, valor)
            else:
                tree.esq = self.inserir(tree.esq, valor)
            return tree
    def string_arvore(self, tree : Arvore | None) -> str:
        '''
        produz uma string com os elementos de uma árvore
        '''
        if tree is None:
            return ', '
        else:
            return self.string_arvore(tree.esq) + str(tree.item)+ self.string_arvore(tree.dir)
    def gera_lista(self, tree : Arvore | None) -> list[int]:
        '''
        gera uma lista com os itens de *arvore*
        '''
        lista : list = []
        if tree is None:
            return []
        else:
            lista = lista + self.gera_lista(tree.esq)
            lista.append(tree.item)
            lista = lista + self.gera_lista(tree.dir)
            return lista
    def procura(self,t: Arvore | None, n: int) -> bool:
        '''
        Percorre o conjunto  procura do inteiro *n* a partir da arvore *t*, retorna True caso o encontre 
        e False no caso contrario
        '''
        if t is None:
            return False
        else:
            return n == t.item or self.procura(t.esq, n) or self.procura(t.dir, n)

    def adiciona(self, n: int) -> None:
        '''Adiciona *n* ao conjunto.'''
        if self.abb is None:
            self.abb = Arvore(n)
        else:
            self.abb = self.inserir(self.abb, n)
    def str(self) -> str:
        '''Cria uma string com os elementos entre chaves e separados por vírgula.'''
        string = self.string_arvore(self.abb)
        string = '{' + string[2:len(string)-2] + '}'
        return string

    def uniao(self, outro: Conjunto) -> Conjunto:
        '''Realiza a união entre *self* e *outro*.'''
        items : list[int] = outro.gera_lista(outro.abb)
        items = items + self.gera_lista(self.abb)
        union = Conjunto()
        for i in items:
             union.adiciona(i)
        return union
    
    def eh_uniao(self, c1: Conjunto, c2: Conjunto) -> bool:
        '''
        Verifica se o conjunto é uma união entre *c1* e *c2*
        '''
        euniao = True
        for i in c1.gera_lista(c1.abb):
            if not self.procura(self.abb, i):
                euniao = False
        for i in c2.gera_lista(c2.abb):
            if not self.procura(self.abb, i):
                euniao = False
        return euniao

