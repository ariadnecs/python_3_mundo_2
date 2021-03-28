# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário
# se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
c = True

while c is True:
    aum = int(input('Digite o primeiro termo de uma PA: '))
    r = int(input('Digite a razão da PA: '))
    n = int(input('A PA tem quantos termos? (Se desejar encerrar o programa digite "0") '))
    count = 1
    if n == 0:
        print('Encerrando o programa...')
        c = False
    for n in range(n, 0, -1):
        an = aum + (count - 1) * r

        print('{:>3}º termo = {}'.format(count, an))
        count += 1

