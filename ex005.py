nome = 'Victor'
print(f'Olá, {nome:=^20}')

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
print(f'A soma de vale {n1+n2}, o produto vale {n1*n2}, a divisão vale {n1/n2}, a potência {n1**n2}', end=' e ')
print(f'a divisão inteira é {n1//n2}')