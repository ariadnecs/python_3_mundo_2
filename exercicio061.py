# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('\033[34m=\033[m' * 40)
print('{:^40}'.format('Os primeiros 10 termos de uma PA'))
print('\033[34m=\033[m' * 40)
t = 'Y'
while t == 'Y':
    a1 = int(input('Digite o primeiro termo de uma PA: '))
    r = int(input('Digite a razão da PA: '))
    n = 1
    t = 1
    while n < 11:
        an = a1 + (n - 1) * r
        print(' {:<2}º termo = {}'.format(t, an))
        n += 1
        t += 1
    t = str(input('Deseja calcular mais uma PA? [Y/N] ')).upper()

print('Programa finalizado.')
