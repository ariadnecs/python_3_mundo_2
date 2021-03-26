from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0

while op != 5:
    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    op = int(input('\nQual é a sua opção? '))

    if op == 1:
        soma = n1 + n2
        print('A soma de {} e {} é {}.'.format(n1, n2, soma))

    if op == 2:
        mult = n1 * n2
        print('A multiplicação de {} por {} é {}.'.format(n1, n2, mult))

    if op == 3:
        if n1 > n2:
            print('{} é maior do que {}'.format(n1, n2))
        if n2 > n1:
            print('{} é maior do que {}.'.format(n2, n1))

    if op == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    if op == 5:
        break

print('\nFinalizando...')
sleep(1)
print('Fim do programa!')
