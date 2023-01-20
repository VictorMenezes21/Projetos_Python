#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.

#Pergunte o Valor da casa
valor_casa = float(input('Valor da casa: R$'))

#Pergunte o Salário
salario = float(input('Salário do comprador: R$'))

#Pergunte quantos anos irá pagar
anos = int(input('Quantos anos de financiamento: '))

#A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado
prestação = valor_casa / (anos * 12)

print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos} anos')

if prestação > (salario * 0.30):
    print('O seu salário é insuficiente para fazer esse financiamento.')
    print(f'Porquê R${prestação:.2f} excede a 30% do seu salário')

else:
    print(f'A prestação será de R${prestação:.2f}')

