#Desenvolva um programa que leia um comprimento de 3 retas
print('\033[1;31mDigite o comprimento de três retas\033[m')

r1 = float(input('Primeira: '))
r2 = float(input('Segunda: '))
r3 = float(input('Terceira: '))

#E diga ao usuário se elas podem ou não formar um triângulo.
if r1 < r2+r3:
    print('\033[1;32mÉ possível formar um triângulo\033[m')
elif r2 < r1+r3:
    print('\033[1;32mÉ possível formar um triângulo\033[m')
elif r3 < r1+r2:
    print('\033[1;32mÉ possível formar um triângulo\033[m')
else:
    print('\033[1;31mNão é possível formar um triângulo\033[m')