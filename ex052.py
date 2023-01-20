#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

cont = 0
num = int(input('Digite um número: '))
for n in range(1, num + 1):
    if num % n == 0:
        print(f'\033[32m', end=' ')
        cont += 1

    else:
        print('\033[31m', end=' ')

    print(n, end=' ')

print('\033[m')

if cont > 2:
    print(f'O número {num} foi divisível {cont} vezes, portanto ele não é primo')

else:
    print(f'O número {num} foi divisível {cont} vezes, portanto ele é primo')

