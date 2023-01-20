''' Crie um Programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a
digitar valores. '''

media = 0
soma = 0
maior = 1
menor = 9999
while True:

    n = int(input('Digite um número: '))
    soma += n
    media += 1

    if maior < n:
        maior = n

    if menor > n:
        menor = n

    prox = str(input('Deseja continuar? [S/N]: ')).upper()
    if prox == 'N':
        break

print(f'''
SOMA DOS VALORES: {soma}
MÉDIA DOS VALORES: {soma/media}
MAIOR VALOR LIDO: {maior}
MENOR VALOR LIDO: {menor}''')
