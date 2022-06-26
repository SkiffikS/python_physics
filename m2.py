# -*- coding: utf-8 -*-

# імпорт модулів
import numpy as np # Модуль для роботами із масивами
from scipy import integrate # математичний модуль
from matplotlib import pyplot as plt # модуль для реалізації графіків

plt.close("all")
 
# model_case 1 = Pendulum
# model_case 2 = Double Well

# задаємо необхідні значення
alpha = -1
beta = 1
delta = 2
gam = 1
w = 1

def flow_deriv(x_y_z,tspan):
    # функція для знаходження похідних
    x, y, z = x_y_z
    a = y
    b = delta*np.cos(w*tspan) - alpha*x - beta*x**3 - gam*y
    c = w
    return[a,b,c]
                 
T = 2 * np.pi / w
 
px1 = np.random.rand(1) # масив із одним рандомним значенням
xp1 = np.random.rand(1)
w1 = 0
 
x_y_z = [xp1, px1, w1]
 
# Розміщення траєкторій
t = np.linspace(0, 2000, 40000)
x_t = integrate.odeint(flow_deriv, x_y_z, t)
x0 = x_t[39999,0:3]
 
tspan = np.linspace(1,20000,400000)
x_t = integrate.odeint(flow_deriv, x0, tspan)
siztmp = np.shape(x_t)
siz = siztmp[0]
 
# початкові координати
y1 = x_t[:,0]
y2 = x_t[:,1]
y3 = x_t[:,2]

# створюємо фігуру
plt.figure(2)
lines = plt.plot(y1[1:2000], y2[1:2000], "ko", ms=1)
# додаємо лінії та стилізуємо її
plt.setp(lines, linewidth=0.5)
plt.savefig(r"reports/Duffing")
# виводимо не екран
plt.show()
 
for cloop in range(0,3):
    # цикл із 3 ітераціями для 3 ліній
    #phase = np.random.rand(1)*np.pi;
    phase = np.pi*cloop / 3
 
    repnum = 5000
    px = np.zeros(shape=(2 * repnum,))
    xvar = np.zeros(shape=(2 * repnum,))
    cnt = -1
    testwt = np.mod(tspan-phase, T) - 0.5 * T;
    last = testwt[1]
    for loop in range(2,siz):
        if (last < 0)and(testwt[loop] > 0):
            cnt = cnt+1
            del1 = -testwt[loop - 1] / (testwt[loop] - testwt[loop - 1])
            px[cnt] = (y2[loop] - y2[loop-1]) * del1 + y2[loop - 1]
            xvar[cnt] = (y1[loop] - y1[loop - 1]) * del1 + y1[loop - 1]
            last = testwt[loop]
        else:
            last = testwt[loop]
  
    # створюємо фігури для показу послідовного наростання
    plt.figure(3)
    if cloop == 0:
        lines = plt.plot(xvar, px, "bo", ms=1)
    elif cloop == 1:
        lines = plt.plot(xvar, px, "go", ms=1)
    else:
        lines = plt.plot(xvar, px, "ro", ms=1)
         
    #plt.show()
    # виводимо фігури
 
# зберігаємо основний графік