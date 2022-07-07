# questão repetida?

N = int(input())

montains = []
montainsAux = []

for x in range(0, N):
    inputed = int(input())
    montains.append(inputed)
    montainsAux.append(inputed)

P = int(input())
current = montainsAux[P]
montainsAux.sort()
shortest = montainsAux[0]

print(montains.index(shortest))
