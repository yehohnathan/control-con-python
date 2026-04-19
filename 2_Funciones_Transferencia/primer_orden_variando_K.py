"""
Ejemplo 6. Respuesta al escalón de un sistema de primer orden
para distintos valores de la ganancia K.

La función de transferencia utilizada es:
    H(s) = K / (T s + 1)

Se mantiene T constante y se evalúa el efecto de variar K.
"""

import numpy as np
import matplotlib.pyplot as plt
import control

# Constante de tiempo fija
t_const = 10.0

# Valores de la ganancia
k_array = [1.0, 3.0, 5.0, 10.0]

# Vector de tiempo
t_start = 0.0
t_stop = 60.0
t_step = 0.1
t = np.arange(t_start, t_stop, t_step)

# Simulación para distintos valores de K
for k in k_array:
    # Crear función de transferencia
    num = np.array([k])
    den = np.array([t_const, 1.0])
    h_sys = control.tf(num, den)

    print("H(s) =", h_sys)

    # Respuesta al escalón
    t_out, y = control.step_response(h_sys, t)

    # Gráfica
    plt.plot(t_out, y, label=f"K = {k:g}")

# Configuración de la gráfica
plt.title("Step Response for different K")
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
