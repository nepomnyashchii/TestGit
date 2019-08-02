import pandas as pd

data = {
    'apples': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}

purchases = pd.DataFrame(data, index=["John", "Alex", "Mary", "Mike"])
purchases2 = purchases.loc["John"]
# purchases.index = ["row1", "row2", "row3", "row4"]
print(purchases)
print(purchases2)
