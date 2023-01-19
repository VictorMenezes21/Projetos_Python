#Faça um programa que leia um número de 0 a 9999
num = int(input('Digite um número de 0 a 9999: '))

#E mostre na tela cada um dos dígitos separados

#Separando os dígitos
milhar = num // 1000 % 10
cen = num // 100 % 10
dez = num // 10 % 10
unid = num % 10

print(f'Milhar: {milhar}\nCentena: {cen}\nDezena: {dez}\nUnidade: {unid}')


