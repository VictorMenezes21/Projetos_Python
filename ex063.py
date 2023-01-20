''' Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma
sequência de fibonacci'''

from time import sleep

print('-' * 35)
print(' \tSEQUÊNCIA DE FIBONACCI')
print('-' * 35)

n = int(input('Quantos termos você quer mostrar: '))
t1 = 0
t2 = 1

print('~' * 35)
print(f'{t1} → {t2}', end='')
c = 3

while c <= n:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    c += 1

print(' → FIM')
