from fila_arranjo_circular import Fila
from pilha_arranjo import Pilha

def inverte_fila(fila : Fila):
    '''
    Inverte a ordem dos elementos de *fila*

    Exemplos

    >>> f = Fila()
    >>> f.enfileira(1)
    >>> f.enfileira(2)
    >>> f.enfileira(3)
    >>> inverte_fila(f)
    >>> f.desenfileira()
    3
    >>> f.desenfileira()
    2
    >>> f.desenfileira()
    1
    '''
    inv = Pilha(256)
    while not fila.vazia():
        inv.empilha(fila.desenfileira())
    while not inv.vazia():
        fila.enfileira(inv.desempilha()) 