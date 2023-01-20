#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

cont = 0
p_maior = 0
p_menor = 0

for n in range(1, 6):
    peso = float(input(f'Peso da {n}ª pessoa: '))

    if n == 1:
        p_maior = peso
        p_menor = peso

    else:
        if p_maior < peso:
            p_maior = peso


        if p_menor > peso:
            p_menor = peso


print(f'O maior peso lido foi de {p_maior}Kg\nO menor peso lido foi de {p_menor}Kg')
