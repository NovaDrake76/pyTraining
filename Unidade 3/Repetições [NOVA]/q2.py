# codigo do professor não tá calculando acima de 2 decimais, não sei como ajeitar

initial = int(input())
tax = float(input())
months = int(input())

for i in range(0, months):
    if i != 0:
        print("-")
    print("mês:", i+1)
    print("saldo anterior:", ("{:.2f}".format((initial))))
    print("juros mês:", ("{:.2f}".format((initial * tax)/100)))
    print("novo saldo:", ("{:.2f}".format(initial + (initial * tax)/100)))

    initial = (initial + (initial * tax)/100)
