"""
Ejemplo 7. Respuesta al escalón de un integrador.

La función de transferencia utilizada es:
    H(s) = K / s
"""

import numpy as np
import matplotlib.pyplot as plt
import control

# Ganancia del integrador
k = 10.0

# Numerador y denominador
num = np.array([k])
den = np.array([1.0, 0.0])

# Crear función de transferencia
h_sys = control.tf(num, den)
print("H(s) =", h_sys)

# Respuesta al escalón
t, y = control.step_response(h_sys)

# Gráfica
plt.plot(t, y)
plt.title("Step Response")
plt.xlabel("t")
plt.ylabel("y")
plt.grid(True)
plt.show()
