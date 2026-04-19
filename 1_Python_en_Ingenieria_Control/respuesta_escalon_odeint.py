"""
Ejemplo 2. Resolución numérica de un sistema de primer orden con odeint.

Este ejemplo resuelve la ecuación:
    dy/dt = (1 / T) * (-y + K * u)

utilizando un solucionador numérico de ecuaciones diferenciales ordinarias.
"""
# Librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def first_order_model(output: float, time: float, gain: float,
                      time_constant: float,
                      input_value: float) -> float:
    """
    Define la ecuación diferencial de un sistema de primer orden.

    Parameters
    ----------
    output : float
        Valor actual de la salida y(t).
    time : float
        Tiempo actual. Se incluye por compatibilidad con odeint.
    gain : float
        Ganancia del sistema, K.
    time_constant : float
        Constante de tiempo del sistema, T.
    input_value : float
        Entrada constante u(t).

    Returns
    -------
    float
        Derivada dy/dt.
    """
    dydt = (1.0 / time_constant) * (-output + gain * input_value)
    return dydt


# Parámetros del sistema
K = 3.0         # Ganancia del sistema
T = 4.0         # Constante de tiempo del sistema
u = 1.0         # Magnitud de la entrada escalón

# Condiciones de simulación
t_start = 0.0
t_stop = 25.0
increment = 1.0
t = np.arange(t_start, t_stop + increment, increment)       # Vector de tiempo
y0 = 0.0        # Condición inicial: y(0) = 0

# Resolución numérica de la EDO
y = odeint(first_order_model, y0, t, args=(K, T, u))

# Gráfica
plt.plot(t, y)
plt.title("Sistema de primer orden usando un solucionador de EDO")
plt.xlabel("t [s]")
plt.ylabel("y(t)")
plt.grid(True)
plt.show()
