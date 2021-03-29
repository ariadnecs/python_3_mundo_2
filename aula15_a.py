print('Soma de números inteiros!')
s = 0
while True:
    n = int(input('Digite um número inteiro [para encerrar a soma digite "0"]: '))
    if n == 0:
        break
    s += n

# print('A soma vale {}'.format(s))
print(f'A soma vale {s:>5}')# f strings