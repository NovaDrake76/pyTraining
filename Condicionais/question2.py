# O Restaurante Universitário (RU) da UFRN reabriu recentemente. Porém, em razão
# da restrição de ocupação definida nos protocolos de Biossegurança da Universidade, o RU não
# consegue oferecer a mesma quantidade de refeições diárias que oferecia antes
# da pandemia (cerca de 4.500 refeições/dia). Por causa disso, a Pró-Reitoria
# de Assuntos Estudantis (Proae) vai fornecer um auxílio alimentação aos estudantes
# carentes contemplados no edital de acesso ao RU. Porém, o valor que a universidade
# com esse propósito também é limitado. É possível que o valor do auxílio definido para
# os alunos contemplados ultrapasse o valor que a universidade recebe para esse propósito.
# Para fazer uma estimativa, a Pró-reitoria solicitou pra você um programa que indique
# se os recursos recebidos são suficientes ou não para um determinado valor de auxílio e uma determinada quantidade de alunos.

R = int(input())
A = int(input())
N = int(input())

foodForEveryone = 'S'

totalToSpent = A*N

if(totalToSpent > R):
    foodForEveryone = 'N'

print(foodForEveryone)
