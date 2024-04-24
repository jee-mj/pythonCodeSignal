import pandas as pd

src = {
  "Name": ["John", "Anna", "Peter"],
  "Age": [28, 24, 33],
  "City": ["New York", "Paris", "Berlin"]
}

dataFrame = pd.DataFrame(src)

print("\nHead:\n\n", dataFrame.head(2)) # Get the first (n=2) rows
print("\nTail:\n\n", dataFrame.tail(2)) # Get the last (n=2) rows
print("\nShape:\n\n", dataFrame.shape) # Get the shape of the DataFrame
print("\nColumns:\n\n", dataFrame.columns) # Get the columns of the DataFrame
print("\nData Types:\n\n", dataFrame.dtypes) # Get the data types of the columns

print("\nInfo:\n\n", dataFrame.info()) # Get the information of the DataFrame
