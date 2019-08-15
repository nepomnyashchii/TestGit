import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 1.01, 0.05)
U = np.hstack((2 * x[:10], 2 - 2 * x[10:]))

plt.plot(x, U)
plt.show()