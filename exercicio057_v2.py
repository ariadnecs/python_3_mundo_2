g = str(input('Informe o seu gênero: [M/F/NB = não binário] ')).upper().strip()[0:2]

while g not in 'MFNB':
    g = str(input('Dados inválidos. \nPor favor, informe seu gênero: [M/F/NB = não binário] ')).strip().upper()[0:2]

print('Gênero:', g)
