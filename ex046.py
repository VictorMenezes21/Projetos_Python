#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0
#com uma pausa de 1 segundo entre eles.

from time import sleep

for n in range(10, 0, -1):
    print(n)
    sleep(1)

print('\033[4;32mF E L I Z   A N O   N O V O! ! ! !\033[m')
