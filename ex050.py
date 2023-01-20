#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares
#Se o valor digitado for ímpar desconsidere-o.

print('Informe seis números inteiros')

num_aux = 0
for n in range(6):
    num = int(input(f'{n+1}º: '))
    if num % 2 == 0:
        num_aux += num

print(f'A soma dos números pares é {num_aux}')


