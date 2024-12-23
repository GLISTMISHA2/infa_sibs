import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Параметры колебательного контура
C = 0.2e-6  # Емкость, Ф
L = 0.2     # Индуктивность, Гн
Q0 = 1e-6   # Максимальный заряд, Кл

# Уравнение колебаний
def circuit(y, t):
    q, i = y  # y — это список [заряд, ток]
    dqdt = i  # Первое уравнение: dq/dt = i
    didt = -(1 / (L * C)) * q  # Второе уравнение: di/dt = -(1/LC) * q
    return [dqdt, didt]

# Начальные условия
y0 = [Q0, 0]  # q(0) = Q0, i(0) = 0

# Время (в пределах двух периодов)
T = 2 * np.pi * np.sqrt(L * C)  # Период колебаний
t = np.linspace(0, 2 * T, 1000)

# Решение уравнения
sol = odeint(circuit, y0, t)
q = sol[:, 0]  # Заряд q(t)
i = sol[:, 1]  # Ток i(t)

# ЭДС индукции
emf = -L * np.gradient(i, t)  # ЭДС = -L * di/dt

# Нормируем время по периоду
t_normalized = t / T  # Время в единицах периода

# Построение графиков
plt.figure(figsize=(12, 10))

# Первый график: заряд на конденсаторе
plt.subplot(3, 1, 1)
plt.plot(t_normalized, q, label="Заряд, q(t)", color="blue")
plt.axvline(1, color="green", linestyle="--", label="Один период (T)")
plt.axvline(2, color="green", linestyle="--", label="Два периода (2T)")
plt.title("Заряд на обкладках конденсатора")
plt.xlabel("Время, t/T")
plt.ylabel("Заряд, q (Кл)")
plt.grid(True)
plt.legend()

# Второй график: ток в цепи
plt.subplot(3, 1, 2)
plt.plot(t_normalized, i, label="Ток, i(t)", color="red")
plt.axvline(1, color="green", linestyle="--", label="Один период (T)")
plt.axvline(2, color="green", linestyle="--", label="Два периода (2T)")
plt.title("Ток в колебательном контуре")
plt.xlabel("Время, t/T")
plt.ylabel("Ток, i (А)")
plt.grid(True)
plt.legend()

# Третий график: ЭДС индукции
plt.subplot(3, 1, 3)
plt.plot(t_normalized, emf, label="ЭДС индукции, E(t)", color="purple")
plt.axvline(1, color="green", linestyle="--", label="Один период (T)")
plt.axvline(2, color="green", linestyle="--", label="Два периода (2T)")
plt.title("ЭДС индукции в контуре")
plt.xlabel("Время, t/T")
plt.ylabel("ЭДС, E (В)")
plt.grid(True)
plt.legend()

# Отображение графиков
plt.tight_layout()
plt.show()
