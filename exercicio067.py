# Exercício Python 67: Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

print('*' * 45)
print('{:^45}'.format('Tabuada'))
print('*' * 45)
while True:
    tab = int(input('Você deseja saber a tabuada de qual número? '))

    if tab <= 0:
        break
    for i in range(1, 11):
        print(f'{tab:^3} * {i:>2} = \033[2;34m{tab * i:>3}\033[m')
