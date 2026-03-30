from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Tree:
    n : int
    left : None | Tree
    right : None | Tree

    def __init__(self,right, n, left):
        self.n = n
        self.left = R
        self.right = None

def add_tree(t : Tree | None, n):
    '''
    retorna a raiz da arvore que é resultado da adição de *n*
    '''
    if t is None:
        return Tree(None, t, None)
    elif n > t.n:
        t.right = add_tree(t.right, n)
    elif n < t.n:
        t.left = add_tree(t.left, n)
    return t

def maximo(t):
    '''
    encontra o maior elemento da arvore
    '''
    if t.esq is None:
        pass
    elif t.dir is None:
        pass
    ellif