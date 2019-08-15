import numpy as np

a = np.ones((2,3), dtype=int)

b = np.random.random((2,3))

print(a)
print(b)
a *= 3

print(a)

b += a

print(b)

