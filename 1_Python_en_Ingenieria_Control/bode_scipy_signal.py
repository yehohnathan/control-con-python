"""
Ejemplo 7. Respuesta en frecuencia usando scipy.signal.

Este ejemplo construye una función de transferencia y calcula su
diagrama de Bode utilizando scipy.signal.bode.
"""
# Librerías necesarias
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# Definición de la función de transferencia
num1 = np.array([3.0])
num2 = np.array([2.0, 1.0])
num = np.convolve(num1, num2)

den1 = np.array([3.0, 1.0])
den2 = np.array([5.0, 1.0])
den = np.convolve(den1, den2)

H = signal.TransferFunction(num, den)
print("H(s) =", H)

# Rango de frecuencias
w_start = 0.01
w_stop = 10.0
step = 0.01
n = int((w_stop - w_start) / step) + 1
w = np.linspace(w_start, w_stop, n)

# Cálculo del Bode
w, mag, phase = signal.bode(H, w)

# Gráficas
plt.figure()

plt.subplot(2, 1, 1)
plt.semilogx(w, mag)
plt.title("Bode Plot")
plt.ylabel("Magnitude (dB)")
plt.grid(True, which="both", axis="both")

plt.subplot(2, 1, 2)
plt.semilogx(w, phase)
plt.ylabel("Phase (deg)")
plt.xlabel("Frequency (rad/sec)")
plt.grid(True, which="both", axis="both")

plt.show()
