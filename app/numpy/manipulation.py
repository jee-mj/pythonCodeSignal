import numpy as np

np_array = np.array([[1, 2, 3], [4, 5, 6]])
# Indexing: access the element at the first row, third column
print("Indexed Value: ", np_array[0, 2])  # Indexed Value: 3 # 0-based indexing

# Slicing: access the first row
print("Sliced Value: ", np_array[0, :])  # Sliced Value: [1 2 3]

# Reshape the array to 3 rows and 2 columns (only applicable if the reshaped total size equals the original size)
reshaped_array = np_array.reshape(3, 2)
print("Reshaped Array: ", reshaped_array)
# Reshaped Array:
# [[1 2]
#  [3 4]
#  [5 6]]
