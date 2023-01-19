#Crie um programa que leia o nome de uma cidade
cidade = str(input('Informe o nome da cidade: '))

#Diga se ela começa ou não com o nome 'SANTO"

#Separando os nomes da cidade
cidade = cidade.split()

#Descobrindo se começa com Santo

if 'SANTO' in cidade[0].upper():
    print(f'A cidade começa com o nome SANTO')

else:
    print(f'A cidade informada não começa com o nome SANTO')

#Outra resolução
cid = str(input('Informe o nome da cidade: ')).upper()

print(cid[:5] == 'SANTO')
