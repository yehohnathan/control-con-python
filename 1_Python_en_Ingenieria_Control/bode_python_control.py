"""
Ejemplo 8. Respuesta en frecuencia usando la librería control.

Este ejemplo construye una función de transferencia y calcula su
diagrama de Bode utilizando Python Control Systems Library.
"""
# Librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
import control

# Definición de la función de transferencia
num1 = np.array([3.0])
num2 = np.array([2.0, 1.0])
num = np.convolve(num1, num2)

den1 = np.array([3.0, 1.0])
den2 = np.array([5.0, 1.0])
den = np.convolve(den1, den2)

H = control.tf(num, den)
print("H(s) =", H)

# Diagrama de Bode
control.bode(H, dB=True)
plt.title("Bode Plot")
plt.show()
