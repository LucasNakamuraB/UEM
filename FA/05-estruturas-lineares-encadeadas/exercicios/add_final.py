from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    item: int
    prox: No | None

def add_final(n : int, node : No | None):
    '''
    adiciona *n* na forma de nó ao final do encadeamento e devolve o inicio 

    Exemplos

    >>> p = No(5, No( 4, None))
    >>> add_final(3, p)
    No(item=5, prox=No(item=4, prox=No(item=3, prox=None)))
    >>> p = None
    >>> add_final(1, p)
    No(item=1, prox=None)
    '''
    p = node
    if node is None:
        p = No(n, None)
        return p
    else:
        while p.prox is not None:
            p = p.prox
        p.prox = No(n, None)

        return node
