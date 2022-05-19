# Você entrou em um projeto de iniciação científica voltado a elaborar algoritmos seguros para
# carros autônomos. Por enquanto, a equipe realiza apenas testes/simulações em um ambiente
# virtual e estão interessados em definir um algoritmo que faça o carro dirigir em segurança
# entre dois outros carros. Sua tarefa inicial é desenvolver um programa que indique se um carro
# deve acelerar ou frear em função da distância que se encontra de dois outros carros.
# O ambiente virtual em questão simula uma estrada reta, sem curvas, onde a posição de um carro
# é definida por um único valor, que indica a distância do carro ao início da estrada. Nessa
# simulação, não é possível ter dois carros na mesma posição (dois corpos não ocupam o mesmo local ao mesmo tempo!).

# Seu programa deve indicar para o carro que ele controla para acelerar se houver um carro atrás
# e outro na frente e se o detrás estiver mais próximo do que o da frente. Se for o carro da
# frente que estiver mais próximo, então deve-se mandar frear. Porém, se os carros estiverem
# equidistantes do carro controlado por seu programa ou se ambos estiverem à frente ou atrás,
# seu programa deve indicar para continuar na mesma velocidade (nem acelerar nem frear).

C = int(input())
C1 = int((input()))
C2 = int((input()))

R1 = C1 - C
R2 = C - C2

if((C > C1 and C > C2) or (C < C1 and C < C2)):
    print("C")
elif(R1 > R2):
    print("A")
elif(R2 > R1):
    print("F")
