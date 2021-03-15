# Crie um programa que faça o computador jogar Jokenpô com você
from random import randint
from time import sleep
jogador = int(input('''Escolha uma opção:
[1] pedra
[2] papel
[3] tesoura
Opção escolhida: '''))
computador = randint(1, 3)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('=' * 30)
if jogador == 1:
    print('Você escolheu PEDRA')
    if computador == 1:
        computador = 'PEDRA'
        resultado = 'EMPATE'
    elif computador == 2:
        computador = 'PAPEL'
        resultado = 'VOCÊ PERDEU!'
    elif computador == 3:
        computador = 'TESOURA'
        resultado = 'VOCÊ GANHOU!!!'
    print('O computador escolheu {}. \n{:^30}'.format(computador, resultado))
elif jogador == 2:
    print('Você escolheu PAPEL.')
    if computador == 1:
        computador = 'PEDRA'
        resultado = 'VOCÊ VENCEU!!!'
    elif computador == 2:
        computador = 'PAPEL'
        resultado = 'EMPATE!'
    elif computador == 3:
        computador = 'TESOURA'
        resultado = 'VOCÊ PERDEU!'
    print('O computador escolheu {}. \n{:^30}'.format(computador, resultado))
elif jogador == 3:
    print('Você escolheu TESOURA.')
    if computador == 1:
        comcomputador = 'PEDRA'
        resultado = 'VOCÊ PERDEU!!!'
    elif computador == 2:
        computador = 'PAPEL'
        resultado = 'VOCÊ VENCEU!'
    elif computador == 3:
        computador = 'TESOURA'
        resultado = 'EMPATE!'
    print('O computador escolheu {}. \n{:^30}'.format(computador, resultado))
else:
    print('Opção inválida.')
print('=' * 30)