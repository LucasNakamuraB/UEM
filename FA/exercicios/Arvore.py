from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    esq : No | None
    chave : int
    dir : No | None

Arvore = No | None

def arvore_cheia(tree : Arvore) -> bool:
    '''
    verifica se *tree* possui apenas nos de grau 2 ou 0

    Exemplos

    >>> arvore_cheia(None)
    False
    >>> arvore_cheia(No(No(None, 2, None), 2, No(None, 2, None)))
    True
    >>> arvore_cheia(No(None, 2, None))
    True
    >>> arvore_cheia(No(No(None, 2, None), 2, No(None, 2, No(None, 2, None))))
    False
    '''
    if tree is None:
        return False
    return arvore_cheia(tree.esq) == arvore_cheia(tree.dir)

def max_arvore(tree : Arvore) -> int | None:
    '''
    Retorna o valor maximo da arvore *tree*, ou None, se estiver vazia

    Exemplo

    >>> max_arvore(None)
    None
    >>> max_arvore(No(No(None, 2, None), 7, No(None, 5, None)))
    7
    >>> max_arvore(No(No(None, 2, None), 2, No(None, 2, No(None, 6, None))))
    7
    '''
    
    if tree is None:
        return None
    maior = tree.chave
    dir = max_arvore(tree.dir)
    esq = max_arvore(tree.esq)
    if tree.esq is not None:
        if tree.esq.chave > maior:
            maior = tree.esq.chave
    if tree.dir is not None:
        if tree.dir.chave > maior:
            maior = tree.dir.chave

    return maior
    




