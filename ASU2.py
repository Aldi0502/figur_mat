import numpy as np
import matplotlib.pyplot as plt
import random

from просто.graf import X

#ПЕРЕМЕНЫЕ 
R = 10
alpha = 0


def rotate_system():#будет плавно крутить точку в одном окне графики
    fig, ax = plt.subplots()
    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    ax.set_title("АСУ ТП: Вращение системы")
    for i in range(200):
        alpha += random.uniform(0.05, 0.2)  # Увеличиваем угол поворота
        x = R * np.cos(alpha)  # Вычисляем координату X
        y = R * np.sin(alpha)  # Вычисляем координату Y

        point, = ax.plot([], [], 'mo', markersize=10)
        point.set_data([x], [y])
        fig.canvas.draw() and plt.pause(0.02)
plt.show()