# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considere US$1.00 = R$5.18

repepçao = ' Olá, Seja Bem Vindo '
print(f'{repepçao:=^50}')

real = float(input('Quanto dinheiro você possui em reais?\nR$'))
dolar = real / 5.18

print(f'Com R${real:.2f}, você consegue comprar US${dolar:.2f}')
print(f'Com {real:.2f} reais, você consegue comprar {dolar:.2f} dólares')
