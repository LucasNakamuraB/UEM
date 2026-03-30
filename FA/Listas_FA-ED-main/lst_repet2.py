import math

def posit_nome(lst, nome):
    '''
    produz uma lista com os índices das ocorrencias de *nome* em *lst*

    Exemplo

    >>> posit_nome(['a','b','b','a','b','a'], 'a')
    [0, 3, 5]
    '''
    lst_nome = []
    for i in range(len(lst)):
        if lst[i] == nome:
            lst_nome.append(i)
    return lst_nome

def rm_posit2(lst, n):
    '''
    Recebe uma lista e um índice, retorna a mesma lista sem o elemento do 
    indice especificado

    Exemplo

    >>> rm_posit2([0,1,2,3,4], 1)
    [0, 2, 3, 4]
    '''
    i = 0
    rm_n = 0
    n_lst = []
    for nb in lst:
        if i == n:
            rm_n = nb
        i += 1
    for nb in lst:
        if nb != rm_n:
            n_lst.append(nb)
    return n_lst

def rm_posit1(lst, n):
    '''
    Recebe uma lista e um índice, retorna a mesma lista sem o elemento do 
    indice especificado

    Exemplo

    >>> rm_posit1([0,1,2,3,4], 1)
    [0, 2, 3, 4]
    '''
    n_lst = []
    for i in range(len(lst)):
        if i != n:
            n_lst.append(lst[i])
    return n_lst


def rm_posit_sub(lst, n):
    '''
    Recebe uma lista e um índice, retorna a mesma lista sem o elemento do 
    indice especificado

    Exemplo

    >>> rm_posit_sub([0,1,2,3,4], 1)
    [0, 2, 3, 4]
    '''
    return lst[:n] + lst[n+1:]

def i_vira_n1(lst, idx, n):
    '''
    troca o elemento de indice *idx* em *lst* por *n*

    Exemplo

    >>> i_vira_n1([0, 1, 2, 3], 1, 2)
    [0, 2, 2, 3]
    '''
    n_lst = lst
    for i in range(len(lst)):
        if i == idx:
            n_lst[i] = n
    return n_lst

def i_vira_n3(lst, idx, n):
    '''
    troca o elemento de indice *idx* em *lst* por *n*

    Exemplo

    >>> i_vira_n3([0, 1, 2, 3], 1, 2)
    [0, 2, 2, 3]
    '''
    i = 0
    n_lst = []
    rm_nb = 0

    for num in lst:
        if idx == i:
            rm_nb = num
        i+=1
    
    for nb in lst:
        if nb != rm_nb:
            n_lst.append(nb)
        else:
            n_lst.append(n)
    return n_lst

def i_vira_n(lst,idx,n):
    '''
    troca o elemento de indice *idx* em *lst* por *n*

    Exemplo

    >>> i_vira_n3([0, 1, 2, 3], 1, 2)
    [0, 2, 2, 3]
    '''
    n_lst = lst
    n_lst[idx] = n
    return lst[:n]  + [n] + lst[n+1:]

def rotaciona(lst, n):
    '''
    Coloca os *n* primeiros elementos de uma lista no final dela

    Exemplo

    >>> rotaciona([2,2,1,1], 2)
    [1, 1, 2, 2]
    '''
    n_lst = lst[n:]
    nn = n
    while n > 0:
        n_lst.append(lst[nn - n])
        n -= 1
    return n_lst

def epar(lst):
    '''
    verifica se todos os numeros de *lst* são pares

    exemplos

    >>> epar([2,2])
    True
    >>> epar([1,2])
    False
    '''
    par = True
    i = len(lst) -1
    while i >= 0 and par:
        if lst[i]%2 != 0:
            par = False
        i -= 1
    return par

