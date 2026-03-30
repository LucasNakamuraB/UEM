from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    item: int
    prox: No | None

def max_encad(node : No | None):
    '''
    Encontra o maior valor do encadeamento

    Exemplos

    >>> p = No(5, No(4, No(7, None)))
    >>> max_encad(p)
    7
    >>> p = No(-4, No(0, No(-8, None)))
    >>> max_encad(p)
    0
    '''
    if node is None:
        raise ValueError('Nó nulo')

    max = node.item
    while node is not None:
        if node.item > max:
            max = node.item
        node = node.prox
    
    return max
