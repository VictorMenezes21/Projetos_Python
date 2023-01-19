#Faça um programa que leia o nome completo de uma pessoa.
nome = str(input('Nome completo: ')).strip()
#Mostrando em seguida o primeiro e último nome separadamente

#Separando o nome
nome = nome.split()
#Mostrando o último e o primeiro nome
print(f'Primeiro: {nome[0]}')
print('Último: {}'.format(nome[len(nome)-1]))

