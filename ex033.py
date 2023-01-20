#Faça um programa que leia três números.
print('Informe 3 números')
a = int(input('Primeiro: '))
b = int(input('Segundo: '))
c = int(input('Terceiro: '))

#E mostre qual é o maior e qual é o menor
if a > b > c:
    print(f'{a} é o maior número e {c} é o menor número')
elif a > c > b:
    print(f'{a} é o maior número e {b} é o menor número')
elif b > c > a:
    print(f'{b} é o maior número e {a} é o menor número')
elif b > a > c:
    print(f'{b} é o maior número e {c} é o menor número')
elif c > a > b:
    print(f'{c} é o maior número e {b} é o menor número')
else:
    print(f'{c} é o maior número e {a} é o menor número')