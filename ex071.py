''' Crie um programa que simule o funcionamento de um caixa eletrônico. No início pergunte o usuário qual será
o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs: Considere que o caixa possui cédulas de 50, 20, 10 e 1 real'''


print('~' * 50)
print('{:^50}'.format('Banco VICTOR'))
print('~' * 50)

valor = int(input('Valor a ser sacado: R$'))
total = valor
ced = 50
totalced = 0

while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 50:
            ced = 20

        elif ced == 20:
            ced = 10

        elif ced == 10:
            ced = 1

        if total == 0:
            break