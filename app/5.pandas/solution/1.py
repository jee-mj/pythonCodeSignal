# Importing required libraries
import seaborn as sns
import pandas as pd

# Load Titanic dataset
titanic_df = sns.load_dataset('titanic')

# Filter down to passengers aged between 20 and 30 who did not survive
filtered_data = titanic_df[
    (titanic_df['age'] <= 10) & (titanic_df['survived'] == 1)
]

# Sort the filtered data by fare paid and age
sorted_data = filtered_data.sort_values(['fare', 'age'], ascending=[True, False])

# Display the first 10 rows of the sorted DataFrame
print(sorted_data.head(10))