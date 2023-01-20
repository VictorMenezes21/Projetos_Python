soma = 0
cont = 0
par = 0
n_maior = 0
n_menor = 999999
media = 0
num_digitado = 1
print('Digite 0 para sair do programa')
while num_digitado != 0:
    num_digitado = int(input('Digite um número: '))
    if num_digitado != 0:

        soma = soma + num_digitado
        cont += 1

        if num_digitado > n_maior:
            n_maior = num_digitado

        if num_digitado < n_menor:
            n_menor = num_digitado

        if num_digitado % 2 == 0:
            media += num_digitado
            par += 1

media = media / par

print(f'''
Soma dos números digitados: {soma}
Quantidade dos números digitados: {cont}
Maior número digitado: {n_maior}
Menor número digitado: {n_menor}
Média dos números pares: {media}''')