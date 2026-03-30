from pilha_arranjo import Pilha

def inverte_string(string : str) -> str:
    '''
    inverte a ordem dos caracteres de *string*

    exemplos

    >>> inverte_string('abc')
    'cba'
    '''
    char_pile = Pilha(128)
    invertido = ''
    for i in string:
        char_pile.empilha(i)
    while not char_pile.vazia():
        invertido = invertido + char_pile.desempilha()
    return invertido

def remove_vazio(pilha : Pilha):
    '''
    remove todas as strings vazias de *pilha*
    
    Exemplo

    >>> p = Pilha(256)
    >>> p.empilha('')
    >>> p.empilha('coisa')
    >>> remove_vazio(p)
    >>> p.desempilha()
    'coisa'
    '''
    cache = Pilha(128)
    aux = ''
    while not pilha.vazia():
        aux = pilha.desempilha()
        if not aux == '':
            cache.empilha(aux)
    while not cache.vazia():
        pilha.empilha(cache.desempilha())

def inverte_pilha(pilha : Pilha):
    '''
    inverte a ordem dos elementos de *pilha*

    Eemplos

    >>> p = Pilha(256)
    >>> p.empilha(1)
    >>> p.empilha(2)
    >>> inverte_pilha(p)
    >>> p.desempilha()
    1
    >>> p.desempilha()
    2
    '''

    inv_pile = Pilha(256)
    sec_pile = Pilha(256)

    while not pilha.vazia():
        inv_pile.empilha(pilha.desempilha())
    while not inv_pile.vazia():
        sec_pile.empilha(inv_pile.desempilha())
    while not sec_pile.vazia():
        pilha.empilha(sec_pile.desempilha())

def avalia_posfixa(lst : list):
    '''
    Calcula o resultado da operação posfixa contida em *lst*

    Exemplos

    >>> avalia_posfixa(['102'])
    102
    >>> avalia_posfixa(['55', '5', '/'])
    11
    >>> avalia_posfixa(['5', '6', '*', '3', '+'])
    33
    >>> avalia_posfixa(['5', '-6', '*', '3', '+', '10', '-'])
    -37
    '''
    operat = Pilha(256)
    for i in lst:
        if i == '+':
            b = operat.desempilha()
            a = operat.desempilha()
            operat.empilha(a + b)
        elif i == '-': 
            b = operat.desempilha()
            a = operat.desempilha()
            operat.empilha(a - b)
        elif i == '*':
            b = operat.desempilha()
            a = operat.desempilha()
            operat.empilha(a * b)
        elif i == '/':
            b = operat.desempilha()
            a = operat.desempilha()
            operat.empilha(int(a / b))
        else:
            operat.empilha(int(i))
    return operat.desempilha()





