import sys
from dataclasses import dataclass

times = []
placar = []
maior_nome = 0

@dataclass
class Time():
    nome : str
    gols_r : int
    saldo : int
    vit : int
    pontos : int
    pontos_a : int
    jogos_a : int

def main():
    if len(sys.argv) < 2:
        print('Nenhum nome de arquivo informado.')
        sys.exit(1)
    if len(sys.argv) > 2:
        print('Muitos parâmetros. Informe apenas um nome de arquivo.')
        sys.exit(1)
    jogos = le_arquivo(sys.argv[1])
    # TODO: solução da pergunta 1
    # TODO: solução da pergunta 2
    # TODO: solução da pergunta 3

    contab_jogos(jogos)
    ordena(times)
    gera_placar(placar)
    aproveitamento(placar)
    def_menos_vazada(placar)

def le_arquivo(nome: str) -> list[str]:
    '''
    Lê o conteúdo do arquivo *nome* e devolve uma lista onde cada elemento
    representa uma linha.
    Por exemplo, se o conteúdo do arquivo for
    Sao-Paulo 1 Atletico-MG 2
    Flamengo 2 Palmeiras 1
    a resposta produzida é
    [‘Sao-Paulo 1 Atletico-MG 2’, ‘Flamengo 2 Palmeiras 1’]
    '''
    try:
        with open(nome) as f:
            return f.readlines()
    except IOError as e:
        print(f'Erro na leitura do arquivo "{nome}": {e.errno} - {e.strerror}.');
        sys.exit(1)

# Análise da pergunta 1
# 
# É necessário percorrer a lista "jogos" e adicionar os times que aparecem nela
# e adiciona-los a uma lista de times na forma de um tipo próprio de dado e
# caso algum time se repita, seus dados serão adicionados ao time já existente
# na lista de times, em seguida, deve ser criada uma função para percorrer a 
# lista de times e adicioná-los de forma ordenada a uma lista de classificação,
# tendo como critérios: Pontos (vitória = 3 pontos, empate = 1, derrota = 0),
# número de vitórias, saldo de gols, e ordem alfabética
# O programa deve retornar colunas contendo: nome do time, pontos, e saldo de gols
# cada linha deve ter o mesmo número de caracteres, de acordo com o time de nome
# mais extenso
# 
# Tipos de Dados
# 
# Partida: são strings contidas na lista "jogos" e seguem o formato “Anfitrião Gols Visitante Gols”
# e deve ser separado em uma string para cada nome de time e um numero inteiro para os gols de cada time 
# 
# Time: tipo composto que representa cada time presente no campeonato, contém o
# nome do time na forma de string, o total de pontos como anfitrião, total de gols recebidos, saldo de gols, 
# numero de vitórias e numero de pontos
# 
# Análise da pergunta 2
# 
# É necessário fazer uma função para retornar e imprimir o time com o maior
# aproveitamento jogando como anfitrião, para isso é necessário apenas escolher
# da lista de times o time com maior número de pontos como anfitrião e apresentar
# porcentagem do numero de pontos em relação ao máximo possível (15)
# 
# Tipos de dados
# 
# pontos como anfitrião: numero inteiro contido no tipo composto 'time', já
# mencionado anteriormente
# 
# Análise da pergunta 3
# 
# é necessário apenas fazer uma função para percorrer a lista e retornar o 
# time com o menor numero no campo de gols recebidos do dado composto 'time'

def contab_jogos(lst : list[str]):
    '''
    trensforma as strings de *lst* em dados, que são adicionados aos sess
    respectivos tipos compostos "Time", a string é dividida com base nos espaços
    e os ítens de indice par são os nomes dos times anfitrição e visitante respectivamente
    e os de índice ímpar são os gols de cada um deles cada time gerado receberá
    um valor de nome, gols, vitórias, saldo de gols e gols recebidos, e será
    adicionado à lista *times* por meio da função *contab_time*
    '''
    anfit = Time('', 0,0,0,0,0,0)
    visit = Time('', 0,0,0,0,0,0)
    count = True
    g_a = 0
    g_v = 0
    dados = []
    cache = ''
    for j in lst:
        for i in range(len(j)):
            if j[i] != ' ':
                cache = cache + j[i]
            else:
                dados.append(cache)
                cache = ''
        dados.append(cache[0])
        anfit.nome = dados[0]
        g_a = int(dados[1])
        visit.nome = dados[2]
        g_v = int(dados[3])
        anfit.saldo = g_a - g_v
        anfit.gols_r = g_v
        visit.saldo = g_v - g_a
        visit.gols_r = g_a
        anfit.jogos_a = 1
        if g_a > g_v:
            anfit.pontos = 3
            anfit. vit = 1
            anfit.pontos_a = 3
        elif g_v > g_a:
            visit.pontos = 3
            visit.vit = 1
        else:
            anfit.pontos = 1
            visit.pontos = 1
        contab_time(anfit)
        contab_time(visit)
        dados = []
        cache = ''
        anfit = Time('', 0,0,0,0,0,0)
        visit = Time('', 0,0,0,0,0,0)

