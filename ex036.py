#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
#O empréstimo será negado.

valor_casa = int(input('Informe o valor da casa: '))
salario = int(input('Informe o salário do comprador: '))
tempo_pagamento = int(input('Em quantos anos será pago a casa? '))

tempo_pagamento = tempo_pagamento * 12
valor_casa = valor_casa / tempo_pagamento

if valor_casa > (salario*0.30):
    print('O empréstimo foi negado, valor máximo de prestação excedido!')

elif valor_casa < (salario*0.30):
    print(f'Aprovado! O valor mensal a ser pago será de R${valor_casa}')
