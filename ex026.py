#Faça um programa que leia uma frase pelo teclado
frase = str(input('Digite uma frase: ')).strip()

#E mostre:
#Quantas vezes aparece a letra 'A'
print(f'A frase {frase} possui:')
print(frase.upper().count('A'), 'letras A')

#Em que posição ela aparece a primeira vez
print('A primeira letra A apareceu na posição {} '.format(frase.upper().find('A')+1))

#Em que posição ela aparece a última vez
print('A última letra A apareceu na posição {} '.format(frase.upper().rfind('A')+1))

