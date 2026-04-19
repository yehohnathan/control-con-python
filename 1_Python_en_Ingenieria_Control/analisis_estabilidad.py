"""
Ejemplo 10. Análisis de estabilidad de un sistema con controlador PI.

Este ejemplo construye:
1. La función de transferencia del proceso.
2. La función de transferencia del controlador PI.
3. La función de transferencia del sensor.
4. La función de transferencia del filtro.
5. La función de transferencia de lazo L(s).
6. La función de transferencia de seguimiento T(s).

Además, calcula:
- respuesta al escalón,
- diagrama de Bode con márgenes,
- polos y ceros,
- margen de ganancia,
- margen de fase,
- frecuencias de cruce,
- y ganancia crítica.

Nota:
Después de `control.bode_plot(...)` se agrega `plt.show()` para asegurar
que la figura del diagrama de Bode se muestre correctamente antes de
continuar con el mapa de polos y ceros.
"""

# Librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
import control

# Función de transferencia del proceso
K = 3.0
T = 4.0
num_p = np.array([K])
den_p = np.array([T, 1.0])
Hp = control.tf(num_p, den_p)
print("Hp(s) =", Hp)

# Función de transferencia del controlador PI
Kp = 0.4
Ti = 2.0
num_c = np.array([Kp * Ti, Kp])
den_c = np.array([Ti, 0.0])
Hc = control.tf(num_c, den_c)
print("Hc(s) =", Hc)

# Función de transferencia de la medición
Tm = 1.0
num_m = np.array([1.0])
den_m = np.array([Tm, 1.0])
Hm = control.tf(num_m, den_m)
print("Hm(s) =", Hm)

# Función de transferencia del filtro pasa-bajas
Tf = 1.0
num_f = np.array([1.0])
den_f = np.array([Tf, 1.0])
Hf = control.tf(num_f, den_f)
print("Hf(s) =", Hf)

# Función de transferencia de lazo
L = control.series(Hc, Hp, Hf, Hm)
print("L(s) =", L)

# Función de transferencia de seguimiento
T_sys = control.feedback(L, 1)
print("T(s) =", T_sys)

# Respuesta al escalón del sistema realimentado
t, y = control.step_response(T_sys)
plt.figure(1)
plt.plot(t, y, label="Respuesta del sistema")
plt.title("Step Response Feedback System T(s)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

# Diagrama de Bode con márgenes
plt.figure(2)
control.bode_plot(L, dB=True, deg=True, display_margins=True)

# Importante: mostrar la figura del Bode antes de continuar
plt.show()

# Mapa de polos y ceros
plt.figure(3)
control.pzmap(T_sys, plot=True)
plt.title("Pole Zero Map")
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.grid(True)

# Polos y ceros
poles = control.poles(T_sys)
zeros = control.zeros(T_sys)
print("Poles =", poles)
print("Zeros =", zeros)

# Mostrar coordenadas en consola de forma más clara
print("\nCoordenadas de los polos:")
for i, pole in enumerate(poles, start=1):
    print(f"p{i} = ({pole.real:.4f}, {pole.imag:.4f})")

print("\nCoordenadas de los ceros:")
for i, zero in enumerate(zeros, start=1):
    print(f"z{i} = ({zero.real:.4f}, {zero.imag:.4f})")

# Anotar coordenadas en la gráfica
ax = plt.gca()

for pole in poles:
    ax.annotate(
        f"({pole.real:.2f}, {pole.imag:.2f})",
        xy=(pole.real, pole.imag),
        xytext=(8, 8),
        textcoords="offset points",
        fontsize=9
    )

for zero in zeros:
    ax.annotate(
        f"({zero.real:.2f}, {zero.imag:.2f})",
        xy=(zero.real, zero.imag),
        xytext=(8, -12),
        textcoords="offset points",
        fontsize=9
    )

# Márgenes de estabilidad y frecuencias de cruce
gm, pm, w180, wc = control.margin(L)

# Conversión de margen de ganancia a dB
gm_db = 20.0 * np.log10(gm)

print("\nResultados de estabilidad:")
print("wc =", f"{wc:.2f}", "rad/s")
print("w180 =", f"{w180:.2f}", "rad/s")
print("GM =", f"{gm:.2f}")
print("GM =", f"{gm_db:.2f}", "dB")
print("PM =", f"{pm:.2f}", "deg")

# Ganancia crítica
Kc = Kp * gm
print("Kc =", f"{Kc:.2f}")

plt.show()
