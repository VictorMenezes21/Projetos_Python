
while True:
    print('Para sair do Programa: [M >= N]')
    m = int(input('Valor de M: '))
    n = int(input('Valor de N: '))

    cont = m
    soma = 0

    if m < n:
        while cont <= n:


            print(f'{cont} + ' if cont < n else f'{cont} = ', end='')
            soma += cont
            cont += 1

        print(f'{soma}')
        print('')

    else:
        break

print('~' * 15, ' FIM ', '~' * 15)