#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso, -  Entre 18.5 e 25: Peso ideal, - 25 a 30: Sobrepeso, 30 a 40: Obesidade, - acima de 40: Obesidade Mórbida.


print('\033[1;32m--' * 20, 'Para calcular o IMC', '\033[1;32m--\033[m' * 20)
altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('\033[1;31mAbaixo do Peso.\033[m')

elif 18.5 <= imc < 25:
    print('\033[1;32mPeso ideal.\033[m')

elif 25 <= imc < 30:
    print('\033[1;33mSobrepeso.\033[m')

elif 30 <= imc < 40:
    print('\033[1;32mObesidade.\033[m')

else:
    print('\033[1;32mObesidade Mórbida.\033[m')
