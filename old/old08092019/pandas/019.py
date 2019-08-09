import pandas as pd

df = pd.read_csv('zillow.csv', index_col=0, skipinitialspace=True)

x=df[df['Beds']]
def rating_function(x):
    if x>= 5:
        return "good"
    else:
        return "bad"

data = df["Beds"].apply(rating_function)

print(data)





