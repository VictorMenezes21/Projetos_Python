#Crie um algoritmo que leia um número e mostra o seu dobro, triplo e raiz quadrada.

recepção = ' Olá, Tudo bem? '
print(f'{recepção:=^50}')

n = int(input('Digite um número: '))
print(f'O número {n*2} é o dobro de {n}, {n*3} é o triplo e {n**(1/2)} é a sua raiz quadrada!')
