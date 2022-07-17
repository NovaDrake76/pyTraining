toRender = []
boundingbox = [
   (int(input()),int(input())),
   (int(input()),int(input()))
]

def fullR(list1):
   list1.append((list1[0][1], list1[1][0]))
   list1.append((list1[0][0], list1[1][1]))

   return list1

def Render(R):

   for position in R:
      if position[0] >= boundingbox[3][0] and position[0] <= boundingbox[1][0]:

         if position[1] <= boundingbox[0][1] and position[1] >= boundingbox[3][1]:
            return True

   if R[0][1] >= boundingbox[0][1] and R[3][1] <= boundingbox[3][1]:
      if R[3][0] >= boundingbox[3][0] or R[1][0] <= boundingbox[1][0]:
         return True

      if R[3][0] <= boundingbox[3][0] and R[1][0] >= boundingbox[1][0]:
         return True

   if R[3][0] <= boundingbox[3][0] and R[1][0] >= boundingbox[1][0]:
      return False

   return False

boundingbox = fullR(boundingbox)
NR = int(input())

for i in range(NR):
   x0 = int(input())
   y0 = int(input())

   x1 = int(input())
   y1 = int(input())

   R = [(x0, y0), (x1, y1)]
   R = fullR(R)

   if Render(R) == True:
      toRender.append(f'{x0} {y0} {x1} {y1}')
for r in toRender:
   print(r)