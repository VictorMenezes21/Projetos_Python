#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
#a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
#custa R$60 por dia e R$0,15 por Km rodado.

r = ' Aluguel de Carro '
print(f'{r:=^80}')

km = int(input('Informe a quantidade de Km percorridos: '))
dias = int(input('Informe a quantidade de dias alugado: '))

pagamento = (km*0.15) + (dias*60)

print(f'O valor a ser pago é de R${pagamento:.2f}.')
