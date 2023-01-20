# Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
import random


print('Vamos Jogar Jokenpô')

jokenpo = ('Pedra', 'Papel', 'Tesoura')
comput = random.randint(0, 2)
choice = int(input('''Escolha:
[0] Pedra
[1] Papel
[2] Tesoura
R: '''))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!')

print(f'O Jogador jogou {jokenpo[choice]} -- O Computador jogou {jokenpo[comput]}')

if comput == 0: # O computador jogou PEDRA
    if choice == 0:
        print('EMPATE!')

    elif choice == 1:
        print('\033[1;32mJOGADOR VENCEU!\033[m')
        sleep(1)
        print('-Droga, perdi!')

    elif choice == 2:
        print('\033[1;31mCOMPUTADOR VENCEU!\033[m')
        sleep(1)
        print('-HAHAHA')
        sleep(1)
        print('-Eu venci!')

    else:
        print('\033[1;31mJOGADA INVÁLIDA\033[m')

elif comput == 1: # O computador jogou PAPEL
    if choice == 0:
        print('\033[1;31mCOMPUTADOR VENCEU!\033[m')
        sleep(1)
        print('-Venci, haha!')

    elif choice == 1:
        print('EMPATE!')

    elif choice == 2:
        print('\033[1;32mJOGADOR VENCEU!\033[m')
        sleep(1)
        print('-Perdi, droga!')

    else:
        print('\033[1;31mJOGADA INVÁLIDA\033[m')

elif comput == 2: # O computador jogou TESOURA
    if choice == 0:
        print('\033[1;32mJOGADOR VENCEU!\033[m')
        sleep(1)
        print('-Perdi, droga!')

    elif choice == 1:
        print('\033[1;31mCOMPUTADOR VENCEU!\033[m')
        sleep(1)
        print('-Venci, haha!')

    elif choice == 2:
        print('\033[1;33mEMPATE!\033[m')

    else:
        print('\033[1;31mJOGADA INVÁLIDA\033[m')

else:
    print('\033[1;31mJOGADA INVÁLIDA\033[m')