def repet_v(n, v):
    '''
    Produz uma lista com *n* repetições do valor *v*

    Exemplos

    >>> repet_v(3, 1)
    [1, 1, 1]
    >>> repet_v(0, 4)
    []
    '''
    lst = [v]
    if n == 0:
        lst = []
    else:
        lst = lst + repet_v(n - 1, v)
    return lst 

def fatorial(n):
    '''
    calcula o fatorial de *n*

    Exemplo

    >>> fatorial(4)
    24
    >>> fatorial(3)
    6
    '''
    assert n > -1

    if n == 0:
        return 1
    else:
        n = n * fatorial(n - 1)
    return n

def contagem(n):
    '''
    Produz uma string com os numeros de 1 a *n* separados por virgula

    Exemplo

    >>> contagem(4)
    '1, 2, 3, 4'
    >>> contagem(-3)
    '-1, -2, -3'
    '''
    s = str(n)
    if n == 0:
        return ''
    elif abs(n) == 1:
        s = s
    elif n > 0:
        s = contagem(n - 1) + ', ' + s
    else:
        s = contagem(n + 1) + ', ' + s

    return s
    
def par(n):
    '''
    Retorna True se *n* é par

    Exemplo

    >>> par(2)
    True
    >>> par(3)
    False
    '''

    p = True
    if n == 1:
        p = False
    elif n == 0:
        p = True
    else:
        p = not impar(n - 2)
    return p

def impar(n):
    '''
    retorna True se n e impar

    Exemplo

    >>> impar(3)
    True
    >>> impar(2)
    False
    '''
    i = True
    if n == 0:
        i = False
    elif n == 1:
        i = True
    else:
        i =  not par(n - 2)
    return i

def concatena(lst):
    '''
    concatena todas as strings de *lst*

    Exemplo
    >>> concatena(['o', 'l', 'á'])
    'olá'
    '''
    
    if len(lst) == 0:
        return ''
    else:
        s = lst[0]
        s = s + concatena(lst[1:])

    return s

def n_is_in_list(lst, n):
    '''
    Retorna True se *n* está em *lst*

    Exemplos

    >>> n_is_in_list([0,1,2,3,4], 3)
    True
    >>> n_is_in_list([0,1,2,3,4], 5)
    False
    '''
    if len(lst) == 1:
        return lst[0] == n
    else:
        return lst[0] == n or n_is_in_list(lst[1:], n)

def ebinaria(lst):
    '''
    Verifica se uma lista é composta apenas por 1 ou 0

    Exemplos

    >>> ebinaria([1, 1, 0, 1, 0, 0])
    True
    >>> ebinaria([1, 0, 1, 2])
    False
    '''
    if len(lst) == 1:
        return 0 <= lst[0] <= 1
    else:
        return 0 <= lst[0] <= 1 and ebinaria(lst[1:])

def valor_max(lst):
    '''
    Retorna o valor máximo de uma lista

    Exemplo

    >>> valor_max([0, 1, 5, 2, 4])
    5
    '''
    assert len(lst) > 0
    maior = lst[0]
    if len(lst) == 1:
        return maior
    else:
        m = valor_max(lst[1:])
        if maior < m:
            maior = m
    return maior

def max_str(lst):
    '''
    Retorna o tamanho da maior string de *lst*, *n* deve ser o tamanho de *lst*

    Exemplo

    >>> max_str(['1', '22', '666666', '333'])
    6
    '''
    i = len(lst)
    m = len(lst[i -1])
    if i == 1:
        if len(lst[0]) > m:
            m = len(lst[0])
        return m
    else:
        max = max_str(lst, i-1)
        if m < max:
            m = max
    return m
            
def lst_posit(lst, i):
    '''
    Cria uma lista com todos os
    '''
        



