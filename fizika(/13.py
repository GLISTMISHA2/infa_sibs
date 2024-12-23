import numpy as np
import matplotlib.pyplot as plt

# Параметры
beta = 0.5  # Коэффициент затухания
omega_0 = 5  # Собственная частота
omega_d = np.sqrt(omega_0**2 - beta**2)  # Частота затухающего колебания
A = 1  # Амплитуда
phi = 0  # Начальная фаза
T = 2 * np.pi / omega_d  # Период затухающих колебаний

# Временной интервал для двух периодов
n_periods = 2  # Количество периодов
t_in_periods = np.linspace(0, n_periods, 500)  # Время в периодах

# Решение уравнения
x = A * np.exp(-beta * t_in_periods * T) * np.cos(omega_d * t_in_periods * T + phi)

# Построение графика
plt.plot(t_in_periods, x)
plt.title('Затухающие колебания пружинного маятника')
plt.xlabel('Период, T')
plt.ylabel('Амплитуда, м')
plt.grid(True)
plt.show()
