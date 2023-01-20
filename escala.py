import matplotlib.pyplot as plt

# Dados da escala
valores = [10, 20, 30, 40, 50]

# Cria a escala
plt.plot(valores)

# Adiciona etiqueta aos eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Adiciona um título à escala
plt.title('Minha escala')

# Mostra a escala
plt.show()