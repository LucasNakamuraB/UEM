from enum import Enum,auto
from dataclasses import dataclass

def concatena(lst):
    '''
    retorna uma unica string a partir da concatenação dos elemntos de *lst*

    Exemplos

    >>> concatena(['a','b','c'])
    'abc'
    '''
    conc = ''
    for i in lst:
        conc = conc + i
    return conc

def lst_num(lst):
    '''
    retorna uma lista de numeros a partir de uma lista de strings
    exemplos
    >>> lst_num(['1','1','2'])
    [1, 1, 2]
    '''
    nums = []
    for i in lst:
        nums.append(int(i))
    return nums

def produto(lst):
    '''
    retorna o produto dos elementos de *lst*

    >>> produto([1,2,3])
    6
    '''
    p = lst[0]
    for i in lst:
        p = p * i
    return p

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
    for i in lst:
        if i%2 == 0:
            pass
        else:
            par = False
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
    f = True
    for i in lst:
        if i:
            f = False
    return f

def tira_zero(lst):
    '''
    cria uma nova lista a partir de *lst*, removendo todos os zeros

    exemplos

    >>> tira_zero([0,1,0,2])
    [1, 2]
    >>> tira_zero([1,2])
    [1, 2]
    '''
    n_lst = []
    for i in lst:
        if i != 0 :
            n_lst.append(i)
    return n_lst

def count_min_2rep(lst):
    '''
    conta quantas vezes o valor minimo de uma função aparece

    >>> count_min_2rep([2,1,1,2,0,0,0])
    3
    '''
    n = 0
    min = lst[0]
    for i in lst:
        if i < min:
            min = i
    
    for i in lst:
        if i == min:
            n += 1
    
    return n

def count_min_1rep(lst):
    '''
    conta quantas vezes o valor minimo de uma função aparece

    >>> count_min_1rep([2,1,1,2,0,0,0])
    3
    '''
    n = 1
    min = lst[0]
    for i in lst:
        if i < min:
            min = i
            n = 1
        elif i == min:
            n += 1
    return n
#a função de 1 repetição á mais simples

def amp_3etp(lst):
    '''
    retorna a diferença entre o maior e menor elemento de *lst*

    exemplo
    
    >>> amp_3etp([1,2,3,3,2,4])
    3
    '''
    amp = 0
    min = lst[0]
    max = lst[0]
    for i in lst:
        if i < min:
            min = i
    for i in lst:
        if i > max:
            max = i
    amp = max - min
    return amp

def amp_1rep(lst):
    '''
    retorna a diferença entre o maior e menor elemento de *lst*

    exemplo
    
    >>> amp_1rep([1,2,3,3,2,4])
    3
    '''
    amp = 0
    min = lst[0]
    max = lst[0]

    for i in lst:
        if i > max:
            max = i
        elif i < min:
            min = i
        amp = max - min
    amp = max - min
    return amp
# 1 repetição é mais simples

class maismenos(Enum):
    MAIS = auto()
    MENOS = auto()
    IGUAL = auto()

def mais_pn(lst):
    '''
    retorna se a lista possui mais numeros positivos ou negativos

    exemplo

    >>> mais_pn([1,2,3,-1,-2])
    <maismenos.MAIS: 1>
    >>> mais_pn([1,2,-1,-2,-3])
    <maismenos.MENOS: 2>
    >>> mais_pn([1,2,-1,-2])
    <maismenos.IGUAL: 3>
    '''
    p = 0
    n = 0
    for i in lst:
        if i >= 0:
            p += 1
        else:
            n += 1
    if p > n:
        return maismenos.MAIS
    elif p < n:
        return maismenos.MENOS
    else:
        return maismenos.IGUAL

def sep_pn(lst):
    '''
    recebe *lst* e retorna uma lista com os numeros negativos no inicio e
    positivos no final

    exemplo

    >>> sep_pn([1,-1,2,-2,3,-3])
    [-1, -2, -3, 1, 2, 3]
    '''
    l_pos = []
    l_neg = []
    for i in lst:
        if i >= 0:
            l_pos.append(i)
        else:
            l_neg.append(i)
    return l_neg + l_pos

@dataclass
class Position():
    x : int
    y : int
    z : int

class Moves(Enum):
    CIMA = auto()
    BAIXO = auto()
    FRENTE = auto()
    TRAS = auto()
    DIREITA = auto()
    ESQUERDA = auto()

def mover(pos : Position, lst : list):
    '''
     altera os valores de *pos* com base na lista *lst* de comandos
     x aumenta com DIREITA e diminui com ESQUERDA
     y aumenta com CIMA e diminui com BAIXO
     z aumenta com FRENTE e diminui com TRAS

     exemplos

    >>> mover(Position(0,0,0), [Moves.CIMA, Moves.FRENTE, Moves.DIREITA])
    Position(x=1, y=1, z=1)
    >>> mover(Position(0,0,0), [Moves.BAIXO, Moves.TRAS, Moves.ESQUERDA])
    Position(x=-1, y=-1, z=-1)
    '''
    new_pos = pos
    for move in lst:
        if move == Moves.CIMA:
            new_pos.y += 1
        elif move == Moves.BAIXO:
            new_pos.y -= 1
        elif move == Moves.FRENTE:
            new_pos.z += 1
        elif move == Moves.TRAS:
            new_pos.z -= 1
        elif move == Moves.DIREITA:
            new_pos.x += 1
        else:
            new_pos.x -= 1
    return new_pos

