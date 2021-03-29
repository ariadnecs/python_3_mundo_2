#
print('Soma de números inteiros!')
s = 0
while True:
    n = int(input('Digite um número inteiro [para encerrar a soma digite "999"]: '))
    if n == 999:
        break
    s += n

# print('A soma vale {}'.format(s))
print(f'A soma vale {s:>5}')# f strings