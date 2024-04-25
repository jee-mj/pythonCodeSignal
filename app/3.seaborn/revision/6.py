# Import the necessary libraries
import pandas as pd
import seaborn as sns

# TODO: Load the Titanic dataset into a pandas DataFrame
titanic = sns.load_dataset('titanic')
dataFrame = pd.DataFrame(titanic)

# TODO: Output the first 5 rows of the DataFrame
print("\nFirst 5 rows:\n\n",dataFrame.iloc[:5])

# TODO: Create a new column, "IsChild", to identify the passengers who are under 18
dataFrame["IsChild"] = dataFrame["age"].apply(lambda i: "No" if i >= 18 else "Yes")

# TODO: Output the DataFrame after the addition of the 'IsChild' column
print("\nAfter adding 'IsChild' field:\n\n", dataFrame)