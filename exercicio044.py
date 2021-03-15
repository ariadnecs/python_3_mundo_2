#Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento: à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto; em até 2x no cartão: preço formal; 3x ou mais no cartão: 20% de juros
valor = float(input('Valor do produto: R$'))
cond_pag = int(input('Condição de pagamento: \n[1] à vista dinheiro/cheque \n[2] à vista no cartão \n[3] parcelado em até 2x'
                     '\n[4] parcelado em 3x ou mais \nOpção escolhida: '))
print('O valor original do produto é de R${:.2f}'.format(valor))
if cond_pag == 1:
    desconto = valor - (valor * 10 / 100)
    print('Pagamento à vista dinheiro/cheque. \nValor do produto com 10% de desconto R${:.2f}.'.format(desconto))
elif cond_pag == 2:
    desconto = valor - (valor * 5 / 100)
    print('Pagamento à vista no cartão. \nValor do produto com 5% de desconto R${:.2f}'.format(desconto))
elif cond_pag == 3:
    valor_parcelas = valor / 2
    print('Sua compra será parcelada em 2x de R${}, sem juros. \nValor a ser pago R${:.2f}.'.format(valor_parcelas, valor))
elif cond_pag == 4:
    valor_juros = valor + (valor * 20/100)
    parcelas = int(input('Quantas parcelas? '))
    valor_parcelas = valor_juros / parcelas
    print('Parcelamento em {}x de R${:.2f}. \nO valor do produto com 20% de juros é de R${:.2f}.'
          .format(parcelas, valor_parcelas, valor_juros))
else:
    print('Opção inválida.')
