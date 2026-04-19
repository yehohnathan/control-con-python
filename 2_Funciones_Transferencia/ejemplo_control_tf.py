"""
Ejemplo 3. Función de transferencia con la librería control.

Este ejemplo crea la función de transferencia:
    H(s) = 2 / (3s + 1)

y calcula su respuesta al escalón utilizando control.tf().
"""

# ---------------------------------------------------------------------
# Importación de librerías
# ---------------------------------------------------------------------
import numpy as np
import control
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------
# Definición de la función de transferencia
# ---------------------------------------------------------------------
num = np.array([2.0])
den = np.array([3.0, 1.0])

h_sys = control.tf(num, den)
print("H(s) =", h_sys)

# ---------------------------------------------------------------------
# Respuesta al escalón
# ---------------------------------------------------------------------
t, y = control.step_response(h_sys)

# ---------------------------------------------------------------------
# Gráfica de resultados
# ---------------------------------------------------------------------
plt.plot(t, y)
plt.title("Step Response")
plt.xlabel("t")
plt.ylabel("y")
plt.grid(True)
plt.show()
