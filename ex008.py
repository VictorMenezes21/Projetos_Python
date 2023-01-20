#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

recepção = ' Olá, Tudo bem? '
print(f'{recepção:=^50}')

m = int(input('Informe o um valor em metros: '))

cm = m*100
mm = m*1000

print(f'O valor de {m} em centímetros é {cm} e em milímetros é {mm}.')
