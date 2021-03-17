# Exercício Python 48: Faça um programa que calcule a soma
# entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
valores = 0
for multres in range(0, 501, 3):
    if multres % 3 == 0 and multres != 0:
        #valores = valores + 1
        valores += 1
        #soma = soma + multres
        soma += multres
print('Há {} múltiplos de 3 no intervalo entre 1 e 500 e a soma destes números é {}.'.format(valores, soma))