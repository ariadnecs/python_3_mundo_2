# DESAFIO 35 Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo
# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes
sr1 = float(input('1º segmento de reta: '))
sr2 = float(input('2º segmento de reta: '))
sr3 = float(input('3º segmento de reta: '))
if sr1 + sr2 > sr3 and sr1 + sr3 > sr2 and sr2 + sr3 > sr1:
    print('Os segmentos de reta {}, {} e {} formam um triângulo '.format(sr1, sr2, sr3), end='')
    if sr1 == sr2 == sr3: # if sr1 == sr2 and sr2 == sr3
        print('Equilátero.')
    elif sr1 == sr2 or sr1 == sr3 or sr2 == sr3:
        print('Isósceles.')
    elif sr1 != sr2 != sr3 != sr1:# lembrar que a diferença não é inclusiva como a igualdade, por isso incluir != sr1
    #else:
        print('Escaleno.')
else:
    print('Os segmentos de reta digitados não formam um triângulo.')