# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
from time import sleep
valor_casa = float(input('Valor da casa: R$'))
salario = float(input('Digite o valor do salário do cliente: R$'))
anos = int(input('Em quantos anos o cliente irá pagar o imóvel? '))
prestacao = valor_casa / (anos * 12)
print('Verificando a aprovação do empréstimo bancário...')
sleep(2)
if prestacao < (salario * 30 / 100):
    print('\nEmpréstimo aprovado!\nO imóvel no valor de R${:.2f} será pago em {} anos.'.format(valor_casa, anos))
    print('A prestação da casa terá o valor mensal de R${:.2f}, sem o acréscimo de juros.'.format(prestacao))
else:
    print('\nEmpréstimo negado. \nO valor da parcela do imóvel excedeu 30% do salário do cliente.')
