## -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    params = {#'backend': 'ps',  
              'axes.labelsize': 24,
              #'text.fontsize': 18,
              #'legend.fontsize': 28,
              'legend.fontsize': 24,
              'xtick.labelsize': 14,
              'ytick.labelsize': 14,
              #'text.usetex': False,
              }
    plt.rcParams.update(params)

    x = np.linspace(0, 5*np.pi, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    err = np.random.normal(size=100)

    plt.plot(x, y1, label=r'$\sin x$', lw=5)
    plt.errorbar(x, y2, yerr=err, label=r'$\cos x \pm$ error', lw=5, elinewidth=3, capsize=5)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$\sin x$')
    plt.grid()
    plt.legend(shadow=True, prop={'size': 18}, loc='lower right')
    plt.show()
