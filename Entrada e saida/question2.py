# Você está muito contente com seu primeiro trabalho remunerado. É uma bolsa de iniciação
#  (IC) em um projeto no valor de R$ 400. Não é muito, mas se você conseguir reservar um
#  percentual desse valor todo mês, no final do projeto você terá (talvez) uma boa quantia para investir em algo que sempre desejou.
# Faça então um programa para simular quanto você terá após um determinado número de meses
# de projeto, em função do percentual que você irá reservar todo mês.
# Obs: nesse cálculo, desconsidere ganhos com investimento ou perdas com a inflação.

# Entrada
# Seu programa deve ler 2 números inteiros P e M, representando respectivamente o percentual
# da bolsa que você irá reservar a cada mês (P) e o número de meses que você ficará reservando (M).

# Saída
# Seu programa deve enviar para a saída (imprimir) um único número inteiro indicando o valor
# do total de quanto você terá ao final dos M meses.

P = int(input())
M = int(input())

print(int((M*400)*(P/100)))
