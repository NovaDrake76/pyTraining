# O bônus mensal de uma empresa é divido com seus colaboradores em função da posição
# que eles possuem no organograma da empresa. Há apenas 3 postos: os funcionários,
# os gerentes de projeto e o diretor executivo (CEO). Os gerentes de projeto recebem
# o dobro do bônus dos funcionários e o diretor executivo recebe o dobro dos gerentes
# de projeto. Escreva um programa para calcular o valor do bônus do CEO a partir do
# valor do bônus total a ser partilhado e o número de funcionários e gerentes de projeto.

# Entrada
# Seu programa deve ler 3 números inteiros B, F e G, representando respectivamente o
# valor do bônus total a ser partilhado (B), o número de funcionários da empresa (F)
# e o número de gerentes de projeto (G).

# Saída
# Seu programa deve enviar para a saída (imprimir) um único número inteiro indicando
# o valor do bônus do CEO.

B = int(input())
F = int(input())
G = int(input())

bonusCEO = int((B/(F + (G*2) + 4))*4)

print(bonusCEO)
