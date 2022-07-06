a = []
b = []

for x in range(0, 5):
    a.append(int(input()))

for y in range(0, 5):
    b.append(int(input()))

c = a + b
c.sort()

print(*c)
