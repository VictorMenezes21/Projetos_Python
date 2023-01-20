print('~' * 55)
print('\t\t\tPESQUISA TAXA DE MORTALIDADE')
print('~' * 55)
quantidade = int(input('Digite a quantidade de crianças nascidas no período: '))
mes = 0
fim = 'S'
sexo_masculino = 0
sexo_feminino = 0
precoce = 0
while fim not in 'Nn':
    sexo = str(input('Informe o sexo da criança [M/F]: '))
    mes = int(input('Quantos meses a criança viveu: '))

    if mes <= 24:
        precoce += 1

    if sexo in 'Mm':
        sexo_masculino += 1

    if sexo in 'Ff':
        sexo_feminino += 1

    if sexo not in 'MmFf':
        print('Opção Inválida')

    fim = str(input('Deseja continuar? [S/N]: '))

print(f'A Porcentagem das crianças mortas no período é de {((sexo_masculino + sexo_feminino) / quantidade) * 100:.2f}%')
print(f'A Porcentagem de crianças do sexo masculino mortas no período é de {(sexo_masculino / quantidade) * 100:.2f}%')
print(f'A Porcentagem de crianças que morreram com 24 meses ou menos é de {(precoce / quantidade) * 100:.2f}%')
