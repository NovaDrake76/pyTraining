# essa tá foda

x0 = int(input())
y0 = int(input())
x1 = int(input())
y1 = int(input())

n = int(input())

objects = []

for i in range(0, n):
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    objects.append({(a, b, c, d): i})

print(objects)
