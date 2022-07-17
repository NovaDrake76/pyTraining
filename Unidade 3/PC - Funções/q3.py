A = []
B = []
N = int(input())


for x in range(N):
 N = int(input())
 A.append(N)

M = int(input())
for y in range(M):
 M = int(input())
 B.append(M)

def sequence(p):
  if p + len(A) > len(B):
   return False
  TA = len(A) - 1
  for i in A:
   x = A[A.index(i)]
   y = B[A.index(i) + p]
   if y != x:
    return False
    
    
  return True
     
  

for b in range(len(B)):
 sequence(b)
 if sequence(b) == True:
   print("S")
   break

if sequence(b) == False:
  print('N')
