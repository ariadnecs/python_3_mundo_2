frase = str(input('Digite uma frase: ')).upper().strip().split()
unir = ''.join(frase)
inverso = ''
inverso = unir[::-1]#inicio:fim:-1 de tras para frente
print('O inverso de {} é {}.'.format(unir, inverso))
if unir == inverso:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
    