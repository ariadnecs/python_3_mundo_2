# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

g = str(input('Qual é o seu gênero? [M/F/NB = não binário] ')).upper().strip()
while g != 'M' and g != 'F' and g != 'NB':
    print('Opção inválida. Digite novamente')
    g = str(input('Qual é o seu gênero? [M/F/NB = não binário] ')).upper()

print('Gênero digitado {}'.format(g))
