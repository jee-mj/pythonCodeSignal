import seaborn as sns

titanic_df = sns.load_dataset('titanic')

# Print the first five entries
print("\n        Print the first five entries:\n\n", titanic_df.head())

# Print the last five entries
print("\n        Print the last five entries:\n\n", titanic_df.tail())

# Print the shape of the DataFrame
print("\n        Print the shape of the DataFrame:\n\n",titanic_df.shape,"\n        Print a concise summary of the DataFrame:\n\n")
# Output: (891, 15)

# Print a concise summary of the DataFrame
titanic_df.info()
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 15 columns):
 #   Column       Non-Null Count  Dtype   
---  ------       --------------  -----   
 0   survived     891 non-null    int64   
 1   pclass       891 non-null    int64   
 2   sex          891 non-null    object  
 3   age          714 non-null    float64 
 4   sibsp        891 non-null    int64   
 5   parch        891 non-null    int64   
 6   fare         891 non-null    float64 
 7   embarked     889 non-null    object  
 8   class        891 non-null    category
 9   who          891 non-null    object  
 10  adult_male   891 non-null    bool    
 11  deck         203 non-null    category
 12  embark_town  889 non-null    object  
 13  alive        891 non-null    object  
 14  alone        891 non-null    bool    
dtypes: bool(2), category(2), float64(2), int64(4), object(5)
memory usage: 80.7+ KB
"""

# Print the descriptive statistics of the DataFrame
print("\n        Print the descriptive statistics of the DataFrame:\n\n", (titanic_df.describe()))
"""
         survived      pclass         age       sibsp       parch        fare
count  891.000000  891.000000  714.000000  891.000000  891.000000  891.000000
mean     0.383838    2.308642   29.699118    0.523008    0.381594   32.204208
std      0.486592    0.836071   14.526497    1.102743    0.806057   49.693429
min      0.000000    1.000000    0.420000    0.000000    0.000000    0.000000
25%      0.000000    2.000000   20.125000    0.000000    0.000000    7.910400
50%      0.000000    3.000000   28.000000    0.000000    0.000000   14.454200
75%      1.000000    3.000000   38.000000    1.000000    0.000000   31.000000
max      1.000000    3.000000   80.000000    8.000000    6.000000  512.329200
"""

print("\n        Count number of male and female passengers on the titanic:\n\n",titanic_df['sex'].value_counts())

# Print the count of unique entries in 'embarked' column
print("\nPrint the count of unique entries in 'embarked' column:\n\n", titanic_df['embarked'].nunique()) # Output: 3

# Print the unique entries in 'embarked' column
print("\nPrint unique entries from 'embarked' column:\n\n", titanic_df['embarked'].unique()) # Output: ['S' 'C' 'Q' nan]