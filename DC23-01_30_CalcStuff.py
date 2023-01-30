import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

for i in np.arange(-10, 11, .01):
    x.append(np.sin(i + np.sin(i)))

for i in np.arange(-10,11, .01):
    y.append(np.cos(i + np.cos(i)))

plt.plot(x,y)

plt.show()