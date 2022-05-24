# Alfredo, Bianca e Clarissa são sócios de uma startup que está começando a dar certo. Eles possuem diferentes
# participações no capital da empresa e, portanto, recebem diferentes percentuais dos lucros. Alfredo
# possui 40% da sociedade, Bianca 50% e Clarissa 10%.
# Faça um programa para calcular a divisão dos valores, dado o lucro de um mês.

# Entrada
# Seu programa deve ler um número inteiro N com o valor do lucro do mês corrente.

# Saída
# Seu programa deve enviar para a saída (imprimir) três números inteiros correspondendo aos valores
# a serem partilhados com Alfredo, Bianca e Clarissa, respectivamente.

N = int(input())

print(int(N*0.4))
print(int(N*0.5))
print(int(N*0.1))
