from ed import array

class Deque:
    '''
    Coleção de strings em que podem ser removidos, o primeiro ou o ultimo a ser
    adicionado

    Exemplo

    >>> d = Deque(128)
    >>> d.empty()
    True
    >>> d.addR('b')
    >>> d.empty()
    False
    >>> d.addR('c')
    >>> d.addL('a')
    >>> d.popR()
    'c'
    >>> d.popL()
    'a'
    '''

    
    values : array[str] # Valores contidos na fila

    Rend : int # Posição onde será adicionado o elemento da direita

    Lend : int # Posição onde será adicionado o elemento da esquerda

    elements : int # Numero de elementos contidos na fila

    capacity : int # Máximo de elementos que a fila pode conter

    def __init__(self, capacity):
        '''
        Cria uma fila quue pode conter no máximo *capacity* elementos
        '''
        self.values = array(capacity, '')
        self.Rend = 0
        self.Lend = 0
        self.elements = 0
    
    def addR(self, item):
        '''
        Adiciona *item* à direita da fila

        Exemplo:

        >>> d = Deque(128)
        >>> d.addR('a')
        >>> d.addL('b')
        >>> d.popR()
        'a'
        '''
        self.values[self.Rend] = item
        self.elements += 1
        self.Rend += 1
        self.Rend = self.Rend % self.capacity
    
    def addL(self, item):
        '''
        Adiciona *item* à esquerda da fila

        Exemplos

        >>> d = Deque(128)
        >>> d.addL('a')
        >>> d.addR('b')
        >>> d.popL()
        'a'
        '''
        self.values[self.Lend] = item
        self.elements += 1
        self.Lend -= 1
        self.Rend = self.Lend % self.capacity

