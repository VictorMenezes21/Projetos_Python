#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- À vista dinheiro/cheque: 10% de desconto, - À vista no cartão: 5% de desconto, em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros

print('{:=^40}'.format('LOJAS V.MENEZES'))
valor = float(input('Informe o valor a ser pago: '))

option = int(input('''
Escolha a forma de pagamento:
1. À Vista dinheiro/cheque
2. À vista cartão
3. Parcelado no cartão

R: '''))

if option == 1:
    desconto = valor * 0.10
    print(f'O valor a ser pago é de R${valor-desconto:.2f}')

elif option == 2:
    desconto = valor * 0.05
    print(f'O valor a ser pago é de R${valor-desconto:.2f}')

elif option == 3:
    parcela = int(input('Quantas vezes você gostaria de parcelar?\n'))
    if parcela <= 2:
        valor_parcela = valor / parcela
        print(f'Sua compra será parcelada em {parcela}x de R${valor_parcela:.2f}, no valor total de R${valor:.2f}')

    else:
        juros = valor * 0.20
        valor_parcela = (valor + juros) / parcela
        print(f'Sua compra será parcelada em {parcela}x de R${valor_parcela:.2f}, no valor total de R${valor + juros:.2f}')

else:
    print('\033[1;31mOpção Inválida\033[m')
