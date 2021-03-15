# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO – Média entre 5.0 e 6.9: RECUPERAÇÃO – Média 7.0 ou superior: APROVADO
nota1 = float(input('Digitte a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('Notas da(o) aluna(o) {:.1f} e {:.1f}, média {:.1f}.'.format(nota1, nota2, media))
if media < 5.0:
    print('Aluna(o) reprovada(o)')
#elif media >= 5 and media <= 6.9:
elif 7 > media >= 5:
    print('Aluna(o) está em recuperação')
elif media >= 7:
    print('Aluna(o) aprovada(o)')
