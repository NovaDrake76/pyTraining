list1 = []
list2 = []
notes1 = []
notes2 = []
progression1 = []
progression2 = []
progression3 = []
N = int(input())


for x in range(N):
 N = int(input())
 list1.append(N)

M = int(input())
for y in range(M):
 M = int(input())
 list2.append(M)

def notas(n):
  if n == 1 or n==8:
    n = 1
  elif n == 2 or n==9:
    n = 2
  elif n == 3 or n == 10:
    n = 3
  elif n == 4 or n == 11:
    n = 4
  elif n == 5 or n == 12:
    n = 5
  elif n == 6 or n == 13:
    n = 6
  elif n ==7 or n == 14:
    n = 7
  return n

for i in list1:
  notes1.append(notas(i)) 

for i in list2:
  notes2.append(notas(i))


for x in notes1:
   anterior = notes1.index(x) -1 
   if x == 1 and notes1[anterior] == 7:
    p = 1
    progression2.append(p)   
   elif notes1.index(x) == 0 or x < notes1[anterior]:
     p = 0
     progression2.append(p)   
   elif x > notes1[anterior]:
    p = x - notes1[anterior]   
    progression2.append(p)
   elif x == notes1[anterior]:
    p = 1
    progression2.append(p)

for x in notes2:
   anterior = notes2.index(x) -1     
   if notes2.index(x) == 0 or x < notes2[anterior]:
     p = 0
     progression3.append(p)   
   elif x > notes2[anterior]:
    p = x - notes2[anterior]   
    progression3.append(p)
   elif x == notes2[anterior]:
    p = 1
    progression3.append(p)

if progression2 == progression3:
  print('S')
else:
  print('N')