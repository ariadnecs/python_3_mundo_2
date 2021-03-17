# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
div = 0
primo = int(input('Digite um número: '))
print('O número {} é divisível por: '.format(primo), end='')
for p in range(1, 1000):
    if primo % p == 0:
        div += 1
        print(' {}'.format(p), end=' ')
if div == 2:
    print('\nÉ um número primo')
else:
    print('\nNão é um número primo')
