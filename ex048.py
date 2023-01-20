#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        cont += 1
        soma += n
        print(n, end=' ')

print(f'\nA soma de todos os {cont} valores solicitados é {soma}')
