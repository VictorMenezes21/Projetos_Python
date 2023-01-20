from prettytable import PrettyTable

# Cria a tabela
tabela = PrettyTable()

# Adiciona as colunas
tabela.field_names = ['Nome', 'Idade']

# Alinha as colunas à direita
tabela.align['Nome'] = 'l'
tabela.align['Idade'] = 'r'

# Adiciona os cabecalhos
tabela.hrules = 1
tabela. vrules = 1

# Adicionar as linhas
tabela.add_row(['João', 35])
tabela.add_row(['Maria', 28])
tabela.add_row(['José', 55])
tabela.add_row(['Victor', 21])

# Imprime tabela
print(tabela)