"""
Ejemplo 7. Discretización de un modelo en espacio de estados.

Este ejemplo construye un sistema continuo en espacio de estados
utilizando scipy.signal.StateSpace y luego lo convierte a un modelo
discreto con un tiempo de muestreo Ts usando el método de Euler.
"""

# Librerías necesarias
import scipy.signal as sig

# Parámetros del sistema
K = 3.0         # Ganancia del sistema
T = 4.0         # Constante de tiempo del sistema
Ts = 0.1        # Tiempo de muestreo

# Modelo continuo en espacio de estados
A = [[-1.0 / T, 0.0],
     [0.0, 0.0]]
B = [[K / T],
     [0.0]]
C = [[1.0, 0.0]]
D = 0.0

sys_c = sig.StateSpace(A, B, C, D)
print("Sistema continuo:")
print(sys_c)

# Discretización del sistema
sys_d = sys_c.to_discrete(Ts, method="euler")
print("\nSistema discreto:")
print(sys_d)

# Mostrar matrices discretas
print("\nAd =")
print(sys_d.A)

print("\nBd =")
print(sys_d.B)

print("\nCd =")
print(sys_d.C)

print("\nDd =")
print(sys_d.D)
