#Escreva um programa que faça um computador pensar em um número inteiro entre 0 e 5 e peça para o usuário
#Tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
#Venceu ou perdeu
import random
from time import sleep
import colorsys

computador = random.randint(0, 5) #Faz o computador 'PENSAR'

print('--' * 30)
print('Vou pensar em um número entre 0 e 5. Tente Advinhar...\033[m')
print('--' * 30)

n = int(input('Em que número eu pensei?\n')) #Jogador tenta adivinhar

print('PROCESSANDO...')
sleep(1.5)

if n == computador:
    print('\033[32mVocê GANHOU, parabéns!!\033[m')
else:
    print(f'\033[31mHAHAHAHAHAHAHA GANHEI, porque eu pensei no {computador}!\033[m')