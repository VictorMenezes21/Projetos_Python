#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
recepção = ' Olá, Aluno '
print(f'{recepção:=^50}')

nota1 = float(input('Informe sua 1ª nota: '))
nota2 = float(input('Informe sua 2ª nota: '))

media = (nota1+nota2)/2

print(f'A média da sua nota é {media}')