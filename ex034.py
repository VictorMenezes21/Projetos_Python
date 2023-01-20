#Escreva um programa que pergunte o salário de um funcionário
salario = float(input('Informe se salário atual: '))

#E calcule o valor do seu aumento
#Para salários superiores a R$1.250,00, calcule um aumento de 10%
if salario > 1250.00:
    aumento = salario * 0.10
    salarioNovo = aumento + salario
    print(f'Com um aumento de R${aumento}, seu novo salário é R${salarioNovo}.')

#Para os inferiores ou igual o aumento é de 15%
else:
    aumento = salario * 0.15
    salarioNovo = aumento + salario
    print(f'Com um aumento de R${aumento}, seu novo salário é R${salarioNovo}')