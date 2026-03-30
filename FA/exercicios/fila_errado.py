from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    item: str
    prox: No | None

class Fila:
    '''
    Exemplos

    >>> f = Fila()
    >>> f.enfileira('a')
    >>> f.enfileira(None)
    >>> f.desenfileira()
    'a'
    >>> f.desenfileira()
    >>> f.vazia()
    True
    >>> f.enfileira('c')
    >>> f.vazia()
    False
    '''

    inicio: No | None
    fim: No | None
    def __init__(self) -> None:
        self.inicio = None
        self.fim = None

    def enfileira(self, item: str):
        if self.fim is None:
            self.inicio = No(item, None)
            self.fim = self.inicio
        else:
            self.fim.prox = No(item, None)
            self.fim = self.fim.prox

    def desenfileira(self) -> str:
        if self.inicio is None:
            raise ValueError('fila vazia')
        item = self.inicio.item
        self.inicio = self.inicio.prox
        if self.inicio is None:
            self.fim = None
        return item
    
    def vazia(self) -> bool:
        return self.inicio is None