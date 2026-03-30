from __future__ import annotations

class Node:
    '''
    Nó de um encadeamento
    '''
    key : int
    value  : int
    next : Node | None

    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next = None

class EHash:
    '''
    Tabela Hash com encadeamento

    Exemplo

    >>> a = EHash(16)
    >>> a.insert(8, 10)
    >>> a.insert(0, 20)
    >>> a.search(0)
    20
    >>> a.search(8)
    10
    >>> a.insert(24, 11)
    >>> a.search(8)
    10
    >>> a.search(24)
    11
    '''
    table : list[Node | None]
    size : int
    def __init__(self, size : int) -> None:
        self.size = size
        self.table = [None] * size
    
    def insert(self, k : int, n : int) -> None:
        '''
        Insere uma chave na tabela
        '''
        key = k % self.size
        if self.table[key] is None:
            self.table[key] = Node(k, n)
        else:
            inserted = False
            i = self.table[key].next    
            while not inserted:
                if i is None:
                    self.table[key].next = Node(k, n)
                    inserted = True
                else:
                    i = i.next
    
    def search(self, k : int) -> int | None: 
        '''
        busca um elemento com base na chave *key*
        '''
        item = self.table[k % self.size]
        if item is None:
            return None
        else:
            while item.next is not None and item.key != k:
                item = item.next
            return item.value



