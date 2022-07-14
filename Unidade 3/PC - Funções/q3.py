# incompleta

N = int(input())

list1 = []
list2 = []

for x in range(0, N):
    if N != 0:
        list1.append(int(input()))

M = int(input())

for x in range(0, M):
    if M != 0:
        list2.append(int(input()))


def verify(p):
    if (p + len(list1)) > len(list2):
        print('N')
    else:
        for i in range(0, list1[-1]):
            x = list1[i-1]
            y = list2[(i+p)-1]
            if x != y:
                print('N')
            print('S')


for i in list1:
    verify(i)
