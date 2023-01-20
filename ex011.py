#Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área
#e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta um área de 2m².

repepção = ' Olá, Seja Bem Vindo '
print(f'{repepção:=^20}')

largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))

a = largura * altura
tinta = a/2

print(f'A sua parede possui {a}m², e precisa de {tinta} litos de tinta para pintá-la.')
