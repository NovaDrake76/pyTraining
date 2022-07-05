# notas

# biblioteca pra achar a média mais facilmente
import statistics

names = []
notas = []
acimaDaMedia = []

# colocando os nomes e notas nas listas
for x in range(0, 5):
    names.append(input())
    notas.append(int(input()))

# calculando a média e imprimindo
median = statistics.fmean(notas)
print("Média: " + str(median))

# verificando quais nomes possuem notas acima da média
for i in names:
    # se a nota na posição do nome for maior que a média, colocar na lista
    # (fiz assim porque se eu fosse usar o index de notas, notas iguais mostrariam o nome de somente uma pessoa)
    if notas[names.index(i)] > median:
        acimaDaMedia.append(i)

print("Acima da média: " + ','.join(acimaDaMedia))

# achando a maior nota
biggest = int(notas.index(max(notas)))
print("Maior nota: " + names[biggest])
