#Faça um programa que leia um ângulo qualquer e mostre na tela
#O valor do seno, cosseno e tangente desse ângulo
import math

ang = float(input('Digite um ângulo: '))

sin = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print((f'O seno de {ang} é {sin:.3f}, o cosseno é {cos:.3f} e a tangente é {tan:.3f}'))
