# Você vai integrar o suporte de uma equipe automobilística da Fórmula E
# (carros elétricos). A primeira missão que te passaram é desenvolver um programa
# para estimar em quantas voltas um carro irá alcançar o outro. Você não tem acesso
# à velocidade dos carros, mas a diferença em segundos dos carros no ponto de largada
# (ex: um carro está 10s à frente do outro) e o quanto essa diferença está caindo,
# em média, a cada volta (ex: de uma volta para a outra, um carro reduz em média a diferença em 2s).

# Entrada
# Seu programa deve ler 2 números inteiros D e M, representando respectivamente a
# diferença atual dos carros em questão (D) e o quanto essa diferença está sendo
# reduzida em média a cada volta (M). Ambos valores estão em segundos e serão sempre valores positivos maiores que 0.

# Saída
# Seu programa deve enviar para a saída (imprimir) um único número inteiro indicando
# o número mínimo de voltas necessárias para um carro alcançar o outro.

D = int(input())
M = int(input())

resto = D % M

if(resto > 0):
    print(int((D/M)+1))
else:
    print(int(D/M))
