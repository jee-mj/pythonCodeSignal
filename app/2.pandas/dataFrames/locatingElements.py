import pandas as pd

src = {
  "Name": ["John", "Anna", "Peter"],
  "Age": [28, 24, 33],
  "City": ["New York", "Paris", "Berlin"]
}

dataFrame = pd.DataFrame(src)

# Select by label
print(dataFrame['Name'], '\n')
print(dataFrame[['Name', 'Age']], '\n')

# Select by integer location
print(dataFrame.iloc[1,0], '\n')
print(dataFrame.iloc[:3,1:], '\n')
print(dataFrame.iloc[1:3,1:], '\n')