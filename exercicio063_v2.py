n = int(input('Você deseja ver quantos números da Sequência de Fibonacci? '))
f = 1
fi = 0

# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
print('Os {} primeiros números da sequência de Fibonacci: '.format(n), end='')
print('\033[32m{}\033[m, \033[32m{}\033[m, '.format(fi, f), end='')

while n > 2:
    fib = fi + f
    print('\033[32m{}\033[m'.format(fib), end='')
    fi = f
    f = fib
    n -= 1

    if n > 2:
        print(', ', end='')
    else:
        print('!', end='')
