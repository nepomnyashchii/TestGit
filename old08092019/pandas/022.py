# import pandas and numpy
import pandas as pd
import numpy as np

# creating simple array
data = np.array(['g','e','e','k','s','f', 'o','r','g','e','e','k','s'])
ser = pd.Series(data)


#retrieve the first element
print(ser[:5])