''' Faça um Programa que leia o sexo de uma pessoa, mas só aceita 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto'''

sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MF':
    print('\033[1;31mResposta inválida!\033[m')
    sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]


if sexo == 'M':
    print('Sexo Masculino registrado com sucesso.')

else:
    print('Sexo Feminino registrado com sucesso.')
