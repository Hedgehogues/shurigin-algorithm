import matplotlib.pyplot as plt
import numpy as np


def shurigin_algorithm_debug(x, draw=False, noise=np.array([]), xlim=[]):
    x = list(x) + list(noise)
    mean = np.mean(x)
    i = 0
    if draw:
        plt.figure(figsize=(10, 7))
        plt.plot(0.5, len(x)-1, 'ko')
        plt.plot(mean, len(x)-1, 'co')
    while len(x) >= 2:
        if draw:
            plt.plot(x, [i] * len(x), 'rx')
        i += 1
        x = sorted(x)
        mid = (x[0] + x[-1]) / 2.
        if mid < x[1]:
            x = x[1:]
        elif mid > x[-2]:
            x = x[:-1]
        else:
            x = x[1:-1]
            x.append(mid)
        if draw:
            plt.plot(np.mean(x), i, 'bo')
    if draw:
        plt.title('Работа алгоритма Шурыгина')
        plt.xlabel('Выборка')
        plt.ylabel('Номер шага')
        plt.legend(['Точное значение среднего', 'Среднее значение выборки', 'Состояние выборки на i-м шаге', 'Значение среднего на i-м шаге'])
    if len(xlim) != 0 and draw:
        plt.xlim(xlim)
    return mean, np.mean(x)

def shurigin_algorithm(x):
    x = list(x)
    mean = np.mean(x)
    while len(x) >= 2:
        x = sorted(x)
        mid = (x[0] + x[-1]) / 2.
        if mid < x[1]:
            x = x[1:]
        elif mid > x[-2]:
            x = x[:-1]
        else:
            x = x[1:-1]
            x.append(mid)
    return np.mean(x)
