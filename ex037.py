#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão

num = int(input('Digite um número: '))

print('''Escolha uma das bases para conversão: 

[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')

opcao = int(input('R: '))

if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')

elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')

elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')

else:
    print('\033[31mOpção inválida, tente novamente\033[m')
