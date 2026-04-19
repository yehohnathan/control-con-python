"""
Ejemplo 4. Función de transferencia usando el operador de Laplace.

Este ejemplo define:
    s = control.TransferFunction.s

y luego construye la función de transferencia:
    H(s) = 2 / (3s + 1)

de forma algebraica.
"""

# ---------------------------------------------------------------------
# Importación de librerías
# ---------------------------------------------------------------------
import control
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------
# Definición del operador de Laplace
# ---------------------------------------------------------------------
s = control.TransferFunction.s

# ---------------------------------------------------------------------
# Definición algebraica de la función de transferencia
# ---------------------------------------------------------------------
h_sys = 2.0 / (3.0 * s + 1.0)
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
