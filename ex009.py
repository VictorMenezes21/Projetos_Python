#Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.

recepçao = " Olá, Seja Bem Vindo! "
print(f'{recepçao:=^50}')

tabuada = ' TABUADA '
num = int(input('Informe um número, para saber sua tabuada: '))
print(f'{tabuada:=^50}')
print('-' * 20)

for tabuada in range(10):
    print('%d x %d = %d' % (num, tabuada + 1, num*(tabuada+1)))

print('-' * 20)
