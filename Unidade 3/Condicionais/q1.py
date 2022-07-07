# jokenpo game

hand1 = input()
hand2 = input()

if hand1 == hand2:
    print('empate')
elif hand1 == 'pedra':
    if hand2 == 'tesoura':
        print('Jogador 1 venceu')
    else:
        print('Jogador 2 venceu')
elif hand1 == 'papel':
    if hand2 == 'pedra':
        print('Jogador 1 venceu')
    else:
        print('Jogador 2 venceu')
elif hand1 == 'tesoura':
    if hand2 == 'papel':
        print('Jogador 1 venceu')
    else:
        print('Jogador 2 venceu')
