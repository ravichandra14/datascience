# ================================
# NUMPY INDEXING PRACTICE
# ================================

import numpy as np

# --------------------------------
# 1. CREATE ARRAYS
# --------------------------------

arr1 = np.array([10, 20, 30, 40, 50])

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("1D Array:")
print(arr1)

print("\n2D Array:")
print(arr2)

# --------------------------------
# 2. 1D INDEXING
# --------------------------------

print("\nFirst Element:")
print(arr1[0])

print("\nThird Element:")
print(arr1[2])

print("\nLast Element:")
print(arr1[-1])

# --------------------------------
# 3. 2D INDEXING
# --------------------------------

print("\nElement at Row 0, Column 1:")
print(arr2[0, 1])

print("\nElement at Row 2, Column 2:")
print(arr2[2, 2])

print("\nLast Element:")
print(arr2[-1, -1])

# --------------------------------
# 4. SLICING IN 1D
# --------------------------------

print("\nElements from Index 1 to 3:")
print(arr1[1:4])

print("\nFirst 3 Elements:")
print(arr1[:3])

print("\nLast 2 Elements:")
print(arr1[-2:])

# --------------------------------
# 5. SLICING IN 2D
# --------------------------------

print("\nFirst Row:")
print(arr2[0])

print("\nSecond Column:")
print(arr2[:, 1])

print("\nFirst Two Rows:")
print(arr2[:2])

print("\nSubmatrix:")
print(arr2[0:2, 1:3])

# --------------------------------
# 6. STEP SLICING
# --------------------------------

print("\nEvery 2nd Element:")
print(arr1[::2])

print("\nReverse Array:")
print(arr1[::-1])

# --------------------------------
# 7. BOOLEAN INDEXING
# --------------------------------

arr = np.array([5, 10, 15, 20, 25])

print("\nElements Greater Than 15:")
print(arr[arr > 15])

print("\nEven Numbers:")
print(arr[arr % 2 == 0])

# --------------------------------
# 8. CONDITIONAL INDEXING
# --------------------------------

data = np.array([1, 2, 3, 4, 5])

result = np.where(data > 3)

print("\nIndexes Where Value > 3:")
print(result)

# --------------------------------
# 9. FANCY INDEXING
# --------------------------------

arr = np.array([10, 20, 30, 40, 50])

indexes = [0, 2, 4]

print("\nFancy Indexing:")
print(arr[indexes])

# --------------------------------
# 10. 2D FANCY INDEXING
# --------------------------------

matrix = np.array([
    [11, 12, 13],
    [21, 22, 23],
    [31, 32, 33]
])

rows = [0, 1, 2]
cols = [2, 1, 0]

print("\n2D Fancy Indexing:")
print(matrix[rows, cols])

# --------------------------------
# 11. MODIFY VALUES USING INDEXING
# --------------------------------

arr = np.array([1, 2, 3, 4, 5])

arr[0] = 100

print("\nModified Array:")
print(arr)

# --------------------------------
# 12. MODIFY MULTIPLE VALUES
# --------------------------------

arr[1:4] = 50

print("\nModified Slice:")
print(arr)

# --------------------------------
# 13. BOOLEAN MODIFYING
# --------------------------------

arr = np.array([10, 20, 30, 40])

arr[arr > 20] = 999

print("\nBoolean Modified Array:")
print(arr)

# --------------------------------
# 14. MULTI-DIMENSIONAL INDEXING
# --------------------------------

cube = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print("\n3D Array:")
print(cube)

print("\nElement from 3D Array:")
print(cube[1, 0, 1])

# --------------------------------
# 15. ITERATING USING INDEX
# --------------------------------

arr = np.array([100, 200, 300])

print("\nIterating with Index:")

for i in range(len(arr)):
    print(f"Index {i} -> {arr[i]}")

# --------------------------------
# 16. np.ndenumerate()
# --------------------------------

matrix = np.array([
    [1, 2],
    [3, 4]
])

print("\nUsing ndenumerate:")

for index, value in np.ndenumerate(matrix):
    print(index, value)

# ================================
# IMPORTANT NOTES
# ================================

"""
1D:
arr[index]

2D:
arr[row, column]

3D:
arr[depth, row, column]

Slicing:
arr[start:end:step]

Boolean Indexing:
arr[arr > value]

Fancy Indexing:
arr[[1, 3, 5]]
"""

# ================================
# END
# ================================