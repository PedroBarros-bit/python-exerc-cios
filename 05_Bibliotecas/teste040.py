import matplotlib.pyplot as plt
import csv

tempo = []
altitude = []

with open('voo_teste.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)

    for linha in leitor:
       
        tempo.append(float(linha[0]))
        altitude.append(float(linha[1]))

print("📊 Gerando gráfico de telemetria...")

plt.plot(tempo, altitude, color='red', marker='x', label='Drone X-1')

plt.title("Análise de Pouso Automático")
plt.xlabel("Tempo (s)")
plt.ylabel("Altitude (m)")
plt.legend() # Mostra a etiqueta "Drone X-1"
plt.grid(True)

plt.show()