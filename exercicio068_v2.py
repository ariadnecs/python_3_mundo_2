# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
v = 0
while True:
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('\nPar ou ímpar? [P/I] ')).upper()


    user = int(input('Digite um valor: '))
    comp = randint(0, 10)
    tot = user + comp

    print(f'Você jogou {user} e o computador {comp}.\nTotal {tot}\n')

    if tipo == 'P':
        if tot % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você perdeu! :(')
            break
    elif tipo == 'I':
        if tot % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você perdeu.')
            break
print(f'\nGAME OVER. Você venceu {v} vezes.')
