from time import sleep

print('Olá 2ºSgt MOTA, no que posso ajudar?')
sleep(2)
print('Meu nome é Shirley, a inteligência aritificial do Pyhton')

a = int(input(('''O que você deseja?
[1] Água
[2] Café
[3] Suco
R: ''')))

if a == 1:
    print('Enchendo copo dágua...')
    sleep(1)
    print('Prontinho')

if a == 2:
    print('Enchendo copo de café...')
    sleep(1)
    print('Prontinho')

if a == 3:
    print('Enchendo copo de suco...')
    sleep(1)
    print('Prontinho')


