"""
Ejemplo 5. Respuesta al escalón de un sistema de primer orden
para distintos valores de la constante de tiempo T.

La función de transferencia utilizada es:
    H(s) = K / (T s + 1)

Se mantiene K constante y se evalúa el efecto de variar T.
"""

import numpy as np
import matplotlib.pyplot as plt
import control

# Ganancia fija
k = 10.0

# Valores de la constante de tiempo
t_array = [5.0, 10.0, 30.0, 50.0]

# Vector de tiempo
t_start = 0.0
t_stop = 200.0
t_step = 0.1
t = np.arange(t_start, t_stop, t_step)

# Simulación para distintos valores de T
for t_const in t_array:
    # Crear función de transferencia
    num = np.array([k])
    den = np.array([t_const, 1.0])
    h_sys = control.tf(num, den)

    print("H(s) =", h_sys)

    # Respuesta al escalón
    t_out, y = control.step_response(h_sys, t)

    # Gráfica
    plt.plot(t_out, y, label=f"T = {t_const:g}")

# Configuración de la gráfica
plt.title("Step Response for different T")
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
