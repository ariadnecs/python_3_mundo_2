from random import randint
from time import sleep
computador = randint(0, 10)
print('\033[34;40mOlá, eu sou o seu computador...\033[m \n\033[34;40mAcabei de pensar em um número entre 0 e 10.\033[m')
print('\033[34;40mSerá que você consegue adivinhar qual foi?\033[m')
acertou = False
n = 0
while not acertou:
    sleep(1)
    jogador = int(input('Qual é o seu palpite? '))
    if jogador == computador:
        n += 1
        print('ACERTOU!\nNós escolhemos o número \033[2;34m{} \033[m!'.format(computador))
        acertou = True
    elif computador < jogador:
        print('Pensei em um número menor do que esse...\nTente novamente.')
        n += 1
    elif computador > jogador:
        print('Pensei em um número maior do que esse...\nTente novamente.')
        n += 1
print('\033[34;40mVocê precisou de {} tentativa(s) para acertar o número que eu escolhi.\033[m'.format(n))