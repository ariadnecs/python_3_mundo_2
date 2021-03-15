# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso;  Entre 18,5 e 25: Peso Ideal
# IMC entre 25,0 e 29,9 Kg/m2: sobrepeso;
# IMC entre 30,0 e 34,9 Kg/m2: obesidade grau I;
# IMC entre 35,0 e 39,9 Kg/m2: obesidade grau II;
# IMC maior do que 40,0 Kg/m2: obesidade grau III
# NÃO SE UTILIZA MAIS O TERMO 'OBESIDADE MÓRBIDA', os valores acima correspondem ao site
# https://centrodeobesidadeediabetes.org.br/tudo-sobre-obesidade/calculadora-de-imc/#:~:text=O%20IMC%20%C3%A9%20reconhecido%20como,ao%20quadrado%20(em%20metros).
print('Cálculo de IMC')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print('Olá, o seu peso é {}Kg e a sua altura é {}m. O valor do seu IMC é de {:.1f}Kg/m².'.format(peso, altura, imc))
if imc < 18.5:
    print('Você está com sobrepeso. Sugiro que procure um profissional para verificar a sua saúde. Fique bem e cuide-se.')
elif imc < 25:
    print('Tenho uma ótima notícia, você está no peso ideal. Mantenha a alimentação saudável e a atividade física em dia.')
elif imc < 29.9:
    print('Você está com sobrepeso. Sugiro que procure um profissional, \npara que assim tenhas uma alimentação equilibrada '
          'e saiba quais atividades física são ideais para você :D')
elif imc < 34.9:
    print('O valor do seu IMC é o correspondente a obesidade grau I. \nSugiro que procure um grupo de apoio, centro de '
          'obesidade, na sua cidade. \nVocê terá o amparo de profissionais, não se sinta só.')
elif imc < 39.9:
    print('O valor do seu IMC é o correspondente a obesidade grau II. \nSugiro que procure um grupo de apoio, centro de '
          'obesidade, na sua cidade. \nVocê terá o amparo de profissionais, não se sinta só.')
elif imc < 40.0:
    print('O valor do seu IMC é o correspondente a obesidade grau I. \nSugiro que procure um grupo de apoio, centro de '
          'obesidade, na sua cidade. \nVocê terá o amparo de profissionais, não se sinta só.')