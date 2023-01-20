#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um número: '))

tabuada = ' TABUADA '

print(f'{tabuada:=^50}')
for n in range(1, 11):
    print(f'{num} x {n} = {num*n}')

print('=' * 50)
