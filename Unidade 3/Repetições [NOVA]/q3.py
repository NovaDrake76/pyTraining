n = int(input())
divisors = []

for i in range(1, n+1):
    if n % i == 0:
        divisors.append(i)

divisors.pop()
total = sum(divisors)

if total == n:
    print("número perfeito")
else:
    print("número não é perfeito")
