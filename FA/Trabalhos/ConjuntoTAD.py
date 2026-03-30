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
    
    
    def __init__(self) -> None:
        '''Cria um novo conjunto vazio.'''
        raise NotImplementedError()
    def inserir(self, tree : Arvore | None , valor: int) -> Arvore:

        '''
        retorn uma nova raiz da arvore com o elemento com *valor* inserido
        '''
        raise NotImplementedError()
    def string_arvore(self, tree : Arvore | None) -> str:
        '''
        produz uma string com os elementos de uma árvore
        '''
        raise NotImplementedError()
    def gera_lista(self, tree : Arvore | None) -> list[int]:
        '''
        gera uma lista com os itens de *arvore*
        '''
        raise NotImplementedError()
    def procura(self,t: Arvore | None, n: int) -> bool:
        '''
        Percorre o conjunto  procura do inteiro *n* a partir da arvore *t*, retorna True caso o encontre 
        e False no caso contrario
        '''
        raise NotImplementedError()

    def adiciona(self, n: int) -> None:
        '''Adiciona *n* ao conjunto.'''
        raise NotImplementedError()
    def str(self) -> str:
        '''Cria uma string com os elementos entre chaves e separados por vírgula.'''
        raise NotImplementedError()

    def uniao(self, outro: Conjunto) -> Conjunto:
        '''Realiza a união entre *self* e *outro*.'''
        raise NotImplementedError()
    
    def eh_uniao(self, c1: Conjunto, c2: Conjunto) -> bool:
        '''
        Verifica se o conjunto é uma união entre *c1* e *c2*
        '''
        raise NotImplementedError()