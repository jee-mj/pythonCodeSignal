import numpy as np
import pandas as pd
import seaborn as sns

# Load Titanic dataset
titanic_df = sns.load_dataset('titanic')

mean_age = titanic_df['age'].mean()
median_age = titanic_df['age'].median()
mode_age = titanic_df['age'].mode()[0]

print(f"Mean age: {mean_age}") # Mean Age: 29.69911764705882
print(f"Median age: {median_age}") # Median Age: 28.0
print(f"Mode age: {mode_age}") # Mode Age: 24.0