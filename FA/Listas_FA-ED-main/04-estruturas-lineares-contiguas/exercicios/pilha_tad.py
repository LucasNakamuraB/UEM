from fila_arranjo_circular import Fila

class Pilha:
    '''
    Uma coleção de strings que segue a política LIFO: o elemento mais
    recentemente inserido é o primeiro a ser removido.

    >>> p = Pilha(128)
    >>> p.vazia()
    True
    >>> p.empilha('O')
    >>> p.empilha('que')
    >>> p.empilha('escrever?')
    >>> p.vazia()
    False
    >>> p.desempilha()
    'escrever?'
    >>> p.empilha('fazer')
    >>> p.empilha('agora?')
    >>> i = 40
    >>> while not p.vazia():
    ...     p.desempilha()
    'agora?'
    'fazer'
    'que'
    'O'
    '''

    fila : Fila
    sec_fila : Fila


    def __init__(self,capacidade):

        self.fila = Fila(capacidade)
        self.sec_fila = Fila(capacidade)


    def empilha(self, item: str):
        '''
        Adiciona o *item* na pilha.
        '''
        self.fila.enfileira(item)

    def desempilha(self) -> str:
        '''
        Devolve o elemento mais recentemente adicionado da pilha.

        Requer que a pilha não esteja vazia.
        '''
        item = ''
        while not self.fila.vazia():
            item = self.fila.desenfileira()
            if not self.fila.vazia():
                self.sec_fila.enfileira(item)
        while not self.sec_fila.vazia():
            self.fila.enfileira(self.sec_fila.desenfileira())
        
        return item
        

    def vazia(self) -> bool:
        '''
        Devolve True se a pilha está vazia, False caso contrário.

        Exemplos
        >>> p = Pilha(128)
        >>> p.vazia()
        True
        >>> p.empilha('lar')
        >>> p.vazia()
        False
        '''
        return self.fila.vazia()