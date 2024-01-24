import matplotlib.pyplot as plt
import numpy as np
        
x = np.linspace(-1, 6, 100)
y = np.log(x)
plt.plot(x, y)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlim(-1, 6)
plt.ylim(-2, 3)
plt.scatter(1, 0, color='black')
plt.scatter(np.exp(1), np.log(np.exp(1)), color='black')
y = x - 1
plt.plot(x, y, color='red', linestyle='dashed')
y = x/np.exp(1)
plt.plot(x, y, color='grey', linestyle='dashed')
plt.show()