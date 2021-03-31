# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
print('#' * 30)
print(f'{"Vamos jogar par ou ímpar?":^30}')
print('#' * 30)
count = 0

while True:
    c = '  '
    while c not in 'PI':
        c = str(input('\nPar ou ímpar? [P/I] ')).strip().upper()[0]

    user = int(input('Escolha um número: '))

    comp = randint(0, 10)
    print('\n', user, '+', comp, '=', user + comp)

    if c == 'P':
        if (comp + user) % 2 == 0:
            count += 1
            print('Par, você ganhou!!!')
        else:
            print('Ímpar, você perdeu!')
            break

    if c == 'I':
        if (comp + user) % 2 == 1:
            count += 1
            print('Ímpar, você ganhou.')
        else:
            print('Par, você pedeu!')
            break
print(f'GAME OVER...\nVocê venceu {count} vezes!')
