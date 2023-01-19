#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- Equilátero: Todos os lados iguais, - Isósceles: Dois lados iguais, - Escaleno: Todos os lados diferentes.

r1 = int(input('Informe o valor da primeira reta: '))
r2 = int(input('Informe o valor da segunda reta: '))
r3 = int(input('Informe o valor da terceira reta: '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    if r1 == r2 == r3:
        print('\033[1;32mO Triângulo formado é um Equilátero\033[m')

    elif r1 == r2 < r3 or r1 == r2 > r3 or r2 == r3 < r1 or r2 == r3 > r1 or r3 == r1 < r2 or r3 == r1 > r2:
        print('\033[1;32mO Triângulo formado é um Isósceles\033[m')

    else:
        print('\033[1;32mO Triângulo formado é um Escaleno\033[m')



else:
    print('\033[1;31mNão é possível formar um triângulo.\033[m')
