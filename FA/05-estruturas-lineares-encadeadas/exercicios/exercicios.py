from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    item: int
    prox: No | None

p = No(7,None)
p.prox = No(1, None)
p.prox.prox = No(2, None)

def contra_encadeia_lista(lst : list):
    '''
    Produz um encadeamento dos itens de *lst* na ordem contraria

    Exemplo

    >>> a = [1,2,3]
    >>> contra_encadeia_lista(a)
    No(item=3, prox=No(item=2, prox=No(item=1, prox=None)))
    '''
    e = No(lst[0], None)
    for i in lst[1:]:
        e = No(i, e)
    return e

def num_itens(p : No | None):
    '''
    Determina quantos itens existem no encadeamento
    que começa com *p*.
    Exemplos
    >>> num_itens(None)
    0
    >>> num_itens(No(10, None))
    1
    >>> num_itens(No(20, No(10, None)))
    2
    >>> num_itens(No(4, No(20, No(10, None))))
    3
    '''
    i = p
    n = 1
    if p is None:
        return 0
    while not i.prox is None:
        n += 1
        i = i.prox
    return n

def soma_nodes(p : No| None):
    '''
    Retorna a soma dos valores de todos os nos do encadeamento

    Exemplos

    >>> soma_nodes(No(5, No(4, None)))
    9
    >>> soma_nodes(None)
    0
    '''
    i = p
    n = 0
    if p is None:
        return 0
    while not i.prox is None:
        n += i.item
        i = i.prox
    n += i.item
    i = i.prox
    return n



