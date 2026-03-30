from __future__ import annotations
from dataclasses import dataclass
from fila_dupla_encadeamento_duplo_sentinela import Deque


@dataclass
class No:
    item: int
    prox: No | None

@dataclass
class Node:
    before : Node
    item : int
    next : Node

def encad_lista(lst : list) -> No:
    '''
    transforma lista em encadeamento

    Exemplo

    >>> l =[1,2,3]
    >>> encad_lista(l)
    No(item=1, prox=No(item=2, prox=No(item=3, prox=None)))
    '''
    node = No(lst[0], None)
    p = node
    for i in range(1,len(lst)):
        p.prox = No(lst[i], None)
        p = p.prox

    return node

def dup_encad_lista(lst : list) -> Node:
    '''
    transforma lista em encadeamento

    Exemplo

    >>> l =[1,2,3]
    >>> dup_encad_lista(l)
    Node(before=None, item=1, next=Node(before=..., item=2,next=Node(before=..., item=3, next=None)))
    '''
    node = Node(None,lst[0], None)
    p = node
    for i in range(1,len(lst)):
        p.next = Node(p, lst[i], None)
        p = p.next

    return node




