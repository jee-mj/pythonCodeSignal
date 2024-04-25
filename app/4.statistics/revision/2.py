"""

This be the moment I realise that my strength is not in statistics.

I have been trying to get better at coding python for a job application that required taking an exam in 12 days, but the content has started becoming more difficult to process.

I should play to my strengths, and leave this alone for now. I'm a good artist after all.

Plus, python always has been and always will be... UGLY. if_i_get_a_job, itWillProbablyAllBeInSnakeCaseWithUglython. 🫣

#FamousLastWords

"""

import numpy as np
import pandas as pd
import seaborn as sns

# Load Titanic dataset
titanic_df = sns.load_dataset('titanic')

# Calculate the mean, median, and mode for the age and fare columns
mean_age_fare = titanic_df[['fare']].mean()
median_age_fare = titanic_df[['fare']].median()
mode_age_fare = titanic_df[['fare']].mode().iloc[0]

print(f"Mean of age and fare: \n{mean_age_fare}\n")
print(f"Median of age and fare: \n{median_age_fare}\n")
print(f"Mode of age and fare: \n{mode_age_fare}\n")

"""
Context:

What actually happened was that I thought accessing a dataset and loading it into a dataFrame was enough revision and neglected to actually transfer my OOP skills from C#/JS to Python before taking the exam.

I failed the exam as deserved.
"""