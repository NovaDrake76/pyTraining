# O clima afeta inúmeras atividades econômicas, desde a agricultura às atividades de TI. Muitos profissionais
# de TI precisam, por precaução, dar uma pausa em seus trabalhos quando o céu começa a trovejar e soltar suas
# descargas elétricas (principalmente quando estão em home-office). O medo dessas descargas causarem avarias
# nas nossa ferramenta de trabalho é justificada!

# Este ano foi especial nesse sentido. Para você ter uma ideia, nos 3 primeiros meses de 2022, o RN foi atingido
# por cerca de 50 mil descargas atmosféricas (raios) causando pouco menos de 1.500 interrupções de energia, quase
# o dobro das interrupções do ano passado inteiro
# (fonte: http://www.tribunadonorte.com.br/noticia/rn-ja-foi-atingido-por-mais-de-50-mil-raios-em-2022-veja-orientaa-a-es-de-segurana-a/535441).
#  Esses dados são pro RN inteiro... mas você é mais afetado pelos raios que caem "perto da sua porta". Uma
# estimativa do número de raios próximos à sua casa seria melhor que o do estado todo.

# Você ouviu falar de uma API de dados (serviço de troca de dados entre sistemas) que fornece um histórico dos
# raios que ocorreram um determinado período. O interessante dessa API é que é possível passar coordenadas
# (longitude e latitude) e ele retorna as distâncias dos raios para elas. Ou seja, você pode fazer uma consulta
# passando as coordenadas de sua casa! Escreva, então, um programa que irá receber as distâncias fornecidas pela
# API e contar quantos raios ocorreram dentro de uma dada distância da sua casa.

# Entrada
# Seu programa deve ler inicialmente um número inteiro D, que indica a distância máxima que você considera "próximo"
# à sua residência. Em seguida, seu programa deve ler outro número inteiro N, que indica a quantidade de raios
# fornecidos pela API, seguido de N valores inteiros correspondente às distâncias de cada raio da sua casa.

# Saída
# Seu programa deve enviar para a saída padrão (imprimir) o número de raios que caíram próximo à sua residência.

D = int(input())

N = int(input())
lightnings = []

for x in range(0, N):
    ray = (int(input()))
    if(ray <= D):
        lightnings.append(ray)

print(len(lightnings))
