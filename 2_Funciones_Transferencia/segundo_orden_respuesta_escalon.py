"""
Ejemplo 10. Respuesta al escalón de una función de transferencia
de segundo orden.

Se estudia la función de transferencia:
    H(s) = K / (a s^2 + b s + c)

Además, se muestra una forma equivalente escrita como producto
de dos términos de primer orden:
    H(s) = K / ((T1 s + 1)(T2 s + 1))
"""

import numpy as np
import matplotlib.pyplot as plt
import control

# Parámetros de la función de transferencia de segundo orden
k = 4.0
a = 3.0
b = 2.0
c = 1.0

# Crear función de transferencia en su forma general
num = np.array([k])
den = np.array([a, b, c])
h_sys = control.tf(num, den)

print("Función de transferencia de segundo orden:")
print("H(s) =", h_sys)
print()

# Parámetros de una forma factorizada equivalente
t1 = 1.0
t2 = 2.0

# Crear función de transferencia como producto de dos términos
# de primer orden
h_factored = control.tf([k], np.polymul([t1, 1.0], [t2, 1.0]))

print("Función de transferencia factorizada:")
print("Hf(s) =", h_factored)
print()

# Calcular respuesta al escalón de la forma general
t_general, y_general = control.step_response(h_sys)

# Calcular respuesta al escalón de la forma factorizada
t_factored, y_factored = control.step_response(h_factored)

# Graficar ambas respuestas
plt.plot(t_general, y_general, label="Forma general")
plt.plot(t_factored, y_factored, "--", label="Producto de 1er orden")

# Configuración de la gráfica
plt.title("Step Response of a 2nd Order Transfer Function")
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
