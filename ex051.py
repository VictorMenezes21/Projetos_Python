#Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética.
#No final, mostre os 10 primeiros termos dessa progressão.
from time import sleep

print('=' * 34)
print(' ' * 5, '10 TERMOS DE UMA PA ')
print('=' * 34)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao

for n in range(termo, decimo, razao):
    print(n, end=' ')
    sleep(0.1)

print('Fim!')