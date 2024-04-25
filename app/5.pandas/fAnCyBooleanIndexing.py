import seaborn as sns
import pandas as pd

# Load dataset
titanic_df = sns.load_dataset('titanic')

# Filter passengers who survived
survivors = titanic_df[titanic_df['survived'] == 1]
print("\nFilter passengers who survived:\n\n", survivors.head())

"""
   survived  pclass     sex   age  ...  deck  embark_town  alive  alone
1         1       1  female  38.0  ...     C    Cherbourg    yes  False
2         1       3  female  26.0  ...   NaN  Southampton    yes   True
3         1       1  female  35.0  ...     C  Southampton    yes  False
8         1       3  female  27.0  ...   NaN  Southampton    yes  False
9         1       2  female  14.0  ...   NaN    Cherbourg    yes  False

[5 rows x 15 columns]
"""

# Sort survivors by age
sorted_df = survivors.sort_values('age')
print("\nSort survivors by age:\n\n",sorted_df.head())

"""
     survived  pclass     sex   age  ...  deck  embark_town  alive  alone
803         1       3    male  0.42  ...   NaN    Cherbourg    yes  False
755         1       2    male  0.67  ...   NaN  Southampton    yes  False
644         1       3  female  0.75  ...   NaN    Cherbourg    yes  False
469         1       3  female  0.75  ...   NaN    Cherbourg    yes  False
831         1       2    male  0.83  ...   NaN  Southampton    yes  False

[5 rows x 15 columns]
"""

# Sort survivors by class and age
sorted_df = survivors.sort_values(['pclass', 'age'], ascending=[False, True])
print("\nSort survivors by class and age:\n\n",sorted_df.head())

# Filter female passengers who survived

female_survivors = titanic_df[
   (titanic_df['survived'] == 1) & (titanic_df['sex'] == 'female')
]

# wHiLe I aM BeInG sIlLy, So Is CoDeSiGnAl! aPpArEnTlY wE CaN oNlY lEaRn At A SnAiL's PaCe! 🐌