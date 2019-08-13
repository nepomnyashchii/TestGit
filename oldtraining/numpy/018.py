import pandas as pd
import numpy as np

S = pd.Series([11, 28, 72, 3, 5, 8])
print(S)

# print(S.index)
# print(S.values)

X = np.array([11, 28, 72, 3, 5, 8])
print(X)
print(S.values)
# both are the same type:
print(type(S.values), type(X))