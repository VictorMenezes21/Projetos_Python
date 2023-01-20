''' Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo'''
import random
from time import sleep

n_vitorias = 0
while True:
    jogador = 0
    n_computador = random.randint(0, 10)
    computador = random.randint(1, 2)
    resultado = 0


    print('~' * 50)
    print('\t\t\t[1] Impar | [2] Par')
    print('~' * 50)
    print('COMPUTADOR ESCOLHENDO...', end=' ')
    sleep(0.3)


    if computador == 1:
        print(f'O Computador escolheu Ímpar')
        sleep(1)
        print('Impar', end='')
        sleep(0.25)
        print(' ou ', end='')
        sleep(0.25)
        print('Par', end='')
        jogador = int(input(': '))
        print(f'Computador: {n_computador} -- Jogador: {jogador}')
        resultado = jogador + n_computador

        if resultado % 2 == 0:
            print(f'{resultado} é par!')
            print('Jogador Venceu!')
            n_vitorias += 1

        else:
            print(f'{resultado} é ímpar!')
            print('Computador Venceu!')
            break

    else:
        print(f'O Computador escolheu Par')
        sleep(1)
        print('Impar', end='')
        sleep(0.25)
        print(' ou ', end='')
        sleep(0.25)
        print('Par', end='')
        jogador = int(input(': '))
        resultado = jogador + n_computador
        print(f'Computador: {n_computador} -- Jogador: {jogador}')

        if resultado % 2 == 0:
            print(f'{resultado} é par!')
            print('Computador Venceu')
            break

        else:
            print(f'{resultado} é ímpar!')
            print('Jogador Venceu!')
            n_vitorias += 1


print(f'O Jogador ganhou {n_vitorias} vezes.')
