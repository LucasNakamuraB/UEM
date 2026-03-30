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
        self.Lend = -1
        self.elements = 0
        self.capacity = capacity
    
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
        if self.full():
            raise ValueError('Queue is full')
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
        if self.full():
            raise ValueError('Queue is full')
        self.values[self.Lend] = item
        self.elements += 1
        self.Lend -= 1
        self.Lend = self.Lend % self.capacity

    def popR(self):
        '''
        Retorna o ultimo item da direita da fila

        Exemplo:

        >>> d = Deque(128)
        >>> d.addR('a')
        >>> d.addL('b')
        >>> d.addR('c')
        >>> d.popR()
        'c'
        '''
        item = self.values[self.Rend - 1]
        self.Rend -= 1
        return item
    
    def popL(self):
        '''
        Retorna o ultimo item da direita da fila

        Exemplo:

        >>> d = Deque(128)
        >>> d.addL('a')
        >>> d.addR('b')
        >>> d.addL('c')
        >>> d.popL()
        'c'
        '''
        item = self.values[self.Lend + 1]
        self.Lend -= 1
        return item

    def empty(self):
        '''
        Verifica se a fila está vazia

        Exemplos

        >>> d = Deque(128)
        >>> d.empty()
        True
        >>> d.addR('a')
        >>> d.empty()
        False
        '''
        return self.elements == 0
    
    def full(self):
        '''
        Verifica se a fila está cheia

        Exemplos

        >>> d = Deque(1)
        >>> d.full()
        False
        >>> d.addR('a')
        >>> d.full()
        True
        '''
        return self.elements == self.capacity


