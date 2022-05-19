# Enquanto você entrou na UFRN no Bacharelado em TI, vários de seus amigos e amigas
# entraram em outros cursos, entre eles o curso de Design. Uma das primeiras tarefas
# no curso de Design foi projetar um Móbile (como o ilustrado abaixo).

# O problema é que é difícil definir as peças e materiais de forma que o móbile
# fique equilibrado... e não fique pendendo para um lado só. Seus amigos agora estão
# tendo uma grande dificuldade e pediram sua ajuda para escrever um programa que simule
# o móbile e diga, antecipadamente, se ele ficará em equilíbrio ou não. A ideia é que
# se tenha uma peça como ilustrada abaixo (imagina ae).
# Você percebe, então, que serão necessárias 4 peças (A, B, C e D), que podem ser
# construídos com materiais diferentes e eventualmente ter pesos diferentes. Porém,
# seus pesos vão atender obrigatoriamente as seguintes equações:

#     A = B + C+ D
#     D = B + C
#     B = C

# Escreva um programa que verifique se, dados os pesos de 4 peças, elas poderão ou não ser montadas como o móbile acima.

# Entrada
# Seu programa deve ler 4 números inteiros A, B, C e D, representando respectivamente os pesos das peças A, B, C e D indicadas na figura.

# Saída
# Seu programa deve enviar para a saída (imprimir) "S" se eles entrarão em equilíbrio ou "N" se não entrarão.

A = int(input())
B = int(input())
C = int(input())
D = int(input())

balance = 'S'

if(B != C or D != (B + C) or A != (B + C + D)):
    balance = 'N'

print(balance)
