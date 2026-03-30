from __future__ import annotations

class Conjunto:
    '''Um conjunto de números inteiros
    Exemplos
    >>>> c1 = Conjunto()
    >>> c1.adiciona(2)
    >>> c1.adiciona(3)
    >>> c1.adiciona(4)
    >>> c1.str()
    '{2, 3, 4}'
    >>> c2 = Conjunto()
    >>> c2.adiciona(1)
    >>> c2.adiciona(2)
    >>> c2.adiciona(4)
    >>> c2.str()
    '{1, 2, 4}'
    >>> c3 = c1.uniao(c2)
    >>> c3.str()
    '{1, 2, 3, 4}'
    >>> c3.eh_uniao(c1, c2)
    True
    >>> c4 = Conjunto()
    >>> c4.adiciona(5)
    >>> c3.eh_uniao(c3, c4)
    False
    '''
    tamanho : int
    conjunto : list[int | None]
    chaves : list[int]
    elementos : int

    def __init__(self) -> None:
        '''Cria um novo conjunto vazio.'''
        self.chaves = []
        self.tamanho = 256
        self.conjunto = [None] * self.tamanho
        self.elementos = 0
    def add_chave(self , c : int) -> None:
        '''
        Adicione *c* como uma chave da tabela de forma ordenada
        '''
        if self.chaves == []:
            self.chaves.append(c)
        elif c > self.chaves[len(self.chaves) - 1]:
            self.chaves.append(c)
        elif c < self.chaves[0]:
            self.chaves = [c] + self.chaves
        else:
            for i in range(len(self.chaves)):
                if c > self.chaves[i] and c < self.chaves[i+1]:
                    self.chaves = self.chaves[:i+1] + [c] + self.chaves[i+1:]
    def colision(self, n : int) -> None:
        '''
        Lida com colisões alocando o elemento *n* à chave mais próxima
        '''
        posit = n % self.tamanho
        adicionado = False
        i = posit + 1
        while not adicionado and i != posit:
            if self.conjunto[i] is None:
                self.conjunto[i] = n
                self.add_chave(i)
                adicionado = True
    def procura(self, n: int, c: int):
        '''
        Percorre o conjunto a partir da chave *c*, a procura do inteiro *n*, ate encontrar um valor None
        e retorna True caso o encontre, e false no caso contrario
        '''
        achou = False
        stop = False
        if c is None:
            return False
        while not achou and not stop:
            posit = n % self.tamanho
            if self.conjunto[posit] == n:
                achou = True
            elif self.conjunto[posit] is None:
                stop = True
            c += 1
        return achou
    def adiciona(self, n: int) -> None:
        '''Adiciona *n* ao conjunto'''
        assert self.elementos < self.tamanho, "O conjunto está cheio!"
        posit = n % self.tamanho
        if self.conjunto[posit] is None:
            self.conjunto[posit] = n
            self.add_chave(posit)
        elif self.conjunto[posit] == n:
            pass
        elif self.conjunto[posit] != posit:
            self.colision(self.conjunto[posit]) #type: ignore
            self.conjunto[posit] = n
        else:
            self.colision(n)
        self.elementos += 1
    def str(self) -> str:
        '''Cria uma string com os elementos entre chaves e separados por vírgula.'''
        string = '{'
        for c in self.chaves:
            string = string + str(self.conjunto[c]) + ', '
        string = string[:len(string) -2] + '}'
        return string
    def uniao(self, outro: Conjunto) -> Conjunto:
        '''Realiza a união entre *self* e *outro*.'''
        new = Conjunto()
        for c in self.chaves:
            new.adiciona(self.conjunto[c]) # type: ignore
        for c in outro.chaves:
            new.adiciona(outro.conjunto[c])# type: ignore
        # O type: ignore é necessário pois o mypy considera que o item do conjunto
        # pode ser None, mas como o item está sendo acessado por uma chave
        # então é impossível que seja None, mas o mypy não vê isso
        return new
    def eh_uniao(self, c1: Conjunto, c2: Conjunto) -> bool:
        '''
        Verifica se o conjunto é uma união entre *c1* e *c2*
        '''
        uniao = True
        for c in c1.chaves:
            item = c1.conjunto[c]
            if not self.procura(item, item):
                uniao = False
        for c in c2.chaves:
            item = c2.conjunto[c]
            if not self.procura(item, item):
                uniao = False
        return uniao