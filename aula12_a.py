# if, elif & else
nome = str(input('Qual é o seu nome? ')).strip().title()
# .strip() remove os excessos de espaços
# .title() transforma em título o que for escrito, palavras iniciam com letras maiúsculas

if nome == 'Spock':# aqui o programa faz a busca pelo nome escrito cmo título, iniciando com maiúscula, sacou?
    print('Olá, Oficial de Ciências {}! \n"Vida longa e próspera".'.format(nome))
elif nome == 'Kirk':
    print('Olá, capitão {}. \nQue tal ser menos mulherengo?'.format(nome))
elif nome == 'Mccoy':
    # corrigir o nome assim: nome = 'McCoy', ou adicionar o nome em format
    print('Olá, Oficial-Chefe Médico {}.'.format('McCoy'))
elif nome == 'Uhura':
    print('Olá, Oficial-Chefe de Comunicações {}. \nA senhora influenciou muitas mulheres em diversas áreas. \nObrigada por esse legado!'.format(nome))
else:
    print('Você faz parte da tripulação agora! \nTenha um bom dia {}.'.format(nome))

