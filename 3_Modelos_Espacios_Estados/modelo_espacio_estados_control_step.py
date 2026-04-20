"""
Ejemplo 3. Respuesta al escalón de un sistema en espacio de estados
utilizando la librería control.

Este ejemplo construye un sistema en espacio de estados con:
    x_dot = A x + B u
    y     = C x + D u

y calcula su respuesta al escalón.
"""

# Librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
import control

# Parámetros del sistema
K = 3.0         # Ganancia del sistema
T = 4.0         # Constante de tiempo del sistema

# Parámetros de simulación
start = 0.0
stop = 30.0
step = 1.0
t = np.arange(start, stop, step)

# Modelo en espacio de estados
A = np.array([[-1.0 / T, 0.0],
              [0.0, 0.0]])
B = np.array([[K / T],
              [0.0]])
C = np.array([[1.0, 0.0]])
D = np.array([[0.0]])

# Construcción del sistema
sys = control.ss(A, B, C, D)
print("Sistema en espacio de estados:")
print(sys)

# Respuesta al escalón
t, y = control.step_response(sys, T=t)

# Gráfica
plt.plot(t, y)
plt.title("Respuesta al escalón")
plt.xlabel("t [s]")
plt.ylabel("y(t)")
plt.grid(True)
plt.show()
