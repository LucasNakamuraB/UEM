def sum_to_lst(lst, n):
    '''
    modfica *lst* somando *n* a cada um de seus elementos

    Exemplos

    >>> sum_to_lst([1, 2, 3], 2)
    [3, 4, 5]
    '''
    for i in range(len(lst)):
        lst[i] += n
    return lst

def same_size(lst):
    '''
    deixa todas as strings de *lst* do mesmo tamaho, adicionando espaços em
    branco ao final delas se necessário

    Exemplos

    >>> same_size(['1','22', '4444','333'])
    ['1   ', '22  ', '4444', '333 ']
    '''
    size = 0
    check = True
    i = 0
    for i in range(len(lst)):
        if len(lst[i]) > size:
            size = len(lst[i])
    for i in range(len(lst)):
        lst[i] = lst[i] + ' ' * (size - len(lst[i]))
    return lst

def add_lst(lst, lst_add):
    '''
    modifica *lst* adicionando *lst_add* ao final dela

    Exemplos

    >>> add_lst([1, 2], [3, 4])
    [1, 2, 3, 4]
    '''
    for i in lst_add:
        lst.append(i)
    print(lst)

def insert_index(lst, i, v):
    '''
    insere o valor *v* no índice *i* de *lst*

    Exemplos

    >>> insert_index([0,1,3,4], 2 ,2)
    [0, 1, 2, 3, 4]
    '''
    lst.append(v)
    idx = len(lst) -1
    while idx > i:
        t = lst[idx - 1]
        lst[idx - 1] = lst[idx]
        lst[idx] = t
        idx -= 1
    print(lst)

def remove(lst, idx):
    '''
    remove o elemento de indice *idx* de *lst*

    exemplos

    >>> remove([0, 1, 2], 1)
    [0, 2]
    '''
    while idx < len(lst) - 1:
        t = lst[idx + 1]
        lst[idx + 1] = lst[idx]
        lst[idx] = t
        idx += 1
    lst.pop()
    return lst

def rm_idx_par(lst):
    '''
    remove da lista todos os elementos de índice par

    Exemplos

    >>> rm_idx_par([0, 1, 2, 3, 4])
    [1, 3]
    '''
    count = (len(lst) + 1) // 2
    for i in range(count):
        j = i
        while j < len(lst) - 1:
            t = lst[j + 1]
            lst[j + 1] = lst[j]
            lst[j] = t
            j += 1
    for n in range(count):
        lst.pop()
    return lst

def rm_vazio(lst):
    '''
    Remove todas as strings vazias de *lst*

    Exemplo

    >>> rm_vazio(['a', '', 'b', ''])
    ['a', 'b']
    '''
    i = 0
    while i < len(lst):
        if lst[i] == '':
            remove(lst, i)
        i += 1
    return lst

def separa_neg(lst):
    '''
    coloca os valores menores ou iguais a 0 de *lst* antes dos maioras que 0

    Exemplo

    >>> separa_neg([1, -1, 2, -2])
    [-1, -2, 1, 2]
    >>> separa_neg([1, -1, 2, -2 , -3])
    [-1, -2, -3, 1, 2]
    '''
    for i in range((len(lst) + 1) // 2):
        if lst[i] > 0:
            j = i
            while j < len(lst) - 1:
                t = lst[j + 1]
                lst[j + 1] = lst[j]
                lst[j] = t
                j += 1
    return lst

def ord_select(lst):
    '''
    faz ordenação por seleção em *lst*

    Exemplo

    >>> ord_select([2, 1, 5 ,6 , 3])
    [1, 2, 3, 5, 6]
    '''
    i = 0
    c = lst[0]
    t = 0
    while i < len(lst):
        c = i
        for n in range(i, len(lst)):
            if lst[n] < lst[c]:
                c = n
        while c > i:
            t  =  lst[c]
            lst[c] = lst[c - 1]
            lst[c - 1] = t
            c -= 1
        i += 1
    print(lst)


