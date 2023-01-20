import operator
from operator import itemgetter, attrgetter

with open('instancias-mochila\KNAPDATA40.txt', 'r') as arquivo:
    arquivos = arquivo.readlines()

peso = arquivos[0]  # Peso total da mochila
peso_atual = 0
total_itens = arquivos[1]  # Numero total de itens
dados = []  # Cria a lista de dados
solucao = []  # Cria uma lista informando se o item será levado ou não / 0 ou 1

# Separando os itens do arquivo
for i, n in enumerate(arquivos):
    if n > arquivos[1]:  # Remove o Peso(15) e Capacidade de Itens(40)
        dados.append(n.split(',', 3))  # Separa os valores de cada item em três colunas (Nome, Peso, Benefício)
        dados[i - 2][1] = int(dados[i - 2][1])  # Converte valor do peso em int
        dados[i - 2][2] = int(dados[i - 2][2])  # Converte valor do beneficio em int
        solucao.append(0)  # Preenche a lista de solução com o valor inicial 0

dados.sort(key=operator.itemgetter(2), reverse=True) # Ordena beneficio decrescente
dados.sort(key=operator.itemgetter(1)) # Ordena peso crescente


def imprime_itens():
    for i in range(40):
        print('=' * 30)
        print(f'''
        Nome: {dados[i][0]}
        Peso: {dados[i][1]}
        Benefício: {dados[i][2]}''')


imprime_itens()
