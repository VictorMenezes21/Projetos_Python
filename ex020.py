#Um Professor quer sortear a ordem de apresentação de trabalho dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

a = input('Primeiro Aluno: ')
b = input('Segundo Aluno: ')
c = input('Terceiro Aluno: ')
d = input('Quarto Aluno: ' )

alunos = [a, b, c, d]
sort = random.shuffle(alunos)
print('A ordem de apresentação será!')
for x in alunos:
    print(x)

