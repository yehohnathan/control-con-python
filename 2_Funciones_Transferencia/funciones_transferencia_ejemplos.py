"""
Ejemplo 1. Creación de distintas funciones de transferencia en Python.

Este script agrupa varios ejemplos clásicos de funciones de transferencia:
1. Sistema de primer orden.
2. Sistema con integrador.
3. Sistema de segundo orden.
4. Sistema con numerador de primer grado.

Cada función de transferencia se imprime identificada en consola.

Nota:
El caso con retardo de tiempo no se incluye aquí como una función racional
directa, ya que el término exp(-tau * s) requiere tratamiento adicional,
por ejemplo, aproximación de Padé.
"""
# Librerías necesarias
import numpy as np
import control

# Ejemplo 1: sistema de primer orden
num_1 = np.array([2.0])
den_1 = np.array([3.0, 1.0])
h_1 = control.tf(num_1, den_1)

print("Función de transferencia 1: sistema de primer orden")
print("H1(s) =", h_1)
print()

# Ejemplo 2: sistema con integrador
num_2 = np.array([3.0])
den_2 = np.array([2.0, 1.0, 0.0])
h_2 = control.tf(num_2, den_2)

print("Función de transferencia 2: sistema con integrador")
print("H2(s) =", h_2)
print()

# Ejemplo 3: sistema de segundo orden
num_3 = np.array([4.0])
den_3 = np.array([3.0, -2.0, 1.0])
h_3 = control.tf(num_3, den_3)

print("Función de transferencia 3: sistema de segundo orden")
print("H3(s) =", h_3)
print()

# Ejemplo 4: sistema con numerador de primer grado
num_4 = np.array([4.0, 1.0])
den_4 = np.array([2.0, 5.0, -2.0])
h_4 = control.tf(num_4, den_4)

print("Función de transferencia 4: numerador de primer grado")
print("H4(s) =", h_4)
print()
