import math

initial = int(input())
tax = float(input())
months = int(input())

for i in range(0, months):
    if i != 0:
        print("-")
    print("mês:", i+1)
    print("saldo anterior:", ("{:.2f}".format((math.floor(initial * 10 ** 2) / 10 ** 2))))
    print("juros mês:", "{:.2f}".format((math.floor(((initial * tax)/100) * 10 ** 2) / 10 ** 2)))
    print("novo saldo:", "{:.2f}".format(math.floor((initial + (initial * tax)/100) * 10 ** 2) / 10 ** 2))

    initial = (initial + (initial * tax)/100)
