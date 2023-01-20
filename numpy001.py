import numpy as np

v_uni = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print('Vetor: ', end='')
print(v_uni)
print('~' * 100)

print('Comprimento Len do Vetor: ', end='')
print(len(v_uni))
print('~' * 100)

print('Dimensões do Vetor: ', end='')
print(v_uni.ndim)
print('~' * 100)

print('Retorno da Função Shape: ', end='')
print(f'{v_uni.shape}')
print('~' * 100)

print('Variável pares com números pares extraídos do vetor: Pares = ', end='')
pares = []
for c in v_uni:
    if c % 2 == 0:
        pares.append(c)
print(pares)
print('~' * 100)

print('Substituindo elementos ímpares do vetor por -1, ordenando os resultados: ')

