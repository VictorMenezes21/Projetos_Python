#Simulação de RPG

nome = 'Hero'
vida = 10
ataque = 3
defesa = 2
vivo = True

def main():
    print('Olá aventureiro, no que posso ajudar?')
    print('')
    print('Missões:')
    print('1 - Matar goblins')
    print('2 - Coletar materiais')
    print('3 - Resgatar inocentes')
    print('')

    res = input('Eu escolho: ')

    if res == '1':
        atacar()
    elif res == '2':
        coletar()
    elif res == '3':
        resgatar()
    else:
        print('Hhoho, não tenho essa missão!')



def atacar():
    print('Eu vou matar goblins.')

def coletar():
    print('Eu vou coletar materiais.')

def resgatar():
    print('Vou resgatar os inocentes!')

loop = True
while loop:
    main()