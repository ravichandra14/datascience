# ================================
# NUMPY BROADCASTING PRACTICE
# ================================

import numpy as np

# --------------------------------
# 1. BASIC BROADCASTING
# --------------------------------

arr = np.array([1, 2, 3])

print("Original Array:")
print(arr)

print("\nAdd Scalar:")
print(arr + 10)

print("\nMultiply Scalar:")
print(arr * 5)

# --------------------------------
# 2. 1D + 1D BROADCASTING
# --------------------------------

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\nAddition:")
print(a + b)

# --------------------------------
# 3. 2D + SCALAR
# --------------------------------

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n2D Matrix:")
print(matrix)

print("\nMatrix + 100:")
print(matrix + 100)

# --------------------------------
# 4. 2D + 1D BROADCASTING
# --------------------------------

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

vector = np.array([10, 20, 30])

print("\n2D + 1D Broadcasting:")
print(matrix + vector)

# --------------------------------
# 5. COLUMN BROADCASTING
# --------------------------------

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

column = np.array([
    [10],
    [20]
])

print("\nColumn Broadcasting:")
print(matrix + column)

# --------------------------------
# 6. ROW WISE MULTIPLICATION
# --------------------------------

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

row = np.array([2, 2, 2])

print("\nRow Wise Multiplication:")
print(matrix * row)

# --------------------------------
# 7. NORMALIZATION EXAMPLE
# --------------------------------

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

mean = np.mean(data, axis=0)

print("\nColumn Mean:")
print(mean)

normalized = data - mean

print("\nNormalized Data:")
print(normalized)

# --------------------------------
# 8. IMAGE PROCESSING STYLE
# --------------------------------

image = np.array([
    [100, 120, 140],
    [150, 170, 190]
])

brightness = 30

bright_image = image + brightness

print("\nBrightness Increased:")
print(bright_image)

# --------------------------------
# 9. RANDOM MATRIX BROADCASTING
# --------------------------------

matrix = np.random.randint(1, 10, (3, 3))

print("\nRandom Matrix:")
print(matrix)

print("\nAdd Vector:")
print(matrix + np.array([1, 2, 3]))

# --------------------------------
# 10. BROADCASTING RULE CHECK
# --------------------------------

a = np.array([
    [1],
    [2],
    [3]
])

b = np.array([10, 20, 30])

print("\nBroadcasting Shapes:")
print("Shape of a:", a.shape)
print("Shape of b:", b.shape)

print("\nResult:")
print(a + b)

# ================================
# BROADCASTING RULES
# ================================

"""
Broadcasting works when:

1. Dimensions are equal
OR
2. One of them is 1

Examples:

(3, 1) + (3,) -> Works
(2, 3) + (3,) -> Works
(2, 3) + (2, 1) -> Works
(2, 3) + (4,) -> Error
"""

# ================================
# END
# ================================