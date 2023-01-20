#Desenvolva um programa que pergunte a distância de uma viagem em Km.
dist = float(input('Digite a distância da viagem (Km): '))

#Calcule o preço da passagem cobrando R$0,50 por KM para viajens de até 200Km
if dist <= 200:
    preço = dist*0.50
    print(f'A viagem custa R${preço:.2f}')

#E R$0,45 para viajens mais longes
else:
    preço = dist*0.45
    print(f'A viagem custa R${preço:.2f}')