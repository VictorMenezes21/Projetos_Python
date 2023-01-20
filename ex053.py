#Crie um programa que leia um frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Informe uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]


print(f'O inverso de {junto} é {inverso}')
if junto == inverso:

    print('Temos um palíndromo!')

else:
    print('A frase digitada não é um palíndromo')
