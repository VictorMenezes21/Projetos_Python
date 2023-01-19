frase = 'Curso em Vídeo Python'

#FATIAMENTO
#Pega o item 9 da frase
print(frase[9])
#Começa do item 9 e vai ATÉ (exclusive) o 21
print(frase[9:21])
#Começa do item 9 vai até o 21 (exclusive), pulando de 2 em 2
print(frase[9:21:2])
#A frase começa do caractere 0 e vai até o 5 (exclusive)
print(frase[:5])
#A frase começa do caractere 15 e vai até o final
print(frase[15:])
#A frase começa do 9 e vai até o final pulando de 3 em 3
print(frase[9::3])

#ANÁLISE
#len = lenght = comprimento
print(len(frase))
#Pede o programa para contar quantas vezes a letra o (minúscula) aparece
print(frase.count('o'))
#Considera do 0 até o 13 (exclusive) quantos o's existem
print(frase.count('o', 0, 13))
#Mostra onde COMEÇA o 'deo'
print(frase.find('deo'))
#Retorna o valor -1, significando que não existe ou não encontrou
print(frase.find('Android'))
#Verificador in, retorna True ou False
print('Curso' in frase)

#TRANSFORMAÇÃO
#procura a palavra python e substitui por Android
frase.replace('Python', 'Android')
print(frase.replace('Python', 'Android'))
#Método para transformar todas as letras em maiúsculas
print(frase.upper())
#Método para transformar todas as letras em minúsculas
print(frase.lower())
#Método que transforma todos os caracteres em minúsculos, com exceção do 1º
print(frase.capitalize())
#Método que transforma todas as primeiras letras em maiúsculas
print(frase.title())

frase = '   Aprenda Python  '
print(frase)
#Remove todos os espaços inúteis no início e no final da string
print(frase.strip())
#Remove todos os espaços inúteis da direita
print(frase.rstrip())
#Remove todos os espaços inúteis da esquerda
print(frase.lstrip())

#DIVISÃO
frase = 'Curso em Vídeo Python'
#Divide a String, considerando os espaços
print(frase.split())

#JUNÇÃO
#Junta a String, separando por hífens
print('-'.join(frase))