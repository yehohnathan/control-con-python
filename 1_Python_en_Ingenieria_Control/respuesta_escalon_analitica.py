"""
Ejemplo 1. Gráfica de la respuesta al escalón de un sistema de primer orden.

Este ejemplo utiliza directamente la solución analítica:
    y(t) = K * U * (1 - exp(-t / T))

Se asume una entrada escalón de magnitud U = 1.
"""
# Librerías necesarias
import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
K = 3.0         # Ganancia del sistema
T = 4.0         # Constante de tiempo del sistema
U = 1.0         # Magnitud de la entrada escalón

# Configuración del tiempo de simulación (Vector de tiempo)
start = 0.0
stop = 30.0
increment = 0.1
t = np.arange(start, stop, increment)

# Cálculo de la respuesta
y = K * U * (1 - np.exp(-t / T))

# Gráfica
plt.plot(t, y)
plt.title("Sistema dinámico de primer orden")
plt.xlabel("t [s]")
plt.ylabel("y(t)")
plt.grid(True)
plt.show()
