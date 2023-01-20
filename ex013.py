#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
r = ' Olá, Seja bem vindo! '
print(f'{r:=^50}')

salario = float(input('Informe seu salário: '))
aumento = salario * 0.15
novoSalario = salario + aumento

print(f'Seu salário obteve um aumento de R${aumento}, tendo seu valor agora de R${novoSalario}')