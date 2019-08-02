import pandas as pd

data = {
    'apples': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}

purchases = pd.DataFrame(data)
# purchases.index = ["row1", "row2", "row3", "row4"]
print(purchases)

