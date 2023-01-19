from time import sleep

class colors:
    red = '\033[1;31m'
    green = '\033[1;32m'
    end = '\033[m'

contador = 10

while contador >= 0:
    sleep(1)
    print(contador, end='... ')
    contador -= 1

sleep(1)
print('')
print(colors.green + '*' * 15, 'F E L I Z - A N O - N O V O', '*' * 15 + colors.end)
