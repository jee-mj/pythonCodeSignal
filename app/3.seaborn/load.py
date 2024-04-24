import pandas as pd
import seaborn as sns

# Load the titanic dataset into a Pandas DataFrame
dataFrame_titanic = sns.load_dataset('titanic')

# Look at the first 3 rows of the dataframe
print(dataFrame_titanic)

"""
   survived  pclass     sex   age  ...  deck  embark_town  alive  alone
0         0       3    male  22.0  ...   NaN  Southampton     no  False
1         1       1  female  38.0  ...     C    Cherbourg    yes  False
2         1       3  female  26.0  ...   NaN  Southampton    yes   True

[3 rows x 15 columns]
"""