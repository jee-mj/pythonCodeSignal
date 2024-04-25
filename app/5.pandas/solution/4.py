# Import required libraries
import seaborn as sns
import pandas as pd

# TODO: Load the Titanic dataset
dataFrame = sns.load_dataset('titanic')

# TODO: Filter data for third-class passengers who survived and are older than 40
dataFrame_filterSurvivedElders = dataFrame[
  (dataFrame['survived'] == 1) & (dataFrame['age'] > 40) & (dataFrame['pclass'] == 3)
]

# TODO: Sort the filtered data by age in ascending order
dataFrame_sortSurvivedElders_ageAscending = dataFrame_filterSurvivedElders.sort_values('age', ascending=True)

# TODO: Print the sorted data
print(dataFrame_sortSurvivedElders_ageAscending)