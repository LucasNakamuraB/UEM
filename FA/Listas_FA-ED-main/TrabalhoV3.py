import sys
from dataclasses import dataclass

@dataclass
class Time:
    nome : str
    gols_r : int
    saldo : int
    vit : int
    pontos : int
    pontos_a : int
    jogos_a : int

@dataclass
class Jogo:
    anfit : str
    gols_anf: int
    visit : str
    gols_vis : int

def main():
    if len(sys.argv) < 2:
        print('Nenhum nome de arquivo informado.')
        sys.exit(1)
    if len(sys.argv) > 2:
        print('Muitos parâmetros. Informe apenas um nome de arquivo.')
        sys.exit(1)

    placar = []
    jogos = le_arquivo(sys.argv[1])
    times = contab_jogos(jogos)
    ordena(times, placar)
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

def contab_jogos(lst : list[str]) -> list[Time]:
    '''
    trensforma as strings de *lst* em dados, que são adicionados aos sess
    respectivos tipos compostos "Time", a string é dividida com base nos espaços
    e os ítens de indice par são os nomes dos times anfitrição e visitante respectivamente
    e os de índice ímpar são os gols de cada um deles cada time gerado receberá
    um valor de nome, gols, vitórias, saldo de gols e gols recebidos, e será
    adicionado à lista *times* por meio da função *contab_time*

    Exemplo
    >>> contab_jogos(['Sao-Paulo 1 Atletico-MG 2', 'Flamengo 2 Palmeiras 1'])
    [Time('Sao-Paulo, 2, -1, 0, 0, 0, 1), Time('Atletico-MG', 1, 1, 1, 3, 3, 0), Time('Flamengo, 1, 1, 1, 3, 0, 0), Time('Palmeiras, 2, -1, 0, 0, 0, 0)]

    '''
    jogo : Jogo
    lst_times : list[Time] = []
    times = []
    for j in lst:
        jogo = gera_jogo(j)
        times = gera_times(jogo)
        anfit = times[0]
        visit = times[1]
        contab_time(anfit, lst_times)
        contab_time(visit, lst_times)
    return lst_times

def gera_jogo(string : str) -> Jogo:
    '''
    recebe *string* no formato: 'Nome-do-time-anfitrião gols-do-anfitrião Nome-do-time-visitante gols-do-visitante'
    e retorna um dado composto do tipo jogo
    '''
    dados : list = []
    jogo = Jogo('', 0, '', 0)
    cache : str = ''
    for i in range(len(string)):
        if string[i] != ' ':
            cache = cache + string[i]
        else:
            dados.append(cache)
            cache = ''
    dados.append(cache)
    jogo.anfit = dados[0]
    jogo.gols_anf = int(dados[1])
    jogo.visit = dados[2]
    jogo.gols_vis = int(dados[3])
    return jogo


def gera_times(jogo : Jogo) -> list[Time]:
    '''
    Gera uma lista contendo dois dados do tipo time com base *jogo*
    o primeiro item da lista produzida será o anfitrião, e o segundo o visitante
    '''
    anfit = Time('', 0,0,0,0,0,0)
    visit = Time('', 0,0,0,0,0,0)
    times = []

    anfit.nome = jogo.anfit
    visit.nome = jogo.visit
    anfit.saldo = jogo.gols_anf - jogo.gols_vis
    anfit.gols_r = jogo.gols_vis
    visit.saldo = jogo.gols_vis - jogo.gols_anf
    visit.gols_r = jogo.gols_anf
    anfit.jogos_a = 1
    if jogo.gols_anf > jogo.gols_vis:
        anfit.pontos = 3
        anfit. vit = 1
        anfit.pontos_a = 3
    elif jogo.gols_vis > jogo.gols_anf:
        visit.pontos = 3
        visit.vit = 1
    else:
        anfit.pontos = 1
        anfit.pontos_a = 1
        visit.pontos = 1
    times.append(anfit)
    times.append(visit)
    return times

def contab_time(time : Time, lst : list[Time]):
    '''
    adiciona *time* a lista *times*  e caso algum dos times ja esteja na lista,
    adiciona apenas os dados ao elemento correspondente
    '''
    repet = False
    for t in range(len(lst)):
        if time.nome == lst[t].nome:
            lst[t].pontos += time.pontos
            lst[t].vit += time.vit
            lst[t].saldo += time.saldo
            lst[t].gols_r += time.gols_r
            lst[t].pontos_a += time.pontos_a
            lst[t].jogos_a += time.jogos_a
            repet = True
    if repet == False:
        lst.append(time)

def compara_times(time1 : Time, time2 : Time) -> Time:
    '''
    Retorna o time com melhor classifição entre *time1* e *time2*,
    com base em quem tem o maior Time.pontos, Time.vit, Time.saldo
    ou se Time.nome é anterior na ordem alfabética
    '''
    top_time = time1
    if time2.nome == time1.nome:
        top_time = time1
    elif time2.pontos > time1.pontos:
        top_time = time2
    elif time2.pontos == time1.pontos:
        if time2.vit > time1.vit:
            top_time = time2
        elif time2.vit == time1.vit:
            if time2.saldo > time1.saldo:
                top_time = time2
            elif time2.saldo == time1.saldo:
                if time2.nome < time1.nome:
                    top_time = time2
    return top_time

