''' Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando a estrutura while.'''

from time import sleep

print('=' * 34)
print(' ' * 5, ' GERADOR DE PA ')
print('=' * 34)

loop = True
while loop:
    termo = int(input('Digite o termo: '))
    razao = int(input('Digite a razão: '))
    cont = 1

    while cont <= 10:
        if cont == 10:
            print(f'{termo}')
        else:
            print(f'{termo} → ', end=' ')

        termo += razao
        cont += 1

    quit = str(input('Deseja continuar? [S/N]: ')).upper()

    if quit == 'N':
        loop = False


print('FIM')