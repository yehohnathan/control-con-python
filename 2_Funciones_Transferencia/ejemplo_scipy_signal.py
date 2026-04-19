"""
Ejemplo 2. Función de transferencia con scipy.signal.

Este ejemplo crea la función de transferencia:
    H(s) = 2 / (3s + 1)

y calcula su respuesta al escalón.
"""

# ---------------------------------------------------------------------
# Importación de librerías
# ---------------------------------------------------------------------
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------
# Definición de la función de transferencia
# ---------------------------------------------------------------------
num = np.array([2.0])
den = np.array([3.0, 1.0])

h_sys = signal.TransferFunction(num, den)
print("H(s) =", h_sys)

# ---------------------------------------------------------------------
# Respuesta al escalón
# ---------------------------------------------------------------------
t, y = signal.step(h_sys)

# ---------------------------------------------------------------------
# Gráfica de resultados
# ---------------------------------------------------------------------
plt.plot(t, y)
plt.title("Step Response")
plt.xlabel("t")
plt.ylabel("y")
plt.grid(True)
plt.show()
