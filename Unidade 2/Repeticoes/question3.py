# O volume de chuvas do último verão do foi muito acima da média, pelo menos no Nordeste. Aqui em Natal,
# por exemplo, choveu um volume  de 425,3mm no verão 2021/2022, enquanto a média é de 181mm. Só na noite
# de 5 para 6 de março de 2022 choveu 119,1 mm, o que representa mais da metade da média prevista para todo
# o verão (fonte: https://www.climatempo.com.br/noticia/2022/03/24/balanco-de-chuva-do-verao-2021-2022-nas-capitais-brasileiras-4633).
# Essa chuva, em particular, fez inundar os estacionamentos de alguns condomínios, muros caíram, ruas foram inundadas
# e casas invadidas pela água por todas as regiões da cidade.

# Um dos afetados por essas chuvas volumosas é um grande amigo seu. Sua casa fica em uma área que parece chover mais
# que as demais, pelo menos é o que ele diz. Muitas vezes quando vocês estão na praia curtindo um sol, ele se vira é
# diz: "deve estar chovendo lá em casa agora". Mas não dá pra saber se realmente chove mais na casa dele do que, por
# exemplo, na sua se vocês não fizerem um teste: comparar o volume de chuva em cada uma das casas durante um determinado período.

# Você propôs esse teste com seu amigo. Cada um vai colocar no telhado da casa um tubo de PVC (de mesmo diâmetro em
# ambas as casas) para coletar a água da chuva. Todos os dias irão ver quantos cm de água foram coletados durante o dia
# e esvaziá-los para uma nova coleta no dia seguinte. Ao final de um determinado período, vocês vão juntar esses dados
# para ver qual área teve um maior volume de chuvas. Para facilitar a comparação, escreva um programa para receber os
# dados coletados nas duas casas e indique em que casa choveu mais.

# Entrada
# Seu programa deve ler inicialmente um número inteiro N, que indica quantos dias os dados foram coletados. Em seguida,
# seu programa irá ler N valores inteiros correspondentes aos centímetros de água coletada ao longo dos N dias em uma das
# casas, referenciada no seu programa por "CASA A". Depois, seu programa irá ler novamente N valores inteiros correspondentes
# aos centímetros de água na outra casa, referenciada por "CASA B".

# Saída
# Seu programa deve enviar para a saída padrão (imprimir) a referência da casa que recebeu o maior volume de chuva durante
# o período em questão, podendo imprimir então "CASA A" ou "CASA B", se uma teve um volume d'água maior que a outra,
# ou "IGUAL", se o volume d'água for o mesmo em ambas.

N = int(input())
CASA_A = []
CASA_B = []

for x in range(0, N):
    CASA_A.append(int(input()))

for y in range(0, N):
    CASA_B.append(int(input()))

A_sum = sum(CASA_A)
B_sum = sum(CASA_B)

if(A_sum > B_sum):
    print("CASA A")
elif(A_sum < B_sum):
    print("CASA B")
else:
    print("IGUAL")
