# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('O pesoa da {}ª pessoa é: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    if peso >= maior:
        maior = peso
    elif peso <= menor:
        menor = peso

print('Peso maior é {}Kg e o peso menor é {}Kg'.format(maior, menor))
