"""
Ejemplo 9. Simulación de un sistema de primer orden con controlador PI.

Este ejemplo implementa:
1. Un proceso discreto de primer orden.
2. Un controlador PI discreto.
3. La simulación completa en lazo cerrado.

Ecuaciones utilizadas:

    e[k] = r - y[k]

    u[k] = u[k - 1] + Kp * (e[k] - e[k - 1]) + (Kp / Ti) * Ts * e[k]

    y[k + 1] = (1 + Ts * a) * y[k] + Ts * b * u[k]
"""
# Librerías necesarias
import numpy as np
import matplotlib.pyplot as plt

# Parámetros del modelo
K = 3.0             # Ganancia del sistema
T = 4.0             # Constante de tiempo del sistema
a = -(1.0 / T)      # Parámetro a del proceso
b = K / T           # Parámetro b del proceso

# Parámetros de simulación
Ts = 0.1            # Tiempo de muestreo
t_stop = 20.0       # Tiempo final de simulación
n = int(t_stop / Ts)  # Número de iteraciones

# Inicialización de la salida del proceso
y = np.zeros(n + 2)
y[0] = 0.0          # Condición inicial

# Parámetros del controlador PI
Kp = 0.5
Ti = 5.0

# Referencia y variables auxiliares
r = 5.0
e = np.zeros(n + 2)
u = np.zeros(n + 2)

# Simulación del lazo cerrado
for k in range(n + 1):
    e[k] = r - y[k]
    u[k] = u[k - 1] + Kp * (e[k] - e[k - 1]) + (Kp / Ti) * Ts * e[k]
    y[k + 1] = (1 + Ts * a) * y[k] + Ts * b * u[k]

# Vector de tiempo
t = np.arange(0.0, t_stop + 2 * Ts, Ts)

# Gráfica de la salida del proceso
plt.figure(1)
plt.plot(t, y)
plt.title("Control of Dynamic System")
plt.xlabel("t [s]")
plt.ylabel("y")
plt.grid(True)
plt.axis([0.0, t_stop, 0.0, 8.0])
plt.show()

# Gráfica de la señal de control
plt.figure(2)
plt.plot(t, u)
plt.title("Control Signal")
plt.xlabel("t [s]")
plt.ylabel("u [V]")
plt.grid(True)
plt.show()
