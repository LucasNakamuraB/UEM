from lista_arranjo import Lista

def primos(lim: int) -> Lista:
    '''
    Encontra todos os números primos menores que *lim*.
    3
    Exemplos:
    >>> primos(2)
    '[]'
    >>> primos(20)
    '[2, 3, 5, 7, 11, 13, 17, 19]'
    '''
    primos: Lista = Lista()
    n = 2
    while n < lim:
        eh_primo = True
        i = 0
        while eh_primo and i < primos.num_itens():
            if n % primos.get(i) == 0:
                eh_primo = False
            i = i + 1
        if eh_primo:
            primos.add(n)
        n = n + 1
    return primos.str()

def rm_repet(lst : Lista):
    '''
    Remove todos os elementos repetidos de *lst*

    Exemplos

    >>> l = Lista()
    >>> l.add(1)
    >>> l.add(1)
    >>> l.add(2)
    >>> l.add(2)
    >>> l.add(3)
    >>> l.add(2)
    >>> l.add(4)
    >>> rm_repet(l)
    >>> l.str()
    '[1, 2, 3, 4]'
    '''
    first_ap = Lista()
    i = 0
    while i < lst.num_itens():
        repet = False
        for j in range(first_ap.num_itens()):
            if lst.get(j) == first_ap.get(j):
                repet = True
        if repet:
            lst.remove(i)
        else:
            first_ap.insere(i, lst.get(i))
        i += 1


