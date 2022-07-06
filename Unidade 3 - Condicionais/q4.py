color = input()

inputs = {
    "P(A)": 0,
    "M(A)": 0,
    "G(A)": 0,
    "P(V)": 0,
    "M(V)": 0,
    "G(V)": 0
}

for i in ["P(" + color + ")", "M(" + color + ")", "G(" + color + ")"]:
    inputs[i] = int(input())

stock = {
    "P(A)": 10,
    "M(A)": 7,
    "G(A)": 5,
    "P(V)": 12,
    "M(V)": 5,
    "G(V)": 4
}

sizes = ["P", "M", "G"]

for colors in ['A', 'V']:
    for size in sizes:
        if colors == color:
            if stock[size+'(' + color + ')'] >= inputs[size + '(' + color + ')']:
                print(str(size+'(' + colors + '):') +
                      str(stock[size+'(' + colors + ')'] - inputs[size+'(' + color + ')']))
            else:
                print(size+'(' + colors + '):' +
                      str(stock[str(size)+'(' + colors + ')']) + ' - "Quantidade não disponível".')
        else:
            print(size+'(' + colors + '):' +
                  str(stock[str(size)+'(' + colors + ')']))
