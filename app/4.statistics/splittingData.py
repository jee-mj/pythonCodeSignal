import numpy as np
import pandas as pd
import seaborn as sns

# Load Titanic dataset
titanic_df = sns.load_dataset('titanic')

# Quartiles and percentiles
# Using Numpy

Q1_age_np = np.percentile(titanic_df['age'].dropna(), 25)
Q3_age_np = np.percentile(titanic_df['age'].dropna(), 75)

print("\nFirst Quartile of age (Numpy): ", Q1_age_np) # First Quartile of age (Numpy): 20.125
print("\nThird quartile of age (Numpy): ", Q3_age_np)

# Output:
# First Quartile of age (Numpy):  20.125
# Third quartile of age (Numpy):  38.0

# Using Pandas

Q1_age_pd = titanic_df['age'].quantile(0.25)
Q3_age_pd = titanic_df['age'].quantile(0.75)

print("\nFirst quartile of age (Pandas): ", Q1_age_pd)
print("\nThird quartile of age (Pandas): ", Q3_age_pd)

# Output:
# First quartile of age (Pandas): 20.125
# Third quartile of age (Pandas): 38.0