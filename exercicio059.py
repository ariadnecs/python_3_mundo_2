#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos números [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
v1 = input('\033[34mDigite um número: \033[m')
v2 = input('\033[34mDigite mais um número: \033[m')
while True:

    op = input('\033[34m\nEscolha uma opção: \n[1]somar \n[2]multiplicar\n[3]maior \n[4]novos números \n[5]sair do programa\nSua opção: \033[m')

    try:
        fv1 = float(v1)
        fv2 = float(v2)
        iop = int(op)
    except:
        print('\nOpção inválida. Tente novamente.')
        iop = 4

    if iop == 1:
        soma = fv1 + fv2
        print('\nVocê escolheu somar: \n{:>3} + {:>3} = {:>4.2f}'.format(fv1, fv2, soma))

    elif iop == 2:
        mult = fv1 * fv2
        print('\nVocê escolheu multiplicar: \n{:>3} * {:>3} = {:>4.2f}'.format(fv1, fv2, mult))

    elif iop == 3:
        if fv1 > fv2:
            print('\nO maior valor digitado foi {}.'.format(fv1))
        elif fv1 < fv2:
            print('\nO maior valor digitado foi {}.'.format(fv2))
        else:
            print('\nOs valores digitados são iguais.')

    elif iop == 4:
        v1 = input('\033[34mDigite um número: \033[m')
        v2 = input('\033[34mDigite mais um número: \033[m')
        print('\nVocê digitou {} e {}'.format(v1, v2))
        continue

    elif iop == 5:
        print('Você escolheu finalizar o programa.')
        break
