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
    Uma coleção de strings que segue a política FIFO: o primeiro a ser inserido
    é o primeiro a ser removido.
    '''
    
    inicio: NodeP | None
    fim: NodeP | None

    def __init__(self):
        self.inicio = None
        self.fim = None