from pilha_arranjo import Pilha

class Fila:
    '''
    Uma coleção de strings que segue a política FIFO: o primeiro a ser inserido
    é o primeiro a ser removido.

    Exemplos
    >>> f = Fila(128)
    >>> f.vazia()
    True
    >>> f.enfileira('Amanda')
    >>> f.enfileira('Fernando')
    >>> f.enfileira('Márcia')
    >>> f.vazia()
    False
    >>> f.desenfileira()
    'Amanda'
    >>> f.enfileira('Pedro')
    >>> f.enfileira('Alberto')
    >>> while not f.vazia():
    ...     f.desenfileira()
    'Fernando'
    'Márcia'
    'Pedro'
    'Alberto'
    '''
    pile : Pilha
    sec_pile : Pilha

    def __init__(self, capacidade):
        self.pile = Pilha(capacidade)
        self.sec_pile = Pilha(capacidade)

    def enfileira(self, item: str):
        '''
        Adiciona *item* no final da fila.
        '''
        self.pile.empilha(item)

    def desenfileira(self) -> str:
        '''
        Remove e devolve o primeiro elemento da fila.

        Requer que a fila não esteja vazia.
        '''
        while not self.pile.vazia():
            self.sec_pile.empilha(self.pile.desempilha())
        item = self.sec_pile.desempilha()
        while not self.sec_pile.vazia():
            self.pile.empilha(self.sec_pile.desempilha())
        return item



    def vazia(self) -> bool:
        '''
        Devolve True se a fila está vazia, False caso contrário.
        '''
        return self.pile.vazia()