def isfalse(lst):
    '''
    verifica se todos os itens em *lst* de booleanos são falsos
    exemplo

    >>> isfalse([False, False, False])
    True
    >>> isfalse([False, True, False])
    False
    '''
    i = len(lst) - 1
    f = True
    while i >= 0 and f:
        if lst[i] == True:
            f = False
        i -= 1
    return f

def laurea(lst):
    '''
    verifica se mais de 2/3 dos elemetos de *lst* são maiores que 9.0

    exemplos

    >>> laurea([9.5, 9.5, 9.5, 0])
    True
    >>> laurea([9.5, 9.5, 0.0])
    False
    >>> laurea([0,0,0])
    False
    '''
    i = len(lst) - 1
    l = 0
    while i >=0 and l / len(lst) < 2/3:
        if lst[i] > 9.0:
            l += 1
        i -= 1
    return l / len(lst) > 2/3

def eh_dobrada(lst):
    '''
    produz True se *lst* puder ser reproduzida pela concatenação de 2 listas 
    iguais

    Exemplos

    >>> eh_dobrada([1,0,1,0])
    True
    >>> eh_dobrada([1,1,1])
    False
    >>> eh_dobrada([1,1,0,1])
    False
    '''
    e_dob = True
    if len(lst)%2 != 0:
        e_dob = False

    i = 0

    while i < (len(lst) / 2) and e_dob:
        if lst[i] != lst[int(len(lst)// 2 + i )]:
            
            e_dob = False
        i += 1
    return e_dob

def quant_soma(lst, n):
    '''
    produz um numero inteiro representando a quantidade de elementos de *lst*
    que precisam ser somados para superar *n*, se não for possível superar *n*,
    retorna -1

    exemplo

    >>> quant_soma([1,1,0,1], 2)
    4
    >>> quant_soma([1,0,0,1], 3)
    -1

    '''
    num = 0
    i = 0
    soma = 0
    while i < len(lst) and soma <= n:
        num += 1
        soma = soma + lst[i]
        i += 1
        
    if soma > n:
        return num
    else:
        return -1

def repet_string(string, n):
    '''
    Produs *string* repetida *n* vezes

    exemplo

    >>> repet_string('a', 4)
    'aaaa'
    '''
    n_str = ''
    for i in range(n):
        n_str = n_str + string
    return n_str

def int_str(n):
    '''
    Transforma o numero inteiro *n* em uma string

    exemplo
    >>> int_str(123)
    '123'
    '''
    nums = '0123456789'
    casas = ((n // 10) // 10) + 1
    string = ''
    last = 0
    curr = 0
    while casas >= 0:
        curr = ((n - last) // (10 ** casas))
        last = (n // 10 ** casas) * 10 ** casas
        string = string + nums[curr]
        casas -= 1
    return string

def perfeito(n):
    '''
    Verifica se a soma dos divisores de *n* é igual a *n*

    exemplos

    >>> perfeito(6)
    True
    >>> perfeito(3)
    False
    '''
    soma = 0
    num = 1
    while soma < n and num <= n // 2:
        if n%num == 0:
            soma += num
        num += 1
    return soma == n

def pi(n):
    '''
    Calcula o valor aproximado de pi até *n termos*

    exemplos

    >>> pi(4)
    2.8952
    >>> pi(6)
    2.976046
    '''
    pi = 0
    c = 0
    while c < n:
        pi += 4 * ((-1 )** c)/((2 * c) + 1)
        c += 1
    return round(pi ,n)

def m_ident(n):
    '''
    Cria uma matriz identidade de tamanho *n*

    Exemplos

    >>> m_ident(2)
    [[1, 0], [0, 1]]
    >>> m_ident(3)
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    '''
    id = 0
    matriz= []
    for i in range(0, n):
        line = []
        for j in range(0, n):
            if j == id:
                line.append(1)
            else:
                line.append(0)
        matriz.append(line)
        id += 1
    return matriz

def sum_col_zero(mtx : list[list[int]]):
    '''
    produz uma lista com o indice de todas as colunas da matriz *m* em que a
    soma dos elementos é zero

    Exemplos

    >>> sum_col_zero([[1, 1, -2], [0, 0, 1], [0, 0, 0]])
    [0, 2]
    '''
    soma  = 0
    lst_i = []
    for i in range(0, len(mtx)):
        soma = 0
        for j in mtx[i]:
            soma += j
        if soma == 0:
            lst_i.append(i)
    return lst_i

def sum_lin_zero(mtx : list[list[int]]) -> list:
    '''
    produz uma lista com o indice de todas as linhas da matriz *m* em que a
    soma dos elementos é zero

    Exemplos

    >>> sum_col_zero([[1, 1, -2], [0, 0, 1], [-1, 0, 1]])
    [0, 2]
    ''' 
    soma  = 0
    lst_i : list = []
    for i in range(len(mtx[0]) - 1):
        soma = 0
        for j in range(mtx):
            soma += [i][j]
        if soma == 0:
            lst_i.append(i)
    return lst_i

def mtx_sim(mtx):
    '''
    Verifica se *mtx* representa uma matriz simétrica

    Exemplos

    >>> mtx_sim([[1, 2, 4], [2, 1, 3], [4, 3, 1]])
    True
    '''
    e_sim = True
    i = len(mtx) - 1
    while i >= 0 and e_sim:
        for j in range(len(mtx) - 1):
            if mtx[i][j] !=mtx[j][i]:
                e_sim = False
        i -= 1
    return e_sim
    
def junta_lista(lst):
    '''
    junta as strings de *lst* em uma listagem conforme o portugues,
    tendo os ites separados por virgulas, com o ultimo item sendo separado por
    e

    Exemplo

    >>> junta_lista(['a', 'b', 'c'])
    'a, b, e c'
    
    '''
    email = ''
    for i in range(len(lst)):
        if i == len(lst) - 1 and len(lst) > 1:
            email = email + 'e ' + lst[i]
        else:
            email = email + lst[i] + ', '
    return email

def maior_rec(lst):
    '''
    recebe  uma lista onde cada string é seguido de um int, e cria uma nova
    lista com as strings e seus ints seguintes, ordenada de forma decrescente
    com base nos ints

    Exemplo

    >>> maior_rec(['a', 2, 'b', 3, 'c', 1])
    ['b', 3, 'a', 2, 'c', 1]
    '''
    ord_lst = []
    i_m = 1
     
    while len(lst) > 0:
        i = 1
        i_m = 1
        while i < len(lst):
            if lst[i_m] < lst[i]:
                i_m = i    
            i += 2
        ord_lst.append(lst[i_m -1])
        ord_lst.append(lst[i_m])
        lst = lst[:i_m - 1] + lst[i_m + 1:]

    return ord_lst
        
def str_list(string):
    '''
    recebe uma string de numeros dseparados por virgulas e produz uma lista
    de inteiros

    Exemplos:

    >>> str_list('1,2,3,4,-5')
    [1, 2, 3, 4, -5]
    '''
    i = 0
    s = ''
    n = 0
    lst = []
    count = True
    while i < len(string) - 1:
        count = True
        while count and i < len(string):
            if string[i] == ',':
                count = False
            else:
                s = s + string[i]
            i += 1
        n = int(s)
        lst.append(n)
        s = ''
    return lst
            
def qnts_craft(n):
    '''
    para construir um item de classe
    2 é necessário unir dois item de classe 1. Para construir um item de classe
    10 é necessário unir doistem de classe 9, retorna quantos itens de classe 1
    são necessários para construir um item de classe n, sendo *n* <= 10

    Exemplos

    >>> qnts_craft(2)
    2
    >>> qnts_craft(4)
    8
    >>> qnts_craft(10)
    512
    '''
    assert n <= 10 , 'n não deve ser maior que 10'
    its = 1
    while n > 1:
        its = its * 2
        n -= 1
    return its


