# calcular idade

from datetime import datetime

birth = int(input())

now = currentYear = datetime.now().year

age = now - birth
print(str(age) + ' anos')

if(age >= 18):
    print('Pode votar e dirigir')
elif(age >= 16):
    print('Pode votar e não pode dirigir')
else:
    print('Não pode votar e não pode dirigir')
