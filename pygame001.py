nome = 'H'
vida = 10
gravidade = 9.8
vivo = True

def ataque(x):
    print(f'Dano: {x}')


def pulo(y):
    print('Pular: ', y)


def defesa():
    print('Defender')

#Aqui nós chamamos os nossos parâmetros dentro da função
if nome == 'H':
    ataque(30)