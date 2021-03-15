# Crie um programa que faça o computador jogar Jokenpô com você
from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA') #modulos
computador = randint(0, 2)
jogador = int(input('''Escolha:
[0] PEDRA
[1] PAPEL
[2] TESOURA
Sua opção: '''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
if jogador <= 2:
    print('-' * 30)
    print('Você escolheu {}.'.format(itens[jogador]))
    print('O computador escolheu {}.'.format(itens[computador]))
    print('-' * 30)
    if jogador == 0: # PEDRA
        if computador == 0: # PEDRA
            print('EMPATE!!!')
        elif computador == 1: # PAPEL
            print('VOCÊ PERDEU :(')
        elif computador == 2: # TESOURA
            print('VOCÊ GANHOU \o/')
    elif jogador == 1: # PAPEL
        if computador == 0: # PEDRA
            print('VOCÊ GANHOU \o/')
        elif computador == 1: # PAPEL
            print('EMPATE!!!')
        elif computador == 2: # TESOURA
            print('VOCÊ PERDEU :(')
    elif jogador == 2: # TESOURA
        if computador == 0: # PEDRA
            print('VOCÊ PERDEU :(')
        elif computador == 1: # PAPEL
            print('VOCÊ GANHOU \o/')
        elif computador == 2: # TESOURA
            print('EMPATE!!!')
else:
    print('Você digitou uma opção inválida :/')
