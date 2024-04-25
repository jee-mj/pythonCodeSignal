# Import necessary libraries
import pandas as pd
import seaborn as sns

# Load Titanic dataset
titanic_df = sns.load_dataset('titanic')

# TODO: Compute and print the mean, median, and mode of passenger's age
print(f"Mean age: {titanic_df['age'].mean()}")
print(f"Median age: {titanic_df['age'].median()}")
print(f"Mode age: {titanic_df['age'].mode().iloc[0]}")

# Import Numpy
import numpy as np

# TODO: Compute and print the standard deviation of the ages
print(f"Standard deviation of age: {np.std(titanic_df['age'])}")