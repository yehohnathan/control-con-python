"""
Ejemplo 4. Conversión de un modelo en espacio de estados a función de
transferencia utilizando la librería control.

Este ejemplo construye un sistema en espacio de estados y luego lo
convierte a función de transferencia con control.ss2tf().
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

# Construcción del sistema en espacio de estados
sys_ss = control.ss(A, B, C, D)
print("Sistema en espacio de estados:")
print(sys_ss)

# Conversión a función de transferencia
sys_tf = control.ss2tf(sys_ss)
print("Función de transferencia equivalente:")
print(sys_tf)

# Respuesta al escalón de la función de transferencia
t, y = control.step_response(sys_tf, T=t)

# Gráfica
plt.plot(t, y)
plt.title("Respuesta al escalón")
plt.xlabel("t [s]")
plt.ylabel("y(t)")
plt.grid(True)
plt.show()
