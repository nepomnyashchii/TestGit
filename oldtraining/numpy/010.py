import numpy as np
from numpy import pi

# print(np.arange( 10, 30, 5 ))

# print(np.arange( 0, 2, 0.3 ))

# print(np.linspace( 0, 2, 9 ))

x = np.linspace( 0, 2*pi, 100 )

f = np.sin(x)

print(f)