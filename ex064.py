''' Crie um programa que leia vários números inteiros pelo teclado. O programa só vai pararquando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)'''

n = soma = conta = 0
while True:
    n = int(input('Digite um número: '))

    if n != 999:
        soma += n
        conta += 1

    else:
        break

print(f'A somas dos {conta} números digitados é {soma}')