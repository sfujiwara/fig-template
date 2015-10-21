# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


# Parameters used frequently
plt.rcParams['axes.labelsize'] = 24
plt.rcParams['lines.linewidth'] = 4
plt.rcParams['lines.markersize'] = 10
plt.rcParams['lines.markeredgewidth'] = 3
plt.rcParams['legend.fontsize'] = 18
plt.rcParams['legend.shadow'] = False
plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 14

elw = 3
cs = 5

# Example data
x = np.linspace(0, 5*np.pi, 10)
y1 = np.sin(x)
y2 = np.cos(x)
err = np.random.normal(size=10)

plt.plot(x, y1, label=r'sin x')
plt.errorbar(
    x, y2,
    yerr=err,
   label='cos x',
   elinewidth=elw,
   capsize=cs,
   fmt = 'g--x'
)
plt.xlabel('x')
plt.ylabel('sin x')
plt.grid()
plt.legend(loc='lower right')
plt.show()
