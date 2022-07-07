# Recentemente, há uma grande discussão em torno da lei que libera o uso comercial de alguns jogos
# de azar no Brasil, aprovada pela Câmera dos Deputados e em trâmite no Senado. Entre os jogos de
# azar, encontra-se o Bingo. Sim... aquele que seus avós costumam jogar nos sábados... o mesmo que
# algumas igrejas usam para arrecadar dinheiro para obras... o mesmo utilizado para trocar políticos
# na Itália medieval (bem.... nesse último caso, não é exatamente o mesmo, mas parecido).

# Com a possibilidade do uso comercial do Bingo ser aprovado, alguns empresários já começaram a se
# organizar para implantar e espalhar seus bingos Brasil afora. Eles precisam de sistemas que verifiquem
# automaticamente as cartelas dos participantes e informe se alguém ganhou ("Bingo!") ou não. Um desses
# empresário pediu sua ajuda para implantar o sistema. Escreva um programa que, dada uma sequência de
# valores presentes numa cartela e uma sequência de valores sorteados, informe se a houve Bingo ou não.

# Entrada
# Seu programa deve ler inicialmente um número inteiro N seguido de N valores inteiros, que são os valores
# da cartela. Depois, seu programa deve ler um número inteiro M, seguido de M valores inteiros, que são os
# valores sorteados. Não há valores repetidos nem na primeira nem na segunda sequência.

# Saída
# Seu programa deve enviar para a saída (imprimir) o texto BINGO se todos os N valores da primeira sequência
# fornecida na entrada estiverem presentes na segunda sequência. Se não estiverem, o programa deve enviar
# para a saída o texto INCOMPLETO.

cartela = []
bingo = []
win = True

N = int(input())

for x in range(0, N):
    cartela.append(int(input()))

M = int(input())

for y in range(0, M):
    bingo.append(int(input()))

for z in cartela:
    if(z not in bingo):
        win = False

if(win):
    print('BINGO')
else:
    print('INCOMPLETO')
