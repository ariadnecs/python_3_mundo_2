# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#  se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou
#  se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
datenasc = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - datenasc
if idade < 18:
    faltam = 18 - idade
    anoalist = faltam + date.today().year
    print('Você tem {} anos e terá que se alistar ao serviço militar daqui a {} anos, {}.'.format(idade, faltam, anoalist))
elif idade == 18:
    print('Você completará 18 anos neste ano e deve se alistar ao serviço militar.')
else:
    passaram = idade - 18
    anoalist = date.today().year - passaram
    print('Você tem {} anos e o ano do seu alistamento foi em {}.'.format(idade, anoalist))