def ordena(lst : list[Time], plac : list[Time]) -> None:
    '''
    extrai itens de *lst* e adiciona eles a *placar* de forma ordenada com base
    nos dados de pontos, vitorias, saldo de gols e nome contidos no tipo composto

    Exemplo

    >>> placar = []
    >>> times = [Time('Sao-Paulo, 2, -1, 0, 0, 0, 1), Time('Atletico-MG', 1, 1, 1, 3, 3, 0)]
    >>> ordena(times)
    >>> placar
    [Time('Atletico-MG', 1, 1, 1, 3, 3, 0), Time('Sao-Paulo, 2, -1, 0, 0, 0, 1)]
    '''
    top_time = lst[0]
    j = 0
    time_index = 0
    if len(lst) > 2:
        j = 1
        while j < len(lst):
            top_time = compara_times(top_time, lst[j])
            if top_time == lst[j]:
                time_index = j
            j += 1
        plac.append(top_time)
        remover(lst, time_index)
        ordena(lst, plac)
    else:
        plac.append(top_time)


def gera_placar(lst : list[Time]) -> None:
    '''
    Imprime o placar contido em *lst* exibindo o nome de cada 
    elemento com *nome* ajustado por *ajust_time()*, *pontos*, *vit* e *saldo* 

    Exemplo

    >>> placar = [Time('Atletico-MG', 1, 1, 1, 3, 3, 0), Time('Sao-Paulo, 2, -1, 0, 0, 0, 1)]
    >>> gera_placar(placar)
    Gols        Pontos Vitórias Saldo
    Atletico-MG  3       1      1
    Sao-Paulo    0       0      0
    '''
    maior_nome = tam_max(lst)
    plac = ''
    for t in lst:
        plac = plac + ajust_time(t, maior_nome)
    print('Gols' + ' ' * (maior_nome - 5) + 'Pontos' + ' ' + 'Vitórias' + ' ' + 'Saldo')
    print(plac)

def ajust_time(time : Time, m_nome) -> str:
    '''
    Cria uma string a ser adicionada ao placar, ajustando nome de *time*
    mostrado para que tenha o mesmo numero de caracteres que o nome do
    time de *placar* de maior nome junto com *pontos*, *vit* e *saldo*
    '''
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
    
    t_ajust = time.nome + ' ' * (m_nome - len(time.nome)) + ' ' + pontos +'      ' + vitorias +'     ' + saldo + '\n'
    return t_ajust
    
def tam_max(lst : list[Time]) -> int:
    '''
    Retorna o tamanho da maior string contida no campo de nome dos elementos
    de tipo Time de *lst*
    '''
    m_n = 0
    for n in lst:

        if len(n.nome) > m_n:
            m_n = len(n.nome)
    return m_n

def tam_max_saldo(lst : list[Time]) -> int:
    '''
    Retorna o tamanho em string do maior valor de Time.saldo de *lst*
    '''
    max = 0
    for i in lst:
        if len(str(i.saldo)) > max:
            max = len(str(i.saldo))
    return max

def tam_max_vit(lst : list[Time]) -> int:
    '''
    Retorna o tamanho em string do maior valor de Time.vit de *lst*
    '''
    max = 0
    for i in lst:
        if len(str(i.vit)) > max:
            max = len(str(i.vit))
    return max

def remover(lst : list[Time], idx : int) -> None:
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

def aproveitamento(lst : list[Time]) -> None:
    '''
    Imprime um mensagem no terminal mostrando o elemento de *lst* com o maior
    aproveitamento jogando como anfitrião e a porcentagem de seus pontos como
    anfitrião e o máximo de pontos possíveis como anfitrião

    Exemplo

    >>> placar = [Time('Atletico-MG', 1, 1, 1, 3, 3, 0), Time('Sao-Paulo, 2, -1, 0, 0, 3, 1)]
    >>> aproveitamento(placar)
    O time com o melhor aproveitamento foi o Sao-Paulo, com 100% de aproveitamento
    '''
    m_time = lst[0]
    for i in range(len(lst)):
        if lst[i].pontos_a > m_time.pontos_a:
            m_time = lst[i]
    print('O time com o melhor aproveitamento foi o ' + m_time.nome \
           + ', com ' + str(round((m_time.pontos_a / (m_time.jogos_a * 3))*100, 2)) + \
         '%' + ' de aproveitamento')

def def_menos_vazada(lst : list[Time]) -> None:
    '''
    Imprime uma mensagem no terminal informando qual é o elemento de *lst*
    com o menor valor de gols_r (gols recebidos)

    Exemplo

    >>> placar = [Time('Atletico-MG', 1, 1, 1, 3, 3, 0), Time('Sao-Paulo, 2, -1, 0, 0, 0, 1)]
    >>> def_menos_vazada(placar)
    O time com a defesa menos vazada foi o Atletico-MG com apenas 1 Gol(s) recebido(s)
    '''
    m_time = menos_gols(lst)

    print('O time com a defesa menos vazada foi o ' + m_time.nome\
          + ' com apenas ' + str(m_time.gols_r) + ' Gol(s) recebidos')

def menos_gols(lst : list[Time]) -> Time:
    '''
    retorna o time com menor valor de Time.gols_r
    '''
    time = lst[0]
    if len(lst) == 1:
        time = lst[0]
    else:
        if lst[0].gols_r > menos_gols(lst[1:]).gols_r:
            time = menos_gols(lst[1:])
    return time

if __name__ == '__main__':
    main()