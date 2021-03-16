s = 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    print('A soma de {} + {} '.format(n, s), end='')
    s = s + n
    print('é {}.'.format(s))
    # s += n
