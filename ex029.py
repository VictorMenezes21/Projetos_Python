#Escreva um progama que leia a velocidade de um carro.
vel = float(input('Informe a velocidade do carro: '))
#Se ele ultrapassar 80Km/h. mostre uma mensagem dizendo que ele foi multado
if vel > 80:
    print('Você ultrapassou o limite de velocidade, e por isto foi multado')

    #A multa vai custar R$7.00 por cada km acima do limite.
    multa = (vel-80)*7
    print(f'O valor da multa é de {multa} reais.')

else:
    print('Tenha um bom dia! Dirija com segurança!')