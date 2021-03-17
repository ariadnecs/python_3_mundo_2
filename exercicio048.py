#Exercício Python 48: Faça um programa que calcule a soma entre todos os números ímpares
# que são múltiplos de três e que se encontram no intervalo de 1 até 500
soma = 0
valor = 0
for multres in range(1, 501, 2):
    if multres % 3 == 0 and multres % 2 == 1:
        #valor = valor + 1
        valor += 1
        #soma = soma + multres
        soma += multres
print('A soma dos {} numeros ímpares múltiplos de 3 no intervalo de 1 a 500 é {}.'.format(valor, soma))
