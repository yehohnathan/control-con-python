"""
Ejemplo 3. Simulación discreta de un sistema de primer orden.

Este ejemplo implementa la ecuación en diferencias obtenida mediante
el método de Euler hacia adelante:

    y[k + 1] = (1 + a * Ts) * y[k] + Ts * b * u[k]

donde:
    a = -1 / T
    b = K / T
"""
# Librerías necesarias
import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
K = 3.0         # Ganancia del sistema
T = 4.0         # Constante de tiempo del sistema

a = -1.0 / T    # Parámetro a del modelo
b = K / T       # Parámetro b del modelo

# Parámetros de simulación
Ts = 0.1        # Tiempo de muestreo
t_stop = 30.0   # Tiempo final de simulación
u_k = 1.0       # Entrada escalón
y_k = 0.0       # Valor inicial de la salida

n = int(t_stop / Ts)    # Número de iteraciones

# Almacenamiento de resultados
data = []
data.append(y_k)

# Simulación
for _ in range(n):
    y_k1 = (1 + a * Ts) * y_k + Ts * b * u_k
    y_k = y_k1
    data.append(y_k1)

# Vector de tiempo
t = np.arange(0.0, t_stop + Ts, Ts)

# Gráfica
plt.plot(t, data)
plt.title("Sistema dinámico de primer orden")
plt.xlabel("t [s]")
plt.ylabel("y(t)")
plt.grid(True)
plt.show()
