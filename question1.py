# Você foi chamado para integrar a equipe de desenvolvimento da FIA (Federação Internacional de Automobilismo).
# Os softwares desenvolvidos por sua equipe são responsáveis por monitorar o tempo dos carros a cada volta,
# seja durante a corrida ou na tomada de tempo nas classificações para as largadas.
# Durante uma corrida, a FIA divulga vários dados, entre eles a diferença de tempo entre os carros ou entre
#  um carro em particular. Você foi solicitado para escrever o programa desse último dado. Eles querem que
# você escreva um programa que receba o tempo total de cada carro (em segundos) contabilizado até a última
# volta e envie para saída quantos segundos cada carro se encontra à frente do último colocado.

# Entrada
# Seu programa deve ler inicialmente um número inteiro N, que indica o número de carros em uma corrida,
# seguido de N valores inteiros, representando o tempo total em segundos dos N carros na corrida.

# Saída
# Seu programa deve enviar para a saída (imprimir) N valores inteiros, indicando quantos segundos cada
# carro se encontra à frente do último colocado. Os dados de saída devem seguir a mesma ordem dos carros nos dados de entrada.

N = input()

speeds = []
for x in range(0, int(N)):
    speeds.append(input())

biggest = max(speeds)
