# Exercício Python 49: Refaça o DESAFIO 9,
# mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = int(input('Desejo saber a tabuada do número: '))
for vezes in range(1, 11):
    print('{:<2} * {:2} = {:>3}'.format(num, vezes, num * vezes))