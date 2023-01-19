#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: reprovado, - Média entre 5.0 e 6.9: Recuperação, - Média igual ou superior a 7.0: Aprovado.

nota1 = float(input('Informe sua 1ª nota: '))
nota2 = float(input('Informe sua 2ª nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('\033[1;31mReprovado!\033[m')

elif 5.0 < media < 6.9:
    print('\033[1;33mRecuperação!\033[m')

else:
    print('\033[1;32mAprovado!\033[m')
    