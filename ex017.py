#Faça um programa que leia o comprimento do cateto oposto e do cateto
#Adjacente de um triângulo retângulo, calcule e mostre o comprimento
#da hipotenusa

import math

co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente: '))

hipo = math.sqrt(((co**2)+(ca**2)))
print(f'A hipotenusa desse triângulo retângulo é {hipo:.2f}')

hipo = math.hypot(co, ca)
print(f'A hipotenusa desse triângulo retângulo é {hipo:.2f}')
