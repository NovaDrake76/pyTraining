m = int(input())
d = int(input())
counter = 0

# gambiarra, vo fazer a formula de fibonacci não 👍
f = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,
     89, 144, 233, 377, 610, 987, 1597, 2584]

i = 1
while counter < m:
    if f[i] % d == 0:
        print(f[i])
        counter += 1
    i += 1
