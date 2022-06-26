# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
#print("Розв'язування рівняння тепла")

# основні параметри
plate_length = 50
max_iter_time = 750

alpha = 2
delta_x = 1

delta_t = (delta_x ** 2)/(4 * alpha)
gamma = (alpha * delta_t) / (delta_x ** 2)

# Ініціалізація рішення: сітка u(k, i, j)
u = np.empty((max_iter_time, plate_length, plate_length))

# Початковий стан скрізь всередині сітки
u_initial = 0

# Граничні умови
u_top = 100.0
u_left = 0.0
u_bottom = 0.0
u_right = 0.0

# Початкова умова
u.fill(u_initial)

# Умови країв
u[:, (plate_length-1):, :] = u_top
u[:, :, :1] = u_left
u[:, :1, 1:] = u_bottom
u[:, :, (plate_length-1):] = u_right

# Вирішення задачі із нульовими умовами
# Закоментуйте """ зверху і знизу 
# щоб побачити вирішення задачі із нульовими умовами
# (#""")
"""
# Зміна граничних умов
u_top = 0.0
u_left = 0.0
u_bottom = 0.0
u_right = 0.0

# Змінюємо u_initial (випадкова температура від 28,5 до 55,5 градусів)
#u_initial = 0
u_initial = np.random.uniform(low=28.5, high=55.5, size=(plate_length,plate_length))

# Заміна початкових умов
#u.fill(u_initial)
u[0,:,:] = u_initial
"""

# основний розрахунок
def calculate(u):
    for k in range(0, max_iter_time-1, 1):
        for i in range(1, plate_length-1, delta_x):
            for j in range(1, plate_length-1, delta_x):
                u[k + 1, i, j] = gamma * (u[k][i+1][j] + u[k][i-1][j] +
                                          u[k][i][j+1] + u[k][i][j-1] - 4*u[k][i][j]) + u[k][i][j]

    return u


def plotheatmap(u_k, k):
    # Очищаємо дану фігуру
    plt.clf()

    plt.title(f"Температура при t = {k*delta_t:.3f}")
    plt.xlabel("x")
    plt.ylabel("y")

    # для побудови графіка u_k (u на етапі k)
    plt.pcolormesh(u_k, cmap=plt.cm.jet, vmin=0, vmax=100)
    plt.colorbar()

    return plt


# Розраховуємо
u = calculate(u)

# Функція анімації
def animate(k):
    plotheatmap(u[k], k)


anim = animation.FuncAnimation(
    plt.figure(), animate, interval=1, frames=max_iter_time, repeat=False)
    # викликаємо функції анімації і задаємо параметри

save_name = r"reports/temperature.gif"  # r"reports/temperature1.gif"
# зберігаємо графіки у форматі gif для обох випадків
anim.save(save_name)
#anim.save(save_name)
dir = os.path.abspath(os.curdir)
print(f"Программа завершена.\nРезультат -> {dir + save_name}")