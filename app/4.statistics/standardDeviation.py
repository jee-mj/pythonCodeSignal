import numpy as np
import pandas as pd
import seaborn as sns

# Load Titanic dataset
titanic_df = sns.load_dataset('titanic')

mean_age = titanic_df['age'].mean()
median_age = titanic_df['age'].median()
mode_age = titanic_df['age'].mode()[0]
stdDev_age = np.std(titanic_df['age'])

print("Standard deviation of age: ", stdDev_age) # Standard deviation of age: 14.526497332334044

