from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    primeiro : int
    resto : No | None

Lista = No | None

def tem_impar(lst: Lista):
    '''
    verifica se a lista possui um item impar

    exemplos

    >>> tem_impar(None)
    False
    >>> tem_impar(No(2, None))
    False
    >>> tem_impar(No(2, No(4, None)))
    False
    >>> tem_impar(No(2, No(3, None)))
    True
    >>> tem_impar(No(3, No(2, None)))
    True
    '''
    if lst is None:
        return False
    else:
        return lst.primeiro % 2 == 1 or tem_impar(lst.resto)
    
def max_val(lst : Lista):
    '''
    Devolve o maior valor da lista

    Exemplos

    >>> max_val(None)
    >>> max_val(No(1, No(1, No(1, None))))
    1
    >>> max_val(No(5, No(2, No(4, None))))
    5
    >>> max_val(No(0, No(4, No(9, None))))
    9
    '''
    if lst is None:
        return None
    else:
        n = max_val(lst.resto)
        if n is None or lst.primeiro > n:
            return lst.primeiro
        else:
            return n

def rep_string(string : str, n : int):
    '''
    Devolve *string* repetida *n* vezes

    Exemplo

    >>> rep_string('ola', 0)
    ''
    >>> rep_string('a', 3)
    'aaa'
    >>> rep_string('casa', 4)
    'casacasacasacasa'
    '''
    if n == 0:
        return ''
    else:
        return string + rep_string(string, n-1)
    
def conta_n(lst: list[int]):
    '''
    Conta quantas repetições de *n* existem na lista

    Exemplos

    >>>
    '''


