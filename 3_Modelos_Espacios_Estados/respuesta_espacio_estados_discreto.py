"""
Ejemplo 8. Respuesta al escalón de un modelo discreto en espacio de estados.

Este ejemplo parte de un sistema continuo en espacio de estados,
lo discretiza usando Euler hacia adelante y luego calcula su
respuesta al escalón.
"""

# Librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

# Parámetros del sistema
K = 3.0         # Ganancia del sistema
T = 4.0         # Constante de tiempo del sistema
Ts = 0.5        # Tiempo de muestreo

# Modelo continuo en espacio de estados
A = [[-1.0 / T, 0.0],
     [0.0, 0.0]]
B = [[K / T],
     [0.0]]
C = [[1.0, 0.0]]
D = 0.0

sys_c = sig.StateSpace(A, B, C, D)

# Discretización
sys_d = sys_c.to_discrete(Ts, method="euler")

# Respuesta al escalón del sistema discreto
t, y = sig.dstep(sys_d)

# Convertir salida a arreglos para graficar
t = np.squeeze(t)
y = np.squeeze(y)

# Gráfica
plt.step(t, y, where="post")
plt.title("Respuesta al escalón del sistema discreto")
plt.xlabel("t [s]")
plt.ylabel("y[k]")
plt.grid(True)
plt.show()
