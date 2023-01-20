''' Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O Programa será interrompido quando o número solicitado for negativo.'''


while True:
    print('Para sair da Tabuada, digite um número negativo.')
    num = int(input('Digite um número inteiro: '))

    if num < 0:
        break

    else:
        print('-' * 20, 'TABUADA', '-' * 20)
        n = 0
        for n in range(1, 11):
            print(f'{num} x {n} = {n * num}')

    print('-' * 50)

print('FIM DO PROGRAMA.....')