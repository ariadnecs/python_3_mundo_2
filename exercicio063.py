# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
n = int(input('Você deseja ver quantos números da Sequência de Fibonacci? '))
f = 1
fi = 0
print('Os {} primeiros números da sequência de Fibonacci: '.format(n), end='')
print('\033[36m{}\033[m, '.format(fi), end='')
while n > 1:
    fi = fi + f
    f = fi - f
    print('\033[36m{}\033[m'.format(fi), end='')
    n -= 1
    if n > 1:
        print(', ', end='')
    else:
        print('!', end='')
