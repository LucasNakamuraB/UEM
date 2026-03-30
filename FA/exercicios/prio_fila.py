from __future__ import annotations

class NodeP:

    priority : int
    item : int | str
    next : NodeP | None

    def __init__(self, prio, itm, next):
        self.priority = prio
        self.item = itm
        self.next = next


class FilaP:
    '''
    Uma coleção de strings em que o primeiro a ser removido é aquele com maior 
    prioridade

    Exemplo

    >>> f = FilaP()
    >>> f.vazia()
    True
    >>> f.enfileira('a', 1)
    >>> f.vazia()
    False
    >>> f.enfileira('b', 3)
    >>> f.enfileira('c', 2)
    >>> f.desenfileira()
    'b'
    >>> f.desenfileira()
    'c'
    >>> f.desenfileira()
    'a'
    '''
    
    inicio: NodeP | None
    fim: NodeP | None

    def __init__(self):
        self.inicio = None
        self.fim = None

    def enfileira(self, item, priorid) -> None:
        '''
        Adiciona *item* ao fim da fila
        '''
        if self.vazia():
            self.inicio = NodeP(priorid, item, None)
            self.fim = self.inicio

        else:
            
            aux = NodeP(0,0,self.inicio)
            while aux is not self.fim:
                ant = aux
                aux = aux.next
                if aux == self.fim:
                    if aux.priority < priorid:
                        ant.next = NodeP(priorid, item, aux)
                        if aux is self.inicio:
                            self.inicio = ant.next
                    else:
                        aux.next = NodeP(priorid, item, None)
                        self.fim = aux.next
                        aux = self.fim
                else:
                    if aux.priority < priorid:
                        ant.next = NodeP(priorid, item, aux) 
                        if aux is self.inicio:
                            self.inicio = ant.next
    
    def desenfileira(self) -> int|str:
        '''
        Devolve o item de maior prioridade da fila
        '''
        if self.vazia():
            raise ValueError('A fila está vazia')

        item = self.inicio.item
        if self.inicio is self.fim:
            self.inicio = None
            self.fim = None
        else:
            self.inicio = self.inicio.next
        return item
    
    def vazia(self) -> bool:
        if (self.inicio and self.fim) is None:
            return True
        else:
            return False
