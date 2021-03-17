# Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva
# para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
import emoji
from time import sleep
print('Contagem regressiva!!!')
for r in range(10, -1, -1):
    print(r)
    sleep(1)
print(emoji.emojize(':fireworks:'))
