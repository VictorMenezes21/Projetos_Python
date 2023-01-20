print('''------------------------------------
Código do País de Origem    Imposto
1                           0%
2                           15%
3                           25%
------------------------------------''')

print('''Código do Produto    Preço Por Grama
1 a 4                0%
5 a 7                15%
8 a 10               25%
------------------------------------''')

codigo = int(input('Digite o código do produto: '))
peso = float(input('Digite o peso do produto em quilos: '))


if codigo < 1 or codigo > 10:
    print('Opção Inválida')

codigo_pais = int(input('Digite o código do país'))
if codigo_pais < 1 or codigo_pais > 3:
    print('Opção Inválida')

if 1 <= codigo <= 4:
    peso = (peso / 1000) * 10

elif 5 <= codigo <= 7:
    preco = (peso / 1000) * 25

elif 8 <= codigo <= 10:
     preco = (peso / 1000) * 25