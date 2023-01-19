from time import sleep
def imprime_list():
  for item in animais:
    print(f'               {item: ^20}')
animais = ['gato', 'cachorro', 'tigre', 'leão', 'onça pintada', 'raposa', 'lobo', 'baleia', 'galinha', 'penguim']

recepçao = ' BEM VINDO AO MINI AKINATOR '
print(f'\033[1;32m{recepçao:=^50}\033[1;32m')

print('Pense em um dos animais abaixo:\n\n')

imprime_list()

print('\nResponda com 1 (sim) ou 2 (não)')





while True:
  q1 = int(input('Seu animal é felino? '))
  if q1 == 1:
    animais.remove('cachorro')
    animais.remove('raposa')
    animais.remove('lobo')
    animais.remove('baleia')
    animais.remove('galinha')
    animais.remove('penguim')
    q1 = int(input('Seu animal é pintado e/ou listrado? '))
    if q1 == 1:
      animais.remove('gato')
      animais.remove('leão')
      q1 = int(input('Seu animal é brasileiro? '))
      if q1 == 1:
        animais.remove('tigre')
        print('Com base nas minhas informações...\n')
        sleep(2)
        print(f'O animal é {animais[0]}!')
        break
      if q1 == 2:
        animais.remove('onça pintada')
        print('Com base nas minhas informações...\n')
        sleep(2)
        print(f'O animal é {animais[0]}!')
        break
      else:
        print('Resposta inválida')
    if q1 == 2:
      animais.remove('tigre')
      animais.remove('onça pintada')
      q1 = int(input('Seu animal é doméstico? '))
      if q1 == 1:
        animais.remove('leão')
        print('Com base nas minhas informações...\n')
        sleep(2)
        print(f'O animal é {animais[0]}!')
        break
      if q1 == 2:
        animais.remove('gato')
        print('Com base nas minhas informações...\n')
        sleep(2)
        print(f'O animal é {animais[0]}!')
        break
      else:
        print('Reposta inválida')
    else:
      print('Resposta inválida')
  if q1 == 2:
    animais.remove('gato')
    animais.remove('tigre')
    animais.remove('leão')
    animais.remove('onça pintada')
    q1 = int(input('Seu animal é doméstico? '))
    if q1 == 1:
      animais.remove('raposa')
      animais.remove('lobo')
      animais.remove('baleia')
      animais.remove('penguim')
      q1 = int(input('Seu animal é uma ave? '))
      if q1 == 1:
        animais.remove('cachorro')
        print('Com base nas minhas informações...\n')
        sleep(2)
        print(f'O animal é {animais[0]}!')
        break
      if q1 == 2:
        animais.remove('galinha')
        print('Com base nas minhas informações...\n')
        sleep(2)
        print(f'O animal é {animais[0]}!')
        break
      else:
        print('Resposta inválida')
    if q1 == 2:
      animais.remove('galinha')
      animais.remove('cachorro')
      q1 = int(input('Seu animal é aquático? '))
      if q1 == 1:
        animais.remove('raposa')
        animais.remove('lobo')
        q1 = int(input('Seu animal é mamífero? '))
        if q1 == 1:
          animais.remove('penguim')
          print('Com base nas minhas informações...\n')
          sleep(2)
          print(f'O animal é {animais[0]}!')
          break
        if q1 == 2:
          animais.remove('baleia')
          print('Com base nas minhas informações...\n')
          sleep(2)
          print(f'O animal é {animais[0]}!')
          break
        else:
          print('Resposta inválida')
      if q1 == 2:
        animais.remove('penguim')
        animais.remove('baleia')
        q1 = int(input('Seu animal é pequeno? '))
        if q1 == 1:
          animais.remove('lobo')
          print('Com base nas minhas informações...\n')
          sleep(2)
          print(f'O animal é {animais[0]}!')
          break
        if q1 == 2:
          animais.remove('raposa')
          print('Com base nas minhas informações...\n')
          sleep(2)
          print(f'O animal é {animais[0]}!')
          break
        else:
          print('Resposta inválida')
      else:
        print('Reposta inválida')
    else:
      print('Resposta inválida')
  else:
    print('Resposta Inválida')