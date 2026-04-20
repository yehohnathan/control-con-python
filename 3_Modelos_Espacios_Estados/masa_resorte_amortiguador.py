"""
Ejemplo 7. Simulación de un sistema masa-resorte-amortiguador.

Este ejemplo:
1. Define los parámetros físicos del sistema.
2. Construye el modelo en espacio de estados.
3. Simula la respuesta del sistema ante una fuerza constante.
4. Grafica la posición y la velocidad de la masa.

El sistema está dado por:

    x1_dot = x2
    x2_dot = (1 / m) * (F - c*x2 - k*x1)

donde:
- x1 es la posición,
- x2 es la velocidad.
"""

# Librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

# Parámetros del sistema
c = 4.0   # Constante de amortiguamiento
k = 2.0   # Rigidez del resorte
m = 20.0  # Masa
F = 5.0   # Fuerza constante aplicada

# Señal de entrada
Ft = np.ones(610) * F

# Parámetros de simulación
tstart = 0.0
tstop = 60.0
increment = 0.1
t = np.arange(tstart, tstop + 1.0, increment)

# Matrices del sistema
A = [[0.0, 1.0], [-k / m, -c / m]]
B = [[0.0], [1.0 / m]]
C = [[1.0, 0.0]]
D = 0.0

# Modelo en espacio de estados
sys = sig.StateSpace(A, B, C, D)

# Simulación del sistema
t, y, x = sig.lsim(sys, Ft, t)

# Extracción de estados
x1 = x[:, 0]
x2 = x[:, 1]

# Gráfica de resultados
plt.plot(t, x1, label="x1(t) = posición")
plt.plot(t, x2, label="x2(t) = velocidad")
# plt.plot(t, y, label="y(t) = salida")

plt.title("Simulation of Mass-Spring-Damper System")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.grid(True)
plt.legend()
plt.show()
