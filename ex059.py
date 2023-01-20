''' Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar [2] Multiplicar [3] Maior [Novos números] [5] Sair do Programa'''

n = True

while n:
    n1 = int(input('Digite o 1º Valor: '))
    n2 = int(input('Digite o 2º Valor: '))

    escolha = int(input('''\t\t MENU DE OPÇÕES
[1] Somar
[2] Multiplicar
[3] Maior número
[4] Novos números
[5] Sair do programa
R: '''))

    if escolha == 1:
        print(f'A soma de {n1} + {n2} = {n1+n2}')

    elif escolha == 2:
        print(f'O produto de {n1} x {n2} = {n1*n2}')

    elif escolha == 3:
        if n1 > n2:
            print(f'O Maior número é o {n1}')
        else:
            print(f'O Maior número é o {n2}')

    elif escolha == 4:
        n = True

    elif escolha == 5:
        break

    else:
        print('\033[1;31mOPÇÃO INVÁLIDA\033[m')


print('FIM DO PROGRAMA...')