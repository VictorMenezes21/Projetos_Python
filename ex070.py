''' Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final mostre: A) Total gasto na compra B) Quantos produtos custam + de R$1000 C) Qual é o nome do produto mais caro'''

total = 0
qt = 0
mais_caro = 0
nome_maiscaro = ''


while True:

    nome = str(input('Nome do Produto: '))
    preco = int(input('Preço: R$ '))
    total += preco

    if preco > mais_caro:
        nome_maiscaro = nome
        mais_caro = preco

    if preco > 1000:
        qt += 1

    continuar = str(input('Deseja Continuar? [S/N]: ')).upper()

    if continuar == 'S':
        pass
    elif continuar == 'N':
        break


print(f'''
Total Gasto: R$ {total}
Nº de Produtos com preço maior que R$1000: {qt}
Produto mais caro: Nome: {nome_maiscaro} Preço: R${mais_caro}''')
