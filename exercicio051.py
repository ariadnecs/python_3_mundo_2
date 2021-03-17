# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

print('=' * 35)
print('{:^35}'.format('Os primeiros termos de uma PA'))
print('=' * 35)
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
for n in range(1, 11):
    an = a1 + (n-1) * r
    print(an, end=' -> ')
print('AcaboUUU')
