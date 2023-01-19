animais = ['gato', 'cachorro', 'baleia', 'sapo', 'cobra', 'jacare', 'tubarão', 'galinha', 'penguim', 'camarao', 'golfinho']

def imprime_lista():
    for item in animais:
        print(f'                                          {item:_^10}')


recepçao = ' BEM VINDO AO MINI-AKINATOR! '
print(f'{recepçao:=^100}')
print('Escolha um dos animais abaixo, mas mantenha no seu pensamento, pois irei adivinhar qual é!\nResponda as perguntas com 1 (sim) ou 2 (não).\n')

imprime_lista()

q1 = int(input('Vamos lá!\nSeu animal é terrestre?\n'))
while q1 == 1 or q1 == 2:
    if q1 == 1:
        q1 = int(input('Seu animal tem pelo?\n'))
        if q1 == 1:
            q1 = int(input('Seu animal é felino?\n'))
            if q1 == 1:
                print('Seu animal é um gato')
                break
            else:
                print('Seu animal é um cachorro!')
                break
        else:
            q2 = int(input('Seu animal é um réptil?\n'))
            if q2 == 1:
                q2 = int(input('Seu animal rasteja?\n'))
                if q2 == 1:
                    print('Seu animal é uma cobra!')
                    break
                else:
                    print('Seu animal é um jacaré!')
                    break
            else:
                q3 = int(input('Seu animal tem pena?\n'))
                if q3 == 1:
                    print('Seu animal é uma galinha!')
                    break
                else:
                    print('Seu animal é um sapo!')
                    break
    if q1 == 2:
        q4 = int(input('Seu animal possui barbatana?\n'))
        if q4 == 1:
            q4 = int(input('Seu animal é um mamífero?\n'))
            if q4 == 1:
                q4 = int(input('Seu animal é o maior animal do mundo?\n'))
                if q4 == 1:
                    print('Seu animal é uma baleia!')
                    break
                else:
                    print('Seu animal é um golfinho!')
                    break
            else:
                print('Seu animal é um tubarão!')
                break
        else:
            q5 = int(input('Seu animal é uma ave?\n'))
            if q5 == 1:
                print('Seu animal é um penguim!')
                break
            else:
                print('Seu animal é um camarão!')
                break
