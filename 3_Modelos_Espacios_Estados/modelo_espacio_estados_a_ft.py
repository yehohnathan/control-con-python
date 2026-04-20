"""
Ejemplo 2. Conversión de un modelo en espacio de estados a función de
transferencia.

Este ejemplo construye un sistema en espacio de estados y luego convierte
esa representación a función de transferencia usando scipy.signal.
"""
# Librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

# Parámetros del sistema
K = 3.0         # Ganancia del sistema
T = 4.0         # Constante de tiempo del sistema

# Parámetros de simulación
x0 = [0.0, 0.0]
start = 0.0
stop = 30.0
step = 1.0
t = np.arange(start, stop, step)

# Modelo en espacio de estados
A = [[-1.0 / T, 0.0],
     [0.0, 0.0]]
B = [[K / T],
     [0.0]]
C = [[1.0, 0.0]]
D = 0.0

sys = sig.StateSpace(A, B, C, D)

# Conversión a función de transferencia
H = sys.to_tf()
print(H)

# Respuesta al escalón de la función de transferencia
t, y = sig.step(H, X0=x0, T=t)

# Gráfica
plt.plot(t, y)
plt.title("Respuesta al escalón")
plt.xlabel("t [s]")
plt.ylabel("y(t)")
plt.grid(True)
plt.show()
