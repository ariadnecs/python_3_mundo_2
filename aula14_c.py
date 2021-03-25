n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n % 2 == 0 and n != 0:
        par += 1
    elif n % 2 == 1 and n != 0:
        impar += 1
print('Você digitou {} números pares e {} números ímpares.'.format(par, impar))