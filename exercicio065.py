# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
from time import sleep

n = int(input('Digite um número: '))
lista = [n]
c = True
soma = 0
count = 0

while c is True:

    n = int(input('Digite um número: '))
    lista.append(n)


    string = str(input('Deseja continuar? [Y/N] ')).upper()
    if string == 'N':
        c = False
    elif string != 'N' and string != 'Y':
        print('Opção inválida. Tente novamente.')

print('\nSomando...')
sleep(2)

for num in lista:
    soma += num
    print(soma, end=' ')

    if num == lista[0]:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num

count = len(lista)

print('\nVocê digitou os números {}'.format(lista))
print('Maior número {} e menor número {}.'.format(maior, menor))
print('Soma {}, quantidade de números digitados {} e média {:.2f}'.format(soma, count, soma / count))


