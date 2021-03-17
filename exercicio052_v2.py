# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;34m', end='')
        total += 1
    else:
        print('\033[30m', end='')
    print('{} '.format(c), end='')
print('\033[35m\nO número {} foi dividido {} vezes\033[m'.format(num, total))
if total == 2:
    print('\033[1;34m{}\033[m somente é divisível por 1 e por ele mesmo\ne por isso ele é um número\033[1;34m PRIMO\033[m'.format(num))
else:
    print('e por isso ele não é um número primo.')
