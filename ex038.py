#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#- O primeiro valor é maior, - O segundo valor é maior, - Não existe valor mairo, os dois são iguais.

num1 = int(input('\033[1;97mDigite um número: \033[m'))
num2 = int(input('\033[1;97mDigite outro número: \033[m'))

if num1 > num2:
    print(f'\033[1;35mO primeiro número ({num1}) é maior do que o segundo ({num2})\033[m')

elif num2 > num1:
    print(f'\033[1;32mO segundo número ({num2}) é maior do que o primeiro ({num1})\033[m')

else:
    print('\033[4;31mOs dois números digitados são iguais!\033[m')