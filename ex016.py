#Crie um programa que leia um número Real qualquer pelo teclado
#e mostre na tela a sua porção inteira
import math
from math import trunc

n1 = float(input('Digite um número: '))

print(f'A parte inteira de {n1} é {math.trunc(n1)}')
print(f'A porção inteira de {n1} é {int(n1)}')

