import matplotlib.pyplot as plt

tempo_segundos = [0, 1, 2, 3, 4, 5, 6]
altitude_metros = [0, 5, 15, 20, 20, 10, 0]

# Criar o gráfico
plt.plot(tempo_segundos, altitude_metros, marker='o', linestyle='--', color='blue')

# Configurar os nomes (Labels)
plt.title("Telemetria de Voo: Altitude vs Tempo")
plt.xlabel("Tempo (s)")
plt.ylabel("Altitude (m)")

# Adicionar uma grade (grid) 
plt.grid(True)

# Mostrar na tela
print("Gerando gráfico")
plt.show()