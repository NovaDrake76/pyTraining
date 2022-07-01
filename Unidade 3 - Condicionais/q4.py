# QUESTÃO INCOMPLETA

color = input()

inputs = {
    "P("+color+")": 0,
    "M("+color+")": 0,
    "G("+color+")": 0,
}

stock = {
    "P(A)": 10,
    "M(A)": 7,
    "G(A)": 5,
    "P(V)": 12,
    "M(V)": 5,
    "G(V)": 4
}

colors = ['A', 'V']

for i in inputs:
    inputs[i] = int(input())

sizes = ["P", "M", "G"]


for size in sizes:
    if stock[size+'(' + color + ')'] >= inputs[size + '(' + color + ')']:
        print(str(size+'(' + color + '):') +
              str(stock[size+'(' + color + ')'] - inputs[size+'(' + color + ')']))
    else:
        print(size+'(' + color + '):' + str(stock[str(size)+'(' + color + ')']
                                            ) + ' - "Quantidade não disponível"')
