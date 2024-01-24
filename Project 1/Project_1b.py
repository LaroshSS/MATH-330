import matplotlib.pyplot as plt
import numpy as np
        
x = np.linspace(-2, 2, 100)
y = np.piecewise(x, [x < 0, x >= 0], [0, 1])
plt.plot(x, y)
y = np.piecewise(x, [x < 0, x >= 0], [lambda x: -x, lambda x: x])
plt.plot(x, y)
y = np.piecewise(x, [x < 0, x >= 0], [lambda x: -x**2/2, lambda x: x**2/2])
plt.plot(x, y)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.show()