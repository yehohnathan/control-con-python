"""
Ejemplo 8. Aproximación de Padé para un retardo de tiempo.

Este ejemplo aproxima:
    H(s) = e^(-tau s)

usando distintos órdenes de Padé y compara sus respuestas al escalón.
"""

import numpy as np
import matplotlib.pyplot as plt
import control

# Retardo de tiempo
tau = 2.0

# Órdenes de aproximación
orders = [1, 2, 3, 5, 10]

# Vector de tiempo
t_start = 0.0
t_stop = 10.0
t_step = 0.1
t = np.arange(t_start, t_stop, t_step)

# Simulación para distintos órdenes de Padé
for n in orders:
    # Aproximación de Padé
    num_pade, den_pade = control.pade(tau, n)
    h_pade = control.tf(num_pade, den_pade)

    print("Hpade(s) =", h_pade)

    # Respuesta al escalón
    t_out, y = control.step_response(h_pade, t)

    # Gráfica
    plt.plot(t_out, y, label=f"N = {n}")

# Configuración de la gráfica
plt.title("Pade Approximations")
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
