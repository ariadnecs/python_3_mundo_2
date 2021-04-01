# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('=' * 40)
print(f'{"Banco coisa e tal":^40}')
print('=' * 40)

while True:
    valor = int(input('Qual valor você deseja sacar: R$'))
    print(f'Valor solicitado para saque R${valor:<8} \nSaque:')

    divint_cinq = valor // 50
    rest_cinq = valor % 50
    if divint_cinq != 0:
        print(f'{divint_cinq:>4} cédula(s) de R$50')
    elif rest_cinq == 0:
        break

    divint_vinte = rest_cinq // 20
    rest_vinte = rest_cinq % 20
    if divint_vinte != 0:
        print(f'{divint_vinte:>4} cédula(s) de R$20')
    elif rest_vinte == 0:
        break

    divint_dez = rest_vinte // 10
    rest_dez = rest_vinte % 10
    if divint_dez != 0:
        print(f'{divint_dez:>4} cédula(s) de R$10')
    elif rest_dez == 0:
        break

    divint_um = rest_dez // 1
    if divint_um != 0:
        print(f'{divint_um:>4} cédula(s) de R$1')
    break

print('=' * 40)
print('Operação finalizada. Tenha um bom dia!')
