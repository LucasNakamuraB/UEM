from enum import Enum


class Dia(Enum):
    '''
    Um dia da semana.
    '''
    DOM = 0
    SEG = 1
    TER = 2
    QUA = 3
    QUI = 4
    SEX = 5
    SAB = 6


class Dias:
    '''
    Um conjunto de dias da semana que um evento deve se repetir.
    '''

    listad : list

    def __init__(self) -> None:
        '''
        Cria um novo conjunto vazio de dias.

        Exemplos
        >>> c = Dias()
        >>> c.lista()
        []
        '''
        self.listad = []
        return

    def alterna(self, d: Dia) -> None:
        '''
        Alterna a pertinencia do dia *d* em *self*, isto é, se *d* está em
        *self*, *d* é removido. Se *d* não está em *self*, *d* é adicionado.

        Exemplos
        >>> c = Dias()
        >>> c.alterna(Dia.SEX)
        >>> c.lista()
        ['sex']
        >>> c.alterna(Dia.SEG)
        >>> c.lista()
        ['seg', 'sex']
        >>> c.alterna(Dia.SEX)
        >>> c.lista()
        ['seg']
        '''
        i = 0
        removed = False
        while not removed and i < len(self.listad):
            if self.listad[i] == d:
                self.listad = self.listad[:i] + self.listad[i + 1:]
                removed = True
            i += 1
        if not removed:
            self.listad.append(d)
        return

    def lista(self) -> list[str]:
        '''
        Devolve uma lista com os dias (abreviações) em ordem da semana que
        estão em *self*.

        Exemplos
        >>> c = Dias()
        >>> c.lista()
        []
        >>> c.alterna(Dia.TER)
        >>> c.lista()
        ['ter']
        >>> c.alterna(Dia.DOM)
        >>> c.lista()
        ['dom', 'ter']
        >>> c.alterna(Dia.QUI)
        >>> c.alterna(Dia.SEG)
        >>> c.alterna(Dia.SAB)
        >>> c.alterna(Dia.QUA)
        >>> c.alterna(Dia.SEX)
        >>> c.lista()
        ['dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab']
        '''
        lst_dias = []
        dias = ['dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab']
        for i in dias:
            placed = False
            for j in self.listad:
                if j.name.lower() == i:
                    placed = True
            if placed:
                lst_dias.append(i)
        return lst_dias
