# importing pandas module
import pandas as pd

# making data frame
df = pd.read_csv("zillow.csv", index_col=0, skipinitialspace=True)

ser = pd.Series(df["Beds"])
print(ser)
data = ser.head(10)
print(data)
