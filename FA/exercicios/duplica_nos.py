from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    item: int
    prox: No | None


def duplica_nos(p: No | None):
    '''
    Modifica o encadeamento que começa em *p* criando uma
    cópia de cada nó e colocando a cópia após o nó original
    no encadeamento.

    Exemplos
    >>> p = No(1, No(2, None))
    >>> duplica_nos(p)
    >>> p
    No(item=1, prox=No(item=1, prox=No(item=2, prox=No(item=2, prox=None))))
    >>> # A modificação do primeiro
    >>> # não pode alterar o segundo!
    >>> p.item = 20
    >>> p.prox.item
    1
    '''
    if p is None:
        raise ValueError('p is None')
    node = p
    while node is not None:
        i = No(node.item, node.prox)
        j = node.prox
        node.prox = i
        node = j
