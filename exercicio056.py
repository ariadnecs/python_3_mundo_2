# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos
somaidade = 0
maior = 0
menordevin = 0
for p in range(1, 5):
    print('--------- {}ª PESSOA ----------'.format(p))
    nome = str(input('Digite o seu nome: ')).strip().title()
    idade = int(input('Digite a sua idade: '))
    somaidade += idade
    sexo = str(input('Sexo binário, M ou F? ')).upper()
    if idade >= maior and sexo == 'M' or sexo == 'MASCULINO':
        maior = idade
        maiornome = nome
    elif sexo == 'F' and idade < 20:
        menordevin += 1

media = somaidade / 4
print('A média da idade do grupo é de {:.2f} anos. '.format(media))
print('{} é o homem com maior idade no grupo, {} anos.'.format(maiornome, maior))
print('Há {} mulheres/meninas com menos de 20 anos no grupo.'.format(menordevin))
