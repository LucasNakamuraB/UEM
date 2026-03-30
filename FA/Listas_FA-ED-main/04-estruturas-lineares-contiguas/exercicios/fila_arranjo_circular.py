from ed import array

class Fila:
    '''
    Uma coleção de strings que segue a política FIFO: o primeiro a ser inserido
    é o primeiro a ser removido.

    Exemplos
    >>> f = Fila(256)
    >>> f.vazia()
    True
    >>> f.enfileira('Amanda')
    >>> f.enfileira('Fernando')
    >>> f.enfileira('Márcia')
    >>> f.vazia()
    False
    >>> f.desenfileira()
    'Amanda'
    >>> f.enfileira('Pedro')
    >>> f.enfileira('Alberto')
    >>> while not f.vazia():
    ...     f.desenfileira()CAPACIDADE
    'Fernando'
    'Márcia'
    'Pedro'
    'Alberto'
    '''

    valores: array[str]
    # Indíce onde o próximo elemento será inserido
    fim: int
    # Indíce do primeiro elemento da fila
    inicio: int
    #Maximo de elementos da fila
    capacidade: int
    #Numero de elementos contidos na fila
    elementos: int

    # O valor para o inicio e o fim são incrementados até chegarem em
    # CAPACIDADE, quando voltam a ser 0.
    #
    # A fila está vazia se inicio == fim e está cheia se o próximo valor para
    # fim é igual ao inicio. Dessa forma, nunca podemos preencher todos os
    # elementos de *valores*, pois senão não seria possível distinguir entre fila
    # cheia e fila vazia. Para honrar o valor de CAPACIDADE, inicializamos
    # *valores* com CAPACIDADE + 1 itens.

    def __init__(self, capacidade) -> None:
        '''
        Cria uma nova fila com capacidade para armazenar *CAPACIDADE*
        elementos.
        '''
        self.capacidade = capacidade
        self.valores = array(capacidade, '')
        self.inicio = 0
        self.fim = 0
        self.elementos = 0

    def enfileira(self, item: str):
        '''
        Adiciona *item* no final da fila.

        Requer que a quantidade de elementos na fila seja menor que
        *CAPACIDADE*.

        Exemplos
        >>> f = Fila(256)
        >>> for i in range(f.capacidade):
        ...     f.enfileira(str(i))
        >>> f.enfileira('a')
        Traceback (most recent call last):
        ...
        ValueError: fila cheia
        >>> f.desenfileira()
        '0'
        >>> f.desenfileira()
        '1'
        '''
        if self.cheia():
            raise ValueError('fila cheia')
        self.valores[self.fim] = item
        self.elementos += 1
        if self.fim == len(self.valores) - 1:
            self.fim = 0
        else:
            self.fim += 1

    def desenfileira(self) -> str:
        '''
        Remove e devolve o primeiro elemento da fila.

        Requer que a fila não esteja vazia.

        Exemplos
        >>> f = Fila(256)
        >>> f.desenfileira()
        Traceback (most recent call last):
        ...
        ValueError: fila vazia
        >>> f.enfileira('Márcia')
        >>> f.enfileira('João')
        >>> f.enfileira('Pedro')
        >>> f.desenfileira()
        'Márcia'
        '''
        if self.vazia():
            raise ValueError('fila vazia')
        item = self.valores[self.inicio]
        self.elementos -= 1
        if self.inicio == len(self.valores) - 1:
            self.inicio = 0
        else:
            self.inicio += 1
        return item

    def vazia(self) -> bool:
        '''
        Devolve True se a fila está vazia, False caso contrário.

        Exemplos
        >>> f = Fila(256)
        >>> f.vazia()
        True
        >>> f.enfileira('Jorge')
        >>> f.vazia()
        False
        '''
        return self.elementos == 0

    def cheia(self) -> bool:
        '''
        Devolve True se a fila está cheia, isto é, a quantidade de elementos na
        fila é igual a *CAPACIDADE*, False caso contrário.
        '''
        # O próximo índice para o fim é igual ao início?
        return self.elementos == self.capacidade
    
    def _capacidade(self) -> int:
        '''
        devolve a capacidade da fila
        '''
        return self.capacidade
    
    def esvazia(self):
        self.elementos = 0
        self.inicio = 0
        self.fim = 0
