# Agora que você entrou no BTI, começaram a aparecer oportunidades de trabalho em várias frentes. Uma delas é na área de
# jogos, sua grande paixão. Porém, seu primeiro trabalho não foi beeeemmm como você pensou. Enquanto você achava que ia
# começar trabalhando com gráficos, personagens e tudo mais... te colocaram para fazer análise de dados das partidas
# (você não sabia o quanto isso era importante...)

# Sua primeira tarefa foi organizar o tempo gasto por um jogador em períodos de tamanho fixo. Assim, seu programa poderá,
# por exemplo, ler dados de um ano inteiro e fazer relatórios mensais (período de 30 dias), semanais (7 dias) ou outro
# período qualquer. Os dados lidos são diários e representam o tempo de uso do jogo, podendo ser 0 se o jogador não usar
# o jogo no dia correspondente. Seu programa deverá fornecer, para cada período, o total do tempo jogado e quantos dias o jogador usou o jogo.

# Entrada
# Seu programa deverá ler inicialmente um número inteiro P que indica a quantidade de períodos do relatório. Em seguida,
# deverá ler outro número inteiro D, que indica a quantidade de dias de cada período. Por fim, seu programa deverá ler
# P x D valores inteiros, que representam o tempo de jogos em cada um dos dias.

# Saída
# Seu programa deve enviar para a saída padrão (imprimir), para cada período, duas linhas. A primeira deverá estar no
# formato "TEMPO DE JOGO: t", onde t é a soma dos tempos de jogo no período. A segunda deverá estar no formato
# "DIAS DE JOGO: d", onde d é a quantidade de dias em que o jogador fez uso do jogo. Após cada período, seu programa
# deverá imprimir uma nova linha com "-".
# Obs: Há um (e apenas um) espaço em branco entre o caractere ":" e o valor inteiro seguinte.

P = int(input())
D = int(input())

gamesTime = []
alltimes = int(P * D)

for x in range(0, alltimes):
    gamesTime.append(int(input()))

for y in range(1, P+1):
    daysGaming = (gamesTime[(y-1) * D: (y*D)])
    sumOfTimes = sum(daysGaming)
    print("TEMPO DE JOGO: " + str(sumOfTimes))

    i = int(0)
    for z in daysGaming:
        if(z > 0):
            i = i+1

    print("DIAS DE JOGO: " + str(i))
    print("-")
