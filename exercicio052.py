# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
div = 0
lista = []
num = int(input('Digite um número: '))
print('O número {} é divisível por: '.format(num), end='')
for p in range(1, num + 1):
    if num % p == 0:
        div += 1
        lista.append(p)
if div == 2:
    print('\n{} é dividido apenas por \033[1;34m{}\033[m, ele é um número primo.'.format(num, lista))
else:
    print('\n{} é dividido por \033[1;34m{}\033[m, ele não é um número primo. '.format(num, lista))
