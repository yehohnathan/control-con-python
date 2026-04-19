"""
Ejemplo 9. Sistema de primer orden con retardo de tiempo.

La función de transferencia estudiada es:
    H(s) = K / (T s + 1) * e^(-tau s)

El retardo se aproxima mediante Padé.
"""

import numpy as np
import matplotlib.pyplot as plt
import control

# Parámetros del sistema de primer orden
k = 3.0
t_const = 4.0

# Parte de primer orden
num = np.array([k])
den = np.array([t_const, 1.0])
h_first = control.tf(num, den)
print("H1(s) =", h_first)

# Parámetros del retardo
tau = 2.0
order = 5

# Aproximación de Padé
num_pade, den_pade = control.pade(tau, order)
h_pade = control.tf(num_pade, den_pade)
print("Hpade(s) =", h_pade)

# Sistema total
h_sys = control.series(h_first, h_pade)
print("H(s) =", h_sys)

# Respuesta al escalón
t, y = control.step_response(h_sys)

# Gráfica
plt.plot(t, y)
plt.title("H(s)")
plt.xlabel("t")
plt.ylabel("y")
plt.grid(True)
plt.show()
