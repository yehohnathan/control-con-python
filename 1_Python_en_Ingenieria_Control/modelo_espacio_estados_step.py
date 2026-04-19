"""
Ejemplo 5. Respuesta al escalón de un sistema en espacio de estados.

Este ejemplo construye un sistema en espacio de estados utilizando
scipy.signal.StateSpace y calcula su respuesta al escalón.

El modelo usado es:

    x_dot = A x + B u
    y     = C x + D u
"""
# Librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

# Parámetros del sistema
K = 3.0         # Ganancia del sistema
T = 4.0         # Constante de tiempo del sistema

# Parámetros de simulación
x0 = [0.0, 0.0]     # Condiciones iniciales de los estados
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

# Respuesta al escalón
t, y = sig.step(sys, X0=x0, T=t)

# Gráfica
plt.plot(t, y)
plt.title("Respuesta al escalón")
plt.xlabel("t [s]")
plt.ylabel("y(t)")
plt.grid(True)
plt.show()
