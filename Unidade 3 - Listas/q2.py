# pesquisa

anwser = ''
total = 0

votes = {
    'Windows': 0,
    'Unix': 0,
    'Linux': 0,
    'Netware': 0,
    'MacOS': 0,
    'Outro': 0,
}

while anwser != 0:
    anwser = int(input())
    for i, x in enumerate(votes):
        if anwser == i+1:
            votes[x] += 1
            total += 1

for i in votes:
    if votes[i] == 1:
        print(i + ', ' + str(votes[i]) + " voto, " +
              str(int(round(votes[i]/total*100, 2))) + "%")
    elif votes[i] > 1:
        print(i + ', ' + str(votes[i]) + " votos, " +
              str(int(round(votes[i]/total*100, 2))) + "%")

print("Total: " + str(total) + " votos")

votesMaxValue = max(votes.items(), key=lambda x: x[1])

winners = []
for key, value in votes.items():
    if value == votesMaxValue[1]:
        winners.append(key)

for i in winners:
    print("Vencedor: " + i + " com " +
          str(int(round(votes[i]/total*100, 2))) + "% dos votos ")