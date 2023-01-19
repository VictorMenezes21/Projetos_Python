
monstros = ['Dragão', 'Rei', 'Dragão', 'Dragão', 'Rei']

def atacar():
    print('Atacar dragão')

def defender():
    print('Defender o rei')

for n in monstros:
    if n == 'Dragão':
        atacar()
    elif n == 'Rei':
        defender()