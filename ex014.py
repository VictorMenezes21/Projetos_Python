#Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

r = ' Olá, Seja bem vindo! '
print(f'{r:=^50}')

c = float(input('Informe a temperatura em °C: '))
f = 9 * c / 5 + 32

print(f'{c}°C equivale a {f}°F')
