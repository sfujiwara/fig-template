## -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    normal = np.random.normal(size=10000)
    uniform = np.random.uniform(low=-1, high=1, size=10000)

    plt.boxplot([normal, uniform])
    plt.xticks([1,2], ['normal', 'uniform'])
    plt.xlabel('distributions')
    plt.ylabel('values')
    plt.grid()
    plt.show()
