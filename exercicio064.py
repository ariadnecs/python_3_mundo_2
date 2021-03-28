# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#  No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
num = count = soma = 0
# count = 0
# soma = 0
lista = []

while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        lista.append(num)
        soma += num
        count += 1

media = float(soma / count)
print('Você digitou os números \033[34m{}\033[m'.format(lista))
print('A soma dos números {} digitados é \033[2;34m{}\033[m. \nA média dos números digitados é \033[34m{:.2f}\033[m.'.format(count, soma, media))

