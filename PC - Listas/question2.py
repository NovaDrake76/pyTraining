# A Superintendência de Tecnologia da Informação da UFRN (STI) quer fazer algumas modificações
# no SIGAA inspiradas no modelo de gamificação do Duolingo, com alguns rankings e competições
# semanais sobre as atividades que os professores passam. Eles querem permitir inicialmente que
# o aluno veja se a pontuação conquistada nas atividades está acima ou abaixo da média da turma,
# estimulando quem se encontra com uma pontuação abaixo da média fazer mais atividades, conquistar
# mais pontos e, com isso, passar para o grupo que está acima da média.
# A STI sabe que você entrou no BTI e pede para você contribuir para a nova versão do SIGAA
# escrevendo um programa que informa quais as pontuações que se encontram acima da média de uma lista de pontuações.

# Entrada
# Seu programa deverá ler um valor inteiro N, indicando o tamanho da turma, seguido de N valores
# inteiros, cada um representando a pontuação de um dos alunos da turma.

# Saída
# Seu programa deverá enviar para a saída padrão (imprimir) as pontuações que forem maiores que a
# média das N pontuações lidas. Se não houver pontuação acima da média, seu programa deverá imprimir "-".

N = int(input())

scores = []

for x in range(0, N):
    scores.append(int(input()))

average = sum(scores) / len(scores)

greatScores = []

for y in scores:
    if(y > average):
        greatScores.append(y)

if greatScores:
    for z in greatScores:
        print(z)
else:
    print("-")
