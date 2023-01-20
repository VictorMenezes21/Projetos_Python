#Crie um programa que leia o ano de nascimetno de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade
#e quantas já são maiores

from datetime import date

ano_atual = date.today().year
cont1 = 0
cont2 = 0
for n in range(1, 8):
    ano_nascimento = int(input(f'Em que ano a {n}ª pessoa nasceu: '))
    idade = ano_atual - ano_nascimento

    if idade > 21:
        cont1 += 1
    else:
        cont2 += 1

print(f'Das sete pessoas, {cont1} são de maiores e {cont2} são menores de idade.')

