''' VÁRIAVEIS COMPOSTAS ( T U P L A S ) '''

# AS TUPLAS SÃO IMUTÁVEIS

lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'

#print(lanche[::-1])

for comida in lanche:
   print(comida, end=' ')

for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {pos}')

#for cont in range(0, len(lanche)):
  #  print(lanche[cont])

#c = 0
#while c < len(lanche):
 #   print(lanche[c])
  #  c += 1
