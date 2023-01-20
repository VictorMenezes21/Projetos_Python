'''
Melhore o jogo DESAFIO 028 onde o camputador vai "Pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
import random
from random import randint
from time import sleep

computador = random.randint(0, 5)

print('-=-' * 20)
print('\t\tPENSAREI UM NÚMERO, TENTE ADIVINHAR')
print('-=-' * 20)

n = 0
tentativas = 0

while n != computador:
    n = int(input('Em qual número eu pensei? '))

    print('HMMM...')
    sleep(0.8)
    tentativas += 1

    if n != computador:
        print('\033[1;31mBEEEEEEHHH, Tente Novamente haha!\033[m')


if tentativas == 1:
    print(f'Caraca de Primeira O_O')
else:
    print(f'Finalmente você acertou em kkk, depois de {tentativas} tentativas')

