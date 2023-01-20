''' Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos. B) Quantos homens foram cadastrados
C) Quantas mulheres tem menos de 20 anos'''

homem = 0
maioridade = 0
menor_vinte = 0
continuar = ''

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()

    if idade < 20:

        if idade >= 18:

            if sexo in 'Mm':
                homem += 1
                maioridade += 1

            elif sexo in 'Ff':
                maioridade += 1
                menor_vinte += 1

        else:
            if sexo in 'Ff':
                menor_vinte += 1

            elif sexo in 'Mm':
                homem += 1

    else:

        if sexo in 'Mm':
            homem += 1
            maioridade += 1

        else:
            maioridade += 1

    continuar = str(input('Deseja continuar? [S/N]: ')).upper()

    if continuar == 'S':
        pass

    elif continuar == 'N':
        break


print(f'''Foram cadastrados: 
- {homem} Homens.
- {maioridade} Pessoas maiores de 18 anos.
- {menor_vinte} Mulheres com menos de 20 anos.''')
