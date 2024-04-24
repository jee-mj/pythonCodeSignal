# Essentially, lambdas in python are similar to lambda functions in JavaScript. They are anonymous functions that can take any number of arguments, but can only have one expression. They are used to perform simple operations on data, and are often used in conjunction with the apply() method in pandas dataframes. The apply() method is used to apply a function along the axis of a dataframe. In the example below, we use the apply() method to add a new column to the dataframe that indicates whether the person is youthful or not based on their age, calculated using a lambda function.

import pandas as pd

src = {
  "Name": ["John", "Anna", "Peter"],
  "Age": [28, 24, 33],
  "City": ["New York", "Los Angeles", "Berlin"]
}

dataFrame = pd.DataFrame(src)

dataFrame["IsYouthful"] = dataFrame["Age"].apply(lambda age: "Yes" if ((age/30) < 1) else "No")
print(dataFrame)

"""
    Name  Age            City IsYouthful
0   John   28        New York        Yes
1   Anna   24     Los Angeles        Yes
2  Peter   33          Berlin         No
"""