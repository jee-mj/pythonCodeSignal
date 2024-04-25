# I'm the captain of THIS ship. 🚢
# ... and I ship the code and the comments, not you (hater)! 🚢

import seaborn as sns
import numpy as np

# TODO: Load the Titanic DataSet
dataFrame = sns.load_dataset('titanic')

dataFrame_statistics = {
# TODO: Calculate mean, median, and mode for 'age', print them
    'mean': dataFrame['age'].mean(),
    'median': dataFrame['age'].median(),
    'mode': dataFrame['age'].mode().iloc[0],
# TODO: Calculate the standard deviation for 'age', print it
    'standardDeviation': nd.std(dataFrame['age']),
# TODO: Calculate Quartiles for 'age', print them
    'quartile_1': dataFrame['age'].quantile(0.25),
    'quartile_3': dataFrame['age'].quantile(0.75)
}

for key, value in dataFrame_statistics.items():
    print(f"{key}: {value}")