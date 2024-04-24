import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])

print("Dimensions: ", array.ndim)  # 2 # Number of dimensions
print("Shape: ", array.shape)  # (2, 3) # Size of each dimension (russian doll)
print("Size: ", array.size)  # 6 # Total number of elements
print("Data Type: ", array.dtype)  # int64 # Data type of elements
print("\n\nMore attributes... \n\n")
print("Bytes: ", array.nbytes)  # 48 # Total bytes consumed by the elements of the array
print("Item Size: ", array.itemsize)  # 8 # Size of each element in bytes
print("Strides: ", array.strides)  # (24, 8) # Bytes to step in each dimension
print("Flags: ", array.flags)
# Output:
# Flags:    C_CONTIGUOUS : True
#   F_CONTIGUOUS : False
#   OWNDATA : True
#   WRITEABLE : True
#   ALIGNED : True
#   WRITEBACKIFCOPY : False
print("Real: ", array.real)  # [[1 2 3] [4 5 6]]
print("Imaginary: ", array.imag)  # [[0 0 0] [0 0 0]]
print("Flat: ", array.flat)  # <numpy.flatiter object at 0x7f8e3e2b6e00>
print("T: ", array.T)  # [[1 4] [2 5] [3 6]]
print("Data: ", array.data)  # <memory at 0x7f8e3e2a4f40>
print("Base: ", array.base)  # None
