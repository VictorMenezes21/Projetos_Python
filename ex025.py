#Crie um programa que leia o nome de uma pessoa
nome = input('Nome completo: ')

#Diga se ela tem ''SILVA'' no nome.
if 'SILVA' in nome.upper():
    print('Seu nome possui SILVA')
else:
    print('Seu nome não possui SILVA')