#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo,
#Qual é o nome do homem mais velho e quantas mulheres tem menos de 20 anos

from datetime import date

atual = date.today().year
velho = 0
n_velho = ''
cont = 0
soma = 0

for n in range(1, 5):
    print('-'*5, f'{n}ª PESSOA', '-'*5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    soma += idade

    if sexo in 'Mm':
        if n == 1:
            velho = idade

        else:
            if velho < idade:
                velho = idade
                n_velho = nome
    else:
        if idade < 20:
            cont+= 1

media = soma / 4
print(f'''Média de idade do grupo: {media}
Homem mais velho: {n_velho}, {velho} anos
Quantidade de mulheres com menos de 20 anos: {cont}''')