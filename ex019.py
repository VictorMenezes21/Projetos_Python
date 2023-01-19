#Um professor quer sortear um dos seus quatro alunos para apgar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

a = input('Primeiro Aluno: ')
b = input('Segundo Aluno: ')
c = input('Terceiro Aluno: ')
d = input('Quarto Aluno: ')

lista = [a, b, c, d]
escolhido = random.choice(lista)

print(f'No meu sorteio, o aluno que vai apagar o quadro é o {escolhido}')
