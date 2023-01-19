#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria
#de acordo com a idade: até 9: Mirim, até 14: Infantil, até 19: Junior, até 20: Senior, acima de 20: Master
import datetime

idade = int(input('Para saber sua categoria, informe o ano de seu nascimento: '))

if (datetime.date.today().year - idade) <= 9:
    mirim = datetime.date.today().year - idade
    print(f'Pessoas com {mirim} anos pertencem a categoria Mirim.')

elif 9 < (datetime.date.today().year - idade) <= 14:
    infantil = datetime.date.today().year - idade
    print(f'Pessoas com {infantil} anos pertencem a categoria Infantil.')

elif 14 < (datetime.date.today().year - idade) <= 19:
    junior = datetime.date.today().year - idade
    print(f'Pessoas com {junior} anos pertencem a categoria Júnior.')

elif 19 < (datetime.date.today().year - idade) <= 20:
    senior = datetime.date.today().year - idade
    print(f'Pessoas com {senior} anos pertencem a categoria Sênior.')

else:
    master = datetime.date.today().year - idade
    print(f'Pessoas com {master} anos pertencem a categoria Master.')
