# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
from math import factorial
n = int(input('Digite um númeor interiro que eu calcularei o fatorial dele: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))
