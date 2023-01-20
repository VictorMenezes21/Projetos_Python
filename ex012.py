#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
#com 5% de desconto

r = ' PROMOÇÃO DE 5% DE DESCONTO '
print(f'{r:=^50}')

p = float(input('Informe o valor do seu produto: '))
desc = p * 0.05
nvalor = p - desc

print(f'Com o desconto de R${desc}, você precisará pagar apenas R${nvalor}!!!')
