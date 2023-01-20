cont = 0
aluno = 0
media = 0
media_tot = 0
aprov = 0
exame = 0
reprov = 0

print('''---------------------------------------
Média Aritmética\t|\tSituação
Entre 0 e 29\t\t|\tReprovado
Entre 30 e 69\t\t|\tExame Especial
Entre 70 e 100\t\t|\tAprovado
---------------------------------------''')

while cont < 6:
    nota1 = int(input('Digite a 1ª Nota: '))
    nota2 = int(input('Digite a 2ª Nota: '))
    media = (nota1 + nota2) / 2

    if 0 <= media <= 29:
        print(f'Média {media} - \033[31mReprovado\033[m')
        media_tot += media
        reprov += 1
        cont += 1

    elif 30 <= media <= 69:
        print(f'Média {media} - \033[33mExame Especial\033[m')
        exame += 1
        media_tot += media
        cont += 1

    elif 70 <= media <= 100:
        print(f'Média {media} - \033[32mAprovado\033[m')
        aprov += 1
        media_tot += media
        cont += 1

    else:
        print('Dados inválidos, informe novamente.')

media_tot = media_tot / 6

print(f'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Alunos aprovados: {aprov}
Alunos de Exame: {exame}
Alunos Reprovados: {reprov}
Média da Classe {media_tot:.2f}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')