def doar( saldo_inicial, lst):
    '''
    soma incrementalmente os valores de *lst* a uma variavel de valor igual a
    *saldo_inicial* e sempre que esta variavel ficar com valor abaixo de 0, soma
    10 ao valor que será retornado

    exemplos

    >>> doar(10, [-20,20,-20,20])
    20.0
    '''
    doa = 0.0
    saldo = saldo_inicial
    for i in lst:
        saldo += i
        if saldo < 0:
            doa += 10
    return doa

@dataclass
class Desempenho():
    pontos : int
    vitorias : int
    saldo : int

@dataclass
class Partida():
    gols_feitos : int
    gols_sofridos : int

def desemp(lst):
    '''
    calcula o numero de pontos vitorias e saldo de gols com base nos dados de 
    Partida contidos em *lst*,para cada valor, subtraem-se os gols sofridos dos
    gols feitos e adiciona o valor a um total, se o numero de gols feitos for 
    maior que o d gols sofridos, adiciona-se 1 ao contador de vitórias e 3 ao 
    numero de pontos, e se for igual, adiciona-se 1 ao numero de pontos

    exemplo

    >>> desemp([Partida(5, 1), Partida(1,1), Partida(0,2)])
    Desempenho(pontos=4, vitorias=1, saldo=2)
    '''
    desempenho : Desempenho
    pnt = 0
    vit = 0
    sald = 0
    for p in lst:
        if p.gols_feitos > p.gols_sofridos:
            vit += 1
            pnt += 3
        elif p.gols_feitos == p.gols_sofridos:
            pnt += 1
        sald += p.gols_feitos - p.gols_sofridos
    desempenho = Desempenho(pnt, vit, sald)
    return desempenho

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
    l = 0
    for i in lst:
        if i > 9.0:
            l += 1
    return l / len(lst) > 2/3

class Votos(Enum):
    PRIMEIRO = auto()
    SEGUNDO = auto()
    BRANCO = auto()

def conta_votos(lst, cand):
    '''
    conta quantas vezes *cand* aparece em *lst*

    exemplos

    >>> conta_votos([Votos.PRIMEIRO, Votos.PRIMEIRO, Votos.SEGUNDO], Votos.PRIMEIRO)
    2
    '''
    votes = 0
    for v in lst:
        if v == cand:
            votes += 1
    return votes

def eleic(lst):
    '''
    verifica qual dado do tipo Votos aparece mais vezes em *lst* e retorna
    a string "dado.name venceu", mas caso a maioria seja Votos.BRANCO, retorna
    "Novas Eleições"
    
    Exemplos

    >>> eleic([Votos.PRIMEIRO, Votos.PRIMEIRO, Votos.SEGUNDO])
    'PRIMEIRO venceu'

    >>> eleic([Votos.PRIMEIRO, Votos.SEGUNDO, Votos.SEGUNDO])
    'SEGUNDO venceu'
    
    >>> eleic([Votos.PRIMEIRO, Votos.BRANCO, Votos.SEGUNDO])
    'Novas Eleições'

    >>> eleic([Votos.BRANCO, Votos.BRANCO, Votos.SEGUNDO])
    'Novas Eleições'
    '''
    prim = conta_votos(lst, Votos.PRIMEIRO)
    sec = conta_votos(lst, Votos.SEGUNDO)
    branco = conta_votos(lst, Votos.BRANCO)
    if branco < prim + sec:
        if prim > sec:
            return Votos.PRIMEIRO.name + ' venceu'
        elif sec > prim:
            return Votos.SEGUNDO.name + ' venceu'
        else:
            return 'Novas Eleições'
    else:
        return 'Novas Eleições'
    
@dataclass
class Ponto():
    x : float
    y : float

@dataclass
class Retangulo():
    altura : float
    largura : float

def menor (lst):
    '''
    retorna o menor numero de *lst*
    '''
    m = lst[0]
    for n in lst:
        if n < m:
            m = n
    return m

def maior (lst):
    '''
    retorna o maior numero de *lst*
    '''
    m = lst[0]
    for n in lst:
        if n > m:
            m = n
    return m

def min_rect(lst):
    '''
    calcula o retangulo de menor altura e largura que pode conter todos os
    pontos contidos em *lst* no plano cartesiano q que tenha os lados paralelos
    ao eixo x e y

    exemplo

    >>> min_rect([Ponto(0,2), Ponto(2,4), Ponto(4,2), Ponto(2,0)])
    Retangulo(altura=4, largura=4)
    '''
    inf = Ponto(x=0, y=0)
    sup = Ponto(x=0, y=0)
    h = 0
    l = 0
    rect : Retangulo
    for p in lst:
        if p.x < inf.x:
            inf.x = p.x
        if p.y < inf.y:
            inf.y = p.y
        if p.x > sup.x:
            sup.x = p.x
        if p.y > sup.y:
            sup.y = p.y
    l = sup.x - inf.x
    h = sup.y - inf.y
    rect = Retangulo(l, h)
    return rect
