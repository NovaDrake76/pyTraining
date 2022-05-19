# Em novembro de 2021, a Netflix lançou o documentário "14 Montanhas, 8 Mil Metros e 7 Meses".
# Ele descreve a jornada de Nimsdai Purja, um montanhista nepalês que, em apenas 7 meses,
# escalou os 14 picos mais altos do mundo (todos com mais de 8.000m de altitude). Uma façanha
# incrível e sobre-humana.

# Esse documentário despertou a atenção de outros montanhistas, inclusive um amigo seu que
# já escalou até o Pico do Cabugi! Afinal, como ele mesmo disse: "pra quem sobe o Cabugi,
# esses 14 são fichinhas". Seu amigo quer ficar famoso e fazer a mesma empreitada de Nimsdai
# Purja. Porém, ele não sabe por qual pico começar nem pra qual pico ir depois... e pede sua ajuda.

# Ele quer que você faça um programa para saber qual o próximo pico a ir depois de ter escalado
# um. Em outras palavras, ele quer saber qual o menor custo de ir do topo de um pico a outro,
# considerando que ele deve descer para a base do pico em que se encontra, se deslocar para a
# base do pico seguinte e escalar até seu topo.

# Como primeiro protótipo do seu sistema, você abstrai as distâncias verdadeiras entre os picos
# e cria um modelo em que os picos são definidos em sequência, cada um com sua altitude. O custo
# do deslocamento entre dois picos é calculado então com base nas altitudes de cada pico e a distância
# entre suas bases, na sequência. Como subir e descer de uma montanha é mais custoso que ir de uma
# base a outra, no seu modelo o custo de subir e descer de um pico é definido por 10x a altitude do
# pico. Assim, o custo entre os topos dos picos A e B da figura abaixo é definida por 10 vezes a altitude
# de A mais 10 vezes a altitude de B mais a distância D.
# Considerando que a distância entre as bases de dois picos consecutivos é de 10km, escreva um programa
# que, dado o topo de um pico,  informe qual o topo de pico mais próximo (é o que o seu amigo deve ir em seguida).

# https://i.imgur.com/qUj5g01.png

# Entrada
# Seu programa deve ler inicialmente um número inteiro N seguido de N valores inteiros, cada um
# correspondendo a altitude em metros de um pico na sequência de picos. Depois, seu programa deve
# ler um valor inteiro P indicando o índice do pico que o montanhista se encontra.

# Saída
# Seu programa deve enviar para a saída (imprimir) o índice do topo de pico mais próximo, diferente
# daquele em que o montanhista se encontra.

N = int (input ()) 
 
montains =[] 
montainsAux =[] 
 
for x in range (0, N):
  inputed = int (input ()) 
  montains.append (inputed) 
  montainsAux.append (inputed) 
  
P = int (input ()) 
current = montainsAux[P] 
montainsAux.sort () 
shortest = montainsAux[0] 
     
print (montains.index (shortest))