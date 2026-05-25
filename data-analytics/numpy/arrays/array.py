# ================================
# NUMPY ARRAY PRACTICE
# ================================

import numpy as np

# --------------------------------
# 1. CREATE ARRAYS
# --------------------------------

arr1 = np.array([1, 2, 3, 4, 5])

print("1D Array:")
print(arr1)

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n2D Array:")
print(arr2)

# --------------------------------
# 2. ARRAY PROPERTIES
# --------------------------------

print("\nShape:", arr2.shape)
print("Dimensions:", arr2.ndim)
print("Size:", arr2.size)
print("Data Type:", arr2.dtype)

# --------------------------------
# 3. SPECIAL ARRAYS
# --------------------------------

zeros = np.zeros((2, 3))
print("\nZeros Array:")
print(zeros)

ones = np.ones((3, 3))
print("\nOnes Array:")
print(ones)

identity = np.eye(3)
print("\nIdentity Matrix:")
print(identity)

# --------------------------------
# 4. RANGE FUNCTIONS
# --------------------------------

arr_range = np.arange(1, 10, 2)

print("\nArange:")
print(arr_range)

linspace_arr = np.linspace(0, 1, 5)

print("\nLinspace:")
print(linspace_arr)

# --------------------------------
# 5. RESHAPING
# --------------------------------

arr = np.arange(1, 13)

reshaped = arr.reshape(3, 4)

print("\nReshaped Array:")
print(reshaped)

# --------------------------------
# 6. INDEXING
# --------------------------------

print("\nFirst Element:", arr1[0])
print("Last Element:", arr1[-1])

print("\n2D Indexing:")
print(arr2[1, 2])

# --------------------------------
# 7. SLICING
# --------------------------------

print("\nSlicing:")
print(arr1[1:4])

print("\n2D Slicing:")
print(arr2[:, 1:])

# --------------------------------
# 8. ARRAY OPERATIONS
# --------------------------------

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\nAddition:")
print(a + b)

print("\nSubtraction:")
print(a - b)

print("\nMultiplication:")
print(a * b)

print("\nDivision:")
print(a / b)

# --------------------------------
# 9. BROADCASTING
# --------------------------------

arr = np.array([1, 2, 3])

print("\nBroadcasting:")
print(arr + 10)

# --------------------------------
# 10. STATISTICS
# --------------------------------

data = np.array([10, 20, 30, 40, 50])

print("\nMean:", np.mean(data))
print("Median:", np.median(data))
print("Sum:", np.sum(data))
print("Min:", np.min(data))
print("Max:", np.max(data))
print("Standard Deviation:", np.std(data))

# --------------------------------
# 11. RANDOM NUMBERS
# --------------------------------

random_arr = np.random.rand(3, 3)

print("\nRandom Array:")
print(random_arr)

random_int = np.random.randint(1, 100, (2, 2))

print("\nRandom Integers:")
print(random_int)

# --------------------------------
# 12. FILTERING
# --------------------------------

arr = np.array([10, 15, 20, 25, 30])

filtered = arr[arr > 20]

print("\nFiltered Array:")
print(filtered)

# --------------------------------
# 13. SORTING
# --------------------------------

unsorted = np.array([5, 2, 9, 1, 7])

sorted_arr = np.sort(unsorted)

print("\nSorted Array:")
print(sorted_arr)

# --------------------------------
# 14. UNIQUE VALUES
# --------------------------------

arr = np.array([1, 2, 2, 3, 4, 4, 5])

unique_values = np.unique(arr)

print("\nUnique Values:")
print(unique_values)

# --------------------------------
# 15. MATRIX OPERATIONS
# --------------------------------

matrix1 = np.array([
    [1, 2],
    [3, 4]
])

matrix2 = np.array([
    [5, 6],
    [7, 8]
])

print("\nMatrix Addition:")
print(matrix1 + matrix2)

print("\nMatrix Multiplication:")
print(np.dot(matrix1, matrix2))

# --------------------------------
# 16. TRANSPOSE
# --------------------------------

print("\nTranspose:")
print(matrix1.T)

# --------------------------------
# 17. FLATTEN ARRAY
# --------------------------------

arr = np.array([
    [1, 2],
    [3, 4]
])

print("\nFlattened Array:")
print(arr.flatten())

# --------------------------------
# 18. CONDITIONAL OPERATIONS
# --------------------------------

arr = np.array([1, 2, 3, 4, 5])

result = np.where(arr % 2 == 0, "Even", "Odd")

print("\nConditional Operation:")
print(result)

# --------------------------------
# 19. CONCATENATION
# --------------------------------

a = np.array([1, 2])
b = np.array([3, 4])

combined = np.concatenate((a, b))

print("\nConcatenated Array:")
print(combined)

# --------------------------------
# 20. SAVE AND LOAD
# --------------------------------

np.save("sample.npy", arr1)

loaded = np.load("sample.npy")

print("\nLoaded Array:")
print(loaded)

# ================================
# END OF NUMPY PRACTICE
# ================================