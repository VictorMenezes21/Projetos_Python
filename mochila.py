

with open('instancias-mochila\KNAPDATA40.txt', 'r') as arquivo:
    arquivos = arquivo.readlines()


peso = arquivos[0] #Peso total da mochila
total_itens = arquivos[1] #Capacidade total de itens permitidos
arq = [] # Cria a variável arquivo

#Separando os itens do arquivo
for n in arquivos:
    if n > arquivos[1]: #Remove o Peso(15) e Capacidade de Itens(40)
        arq.append(n.split(',', 3)) #Separa os valores de cada item em três colunas (Nome, Peso, Benefício)


def imprime_itens():
    for i in range(39):
        print('=' * 30)
        print(f'''
        Nome: {arq[i][0]}
        Peso: {arq[i][1]}
        Benefício: {arq[i][2]}''')

nomes = []
pesos = []
utilidade = []
itens = []
peso_atual = 0

for i in arq:
    nomes.append(i[0])
    pesos.append(int(i[1]))
    utilidade.append(int(i[2]))



def escolhe_beneficio():
    peso_item = 0
    while True:
        global peso_atual
        indice = []
        indice = utilidade.index(max(utilidade))
        if peso_item <= int(peso):
            itens.append(nomes[indice])
            peso_item += pesos[indice]
            peso_atual += peso_item
            print(peso_item)
            del utilidade[indice]
            indice = []
            break

escolhe_beneficio()


