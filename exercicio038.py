# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite mais um valor inteiro: '))
if num1 > num2:
    print('O valor {} é maior do que o {}.'.format(num1, num2))
elif num1 < num2:
    print('O valor {} é maior do que o {}.'.format(num2, num1))
else:
    print('Não existe valor maior pois os dois valores são inguais. Valores digitados: {}.'.format(num1))

