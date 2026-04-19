"""
Ejemplo 4. Función de transferencia de un sistema de primer orden.

Este ejemplo construye la función de transferencia:
    H(s) = K / (T s + 1)

y calcula su respuesta al escalón utilizando la librería
Python Control Systems Library.
"""
# Librerías necesarias
import control
import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
K = 3.0         # Ganancia del sistema
T = 4.0         # Constante de tiempo del sistema

# Numerador y denominador de la función de transferencia
num = np.array([K])
den = np.array([T, 1.0])

# Construcción de la función de transferencia
H = control.tf(num, den)
print("H(s) =", H)

# Respuesta al escalón
t, y = control.step_response(H)

# Gráfica
plt.plot(t, y)
plt.title("Respuesta al escalón")
plt.xlabel("t [s]")
plt.ylabel("y(t)")
plt.grid(True)
plt.show()
