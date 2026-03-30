from fila_arranjo_fim import Fila as FilaF
from fila_arranjo_inicio_fim import Fila as FilaIF
from collections import deque

lista = list

def operacoes(fila: deque | list, n: int):
    '''
    Inserie os elementos '1', '2', ..., 'n' em *fila*
    e depois esvazia *fila*.
    '''
    for i in range(n + 1):
        fila.append(i)
    while len(fila) > 0:
        if isinstance(fila, deque):
            fila.popleft()
        else:
            fila.pop(0)


def main():
    from timeit import timeit
    for fila in ['deque', 'lista']:
        print(fila)
        for n in [10000, 20000, 40000, 80000]:
            tempo = timeit(f'operacoes({fila}(), {n})',
                           setup=f'from __main__ import operacoes, {fila}',
                           number=10)
            print(n, tempo)


if __name__ == '__main__':
    main()
