
color = input()
p = int(input())
m = int(input())
g = int(input())

stock = dict([('p', 10), ('m', 7), ('g', 5)], [('p', 10), ('m', 7), ('g', 5)])

pStockA = (10)
mStockA = (7)
gStockA = (5)
pStockV = (12)
mStockV = (5)
gStockV = (4)

if(color == 'A'):
    globals()[pStock+color] = (pStockA - p)
    mStockA = (pStockA - m)
    gStockA = (pStockA - g)
    for i in [pStockA, mStockA, gStockA, pStockV, mStockV, gStockV]:
        if(int(i) < 0):
            print('quantidade não disponível')
        else:
            print(i)

else:
    pStockV = (12 - p)
    mStockV = (5 - m)
    gStockV = (4 - g)
    for i in [pStockV, mStockV, gStockV, pStockA, mStockA, gStockA]:
        if(int(i) <= 0):
            print('quantidade não disponível')
        else:
            print(i)
