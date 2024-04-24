import pandas as pd

src = {
  "Name": ["John", "Anna", "Peter"],
  "Age": [28, 24, 33],
  "City": ["New York", "Paris", "Berlin"]
}

dataFrame = pd.DataFrame(src)

print(dataFrame)

"""
    Name  Age         City
0   John   28     New York
1   Anna   24  Los Angeles
2  Peter   33       Berlin
"""