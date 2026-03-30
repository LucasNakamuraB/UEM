class Selecao:
    '''
    Um intervalo de células selecionadas de uma linha de uma panilha.
    '''
    col_in : list
    col_end : list
    incell : list
    def __init__(self, col: int):
        '''
        Cria uma nova seleção de células que inclui apenas a célula da coluna *col*
        de uma linha qualquer.

        Requer que col >= 1.

        Exemplos
        >>> s = Selecao(10)
        >>> s.inicio()
        10
        >>> s.fim()
        10
        '''
        self.col_in = [None] *col
        self.col_end = [None] * col
        self.incell = [None] *col
        return

    def inicio(self) -> int:
        '''
        Devolve o início da seleção *self*.

        Exemplos
        >>> s = Selecao(4)
        >>> s.inicio()
        4
        >>> s.move_esquerda()
        >>> s.inicio()
        3
        '''
        return len(self.col_in)

    def fim(self) -> int:
        '''
        Devolve o fim da seleção *self*.

        Exemplos
        >>> s = Selecao(4)
        >>> s.fim()
        4
        >>> s.move_direita()
        >>> s.fim()
        5
        '''
        return len(self.col_end)

    def move_direita(self):
        '''
        Altera a selação *self* movendo o início ou fim da seleção para a
        direita da seguinte forma:
        - Se o fim de *self* está a direita da célula onde a seleção começou,
          ou a seleção só tem uma célula, então o fim é movido uma célula para
          a direita.
        - Se o início de *self* está a esquerda célula onde a seleção começou,
          então, o início é movido uma célula para a direta (até o mínimo de
          1).

        Exemplos
        >>> # Mudança do fim
        >>> s = Selecao(2)
        >>> s.move_direita()
        >>> s.inicio()
        2
        >>> s.fim()
        3
        >>> s.move_direita()
        >>> s.inicio()
        2
        >>> s.fim()
        4
        >>> # Mudança do início
        >>> s = Selecao(4)
        >>> s.move_esquerda()
        >>> s.move_esquerda()
        >>> s.move_esquerda()
        >>> s.inicio()
        1
        >>> s.fim()
        4
        >>> s.move_direita()
        >>> s.inicio()
        2
        >>> s.fim()
        4
        '''
        if len(self.col_in) < len(self.incell):
            self.col_in.append(None)
        elif len(self.col_end) > len(self.incell) or len(self.incell) == len(self.col_end) == len(self.col_in):
            self.col_end.append(None)
        return

    def move_esquerda(self):
        '''
        Altera a selação *self* movendo o início ou fim da seleção para a
        esquerda da seguinte forma:
        - Se o inicio de *self* está a esquerda da célula onde a seleção
          começou, ou a seleção só tem uma célula, então o início é movido uma
          célula para a esquerda (até o mínimo de 1).
        - Se o fim de *self* está a direita célula onde a seleção começou,
          então, o fim é movido uma célula para a esquerda.

        Exemplos
        >>> # Mudança do início
        >>> s = Selecao(6)
        >>> s.move_esquerda()
        >>> s.inicio()
        5
        >>> s.fim()
        6
        >>> s.move_esquerda()
        >>> s.inicio()
        4
        >>> s.fim()
        6
        >>> # Mudança do fim
        >>> s = Selecao(4)
        >>> s.move_direita()
        >>> s.move_direita()
        >>> s.move_direita()
        >>> s.inicio()
        4
        >>> s.fim()
        7
        >>> s.move_esquerda()
        >>> s.inicio()
        4
        >>> s.fim()
        6
        '''
        if len(self.col_end) > len(self.incell):
            self.col_end = self.col_end[1:]
        elif len(self.col_in) < len(self.incell) or len(self.incell) == len(self.col_end) == len(self.col_in):
            self.col_in = self.col_in[1:]
        return
