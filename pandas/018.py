import pandas as pd

df = pd.read_csv('zillow.csv', index_col=0, skipinitialspace=True)

def rating_function(x):
    if x >= 4.0:
        return "good"
    else:
        return "bad"

data = df["Beds"].apply(rating_function)

print(data)





