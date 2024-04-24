import pandas as pd

src = {
  "Name": ["John", "Anna", "Peter"],
  "Age": [28, 24, 33],
  "City": ["New York", "Paris", "Berlin"]
}

dataFrame = pd.DataFrame(src)

dataFrame["IsYouthful"] = dataFrame["Age"].apply(lambda age: "Yes" if ((age/30) < 1) else "No")

inputData = pd.DataFrame({"Name": ["Megan"], "Age": [34], "City": ["San Francisco"], "IsYouthful": ["No"]})

dataFrameOutput = pd.concat([dataFrame, inputData], ignore_index=True)

print(dataFrameOutput)

"""
    Name  Age           City IsYouthful
0   John   28       New York        Yes
1   Anna   24    Los Angeles        Yes
2  Peter   33         Berlin         No
3  Megan   34  San Francisco         No
"""