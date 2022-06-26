# -*- coding: utf-8 -*-

from em_waves import Medium, Sine, Gaussian, Rect # Модуль для розв'язку задачі


f_0 = 1.8e9  # [Hz]
E_0 = 10.0  # [V/m]

# Створюємо лінії та задаємо змінні
free_space = Medium(ε_r=1, μ_r=1, σ=0)
medium2 = Medium(ε_r=5, μ_r=2, σ=.04)


wave = Sine(f=f_0, A=E_0)
# wave = Gaussian(rms=1.3)
# wave = Rect(width=4)

wave.add_mediums(medium1=free_space, medium2=medium2)# об'єднуємо лінії
wave.print_data() # виводимо розрахунки
wave.show() # виводимо графік
