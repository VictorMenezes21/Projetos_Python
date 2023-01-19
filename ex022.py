#Crie um programa que leia o nome completo de uma pessoa e mostre:
nome = str(input('Nome completo:\n')).strip()

#O Nome com todas as letras maiúsculas
print(nome.upper())

#O nome com todas minúsculas
print(nome.lower())

#Quantas letras ao todo(sem considerar espaços).
print(f'O nome {nome} possui ', len(nome.strip())-nome.count(' '), ' letras ao todo.')

#Quantas letras tem o primeiro nome
pnome = nome.split()
print(f'O nome {pnome[0]} possui {len(pnome[0])} letras.')
