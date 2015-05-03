## -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    ## Set parameters
    plt.rcParams['axes.labelsize'] = 24
    plt.rcParams['lines.linewidth'] = 5
    plt.rcParams['legend.fontsize'] = 18
    plt.rcParams['legend.shadow'] = False
    plt.rcParams['xtick.labelsize'] = 14
    plt.rcParams['ytick.labelsize'] = 14

    ## Example data
    x = np.linspace(0, 5*np.pi, 10)
    y1 = np.sin(x)
    y2 = np.cos(x)
    err = np.random.normal(size=10)

    plt.plot(x, y1, label=r'$\sin x$')
    plt.errorbar(x, y2, yerr=err,
                 label=r'$\cos x \pm$ error', elinewidth=3, capsize=5)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$\sin x$')
    plt.grid()
    plt.legend(loc='lower right')
    plt.show()
