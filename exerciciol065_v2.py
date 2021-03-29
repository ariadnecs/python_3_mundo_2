resp = 'S'
soma = quant = media = 0

while resp == 'S':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1

    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper()

media = soma / quant
print('Você digitou {} números e a média foi {:.2f}'.format(quant, media))
