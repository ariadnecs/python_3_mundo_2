# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato
conti = ' '
total = prod = count = 0
print('\n{:-^40}'.format('Mercado da Rua'))
while conti != 'N':
    nome = str(input('Nome do produto: ')).strip()
    count += 1
    prec = float(input('Preço do produto: R$'))
    total += prec
    if prec > 1000.00:
        prod += 1

    if count == 1:
        maior = menor = prec

    if prec >= maior:
        maior = prec
        prod_caro = nome
    if prec <= menor:
        menor = prec
        prod_barato = nome

    conti = input('Deseja continuar? [S/N] ').upper()

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'\nTotal de gastos = R${total:.2f} \n{prod} produtos custam mais de R$1000')
print(f'{prod_caro} é o produto mais caro, ele custa R${maior},\n{prod_barato} é o produto mais barato, ele custa {menor}')