def contab_time(time : Time):
    '''
    adiciona *time* a lista *times*  e caso algum dos times ja esteja na lista,
    adiciona apenas os dados ao elemento correspondente
    '''
    repet = False
    if len(times) == 0:
        times.append(time)
    for t in range(len(times)):
        if time.nome == times[t].nome:
            times[t].pontos += time.pontos
            times[t].vit += time.vit
            times[t].saldo += time.saldo
            times[t].gols_r += time.gols_r
            times[t].pontos_a += time.pontos_a
            times[t].jogos_a += time.jogos_a
            repet = True
    if repet == False:
        times.append(time)


def ordena(lst : list[Time]):
    '''
    extrai itens de *lst* e adiciona eles a *placar* de forma ordenada com base
    nos dados de pontos, vitorias, saldo de gols e nome contidos no tipo composto
    '''
    i = 0
    j = 0
    l = 0
    escolhido = False
    while i < len(lst):
        top_time = 0
        j = 1
        while j < len(lst):
            if lst[j].nome == lst[top_time].nome:
                top_time = j
            elif lst[j].pontos > lst[top_time].pontos:
                top_time = j
            elif lst[j].pontos == lst[top_time].pontos:
                if lst[j].vit > lst[top_time].vit:
                    top_time = j
                elif lst[j].vit == lst[top_time].vit:
                    if lst[j].saldo > lst[top_time].saldo:
                        top_time = j
                    elif lst[j].saldo == lst[top_time].saldo:
                        while escolhido == False:
                            if lst[j].nome[l] < lst[top_time].nome[l]:
                                top_time = j
                                escolhido = True
                            l += 1
            j += 1
        i += 1
        placar.append(lst[top_time])
        remover(times, top_time)


def gera_placar(lst : list):
    '''
    
    >>> vsf = [Time('bomdia',1,1,1,1,1), Time('boanoite',2,2,1,1,1)]
    >>> gera_placar(vsf)
    0
    '''
    maior_nome = tam_max(placar)
    plac = ''
    for t in lst:
        plac = plac + ajust_time(t)
    print('Gols' + ' ' * (maior_nome - 3) + 'Pontos' + ' ' + 'Vitórias' + ' ' + 'Saldo')
    print(plac)

def ajust_time(time : Time):
    '''
    >>> maior_nome = 10

    >>> ajust_time(Time('bomdia',1,1,1,1,1))
    '''
    maior_nome = tam_max(placar)
    t_ajust = ''
    pontos = str(time.pontos)
    saldo = str(time.saldo)
    vitorias = str(time.vit)
    if time.pontos < 10 and time.pontos > 0:
        pontos = '0' + pontos
    if time.vit < 10 and time.vit > 0:
        vitorias = '0' + vitorias
    if time.saldo < 10 and time.saldo > 0:
        saldo = '0' + saldo
    
    t_ajust = time.nome + ' ' * (maior_nome - len(time.nome)) + ' ' + pontos +'      ' + vitorias +'     ' + saldo + '\n'
    return t_ajust
    
def tam_max(lst : list):
    '''
    Retorna o tamanho da maior string contida no campo de nome dos elementos
    de tipo Time de *lst*
    '''
    m_n = 0
    for n in lst:

        if len(n.nome) > m_n:
            m_n = len(n.nome)
    return m_n

def remover(lst : list, idx : int):
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

def aproveitamento(lst : list[Time]):
    '''
    Imprime um mensagem no terminal mostrando o elemento de *lst* com o maior
    aproveitamento jogando como anfitrião e a porcentagem de seus pontos como
    anfitrião e o máximo de pontos possíveis como anfitrião
    '''
    m_time = lst[0]
    for i in range(len(lst)):
        if lst[i].pontos_a > m_time.pontos_a:
            m_time = lst[i]
    print('O time com o melhor aproveitamento foi o ' + m_time.nome \
           + ', com ' + str(round((m_time.pontos_a / (m_time.jogos_a * 3))*100, 2)) + \
         '%' + ' de aproveitamento')

def def_menos_vazada(lst : list[Time]):
    '''
    Imprime uma mensagem no terminal informando qual é o elemento de *lst*
    com o menor valor de gols_r (gols recebidos)
    '''
    m_time = lst[0]
    for i in range(len(lst)):
        if lst[i].gols_r < m_time.gols_r:
            m_time = lst[i]
    print('O time com a defesa menos vazada foi o ' + m_time.nome\
          + ' com apenas ' + str(m_time.gols_r) + ' Gols recebidos')


if __name__ == '__main__':
    main()