'''Crie um programa que leia vários números inteiros pelo teclado.
O Programa só vai parar quando o usuário digitar o valor 999 que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o 999)'''

soma = 0
num = 0
cont = 0
print('Para sair do Programa, digite "999"')

while True:
    num = int(input('Digite um número inteiro: '))

    if num == 999:
        break

    soma += num
    cont += 1


print(f'A soma dos {cont} números digitados é igual a {soma}.')