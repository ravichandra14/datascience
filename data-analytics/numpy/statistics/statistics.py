# ==========================================
# NUMPY STATISTICS PRACTICE
# ==========================================

import numpy as np

# ------------------------------------------
# 1. CREATE ARRAY
# ------------------------------------------

arr = np.array([10, 20, 30, 40, 50])

print("Array:")
print(arr)

# ------------------------------------------
# 2. MEAN (AVERAGE)
# ------------------------------------------

mean_value = np.mean(arr)

print("\nMean:")
print(mean_value)

# ------------------------------------------
# 3. MEDIAN
# ------------------------------------------

median_value = np.median(arr)

print("\nMedian:")
print(median_value)

# ------------------------------------------
# 4. MODE
# ------------------------------------------
# NumPy does not directly provide mode
# We use bincount for integer arrays

arr_mode = np.array([1, 2, 2, 3, 4, 4, 4, 5])

mode_value = np.bincount(arr_mode).argmax()

print("\nMode:")
print(mode_value)

# ------------------------------------------
# 5. SUM
# ------------------------------------------

total = np.sum(arr)

print("\nSum:")
print(total)

# ------------------------------------------
# 6. MINIMUM & MAXIMUM
# ------------------------------------------

print("\nMinimum:")
print(np.min(arr))

print("\nMaximum:")
print(np.max(arr))

# ------------------------------------------
# 7. RANGE
# ------------------------------------------

range_value = np.max(arr) - np.min(arr)

print("\nRange:")
print(range_value)

# ------------------------------------------
# 8. STANDARD DEVIATION
# ------------------------------------------

std_value = np.std(arr)

print("\nStandard Deviation:")
print(std_value)

# ------------------------------------------
# 9. VARIANCE
# ------------------------------------------

variance_value = np.var(arr)

print("\nVariance:")
print(variance_value)

# ------------------------------------------
# 10. PERCENTILE
# ------------------------------------------

p25 = np.percentile(arr, 25)
p50 = np.percentile(arr, 50)
p75 = np.percentile(arr, 75)

print("\n25th Percentile:", p25)
print("50th Percentile:", p50)
print("75th Percentile:", p75)

# ------------------------------------------
# 11. QUARTILES
# ------------------------------------------

quartiles = np.percentile(arr, [25, 50, 75])

print("\nQuartiles:")
print(quartiles)

# ------------------------------------------
# 12. CUMULATIVE SUM
# ------------------------------------------

cumsum = np.cumsum(arr)

print("\nCumulative Sum:")
print(cumsum)

# ------------------------------------------
# 13. CUMULATIVE PRODUCT
# ------------------------------------------

cumprod = np.cumprod(arr)

print("\nCumulative Product:")
print(cumprod)

# ------------------------------------------
# 14. DIFFERENCE BETWEEN ELEMENTS
# ------------------------------------------

diff = np.diff(arr)

print("\nDifference Between Consecutive Elements:")
print(diff)

# ------------------------------------------
# 15. SORTING
# ------------------------------------------

unsorted = np.array([40, 10, 30, 20, 50])

sorted_arr = np.sort(unsorted)

print("\nSorted Array:")
print(sorted_arr)

# ------------------------------------------
# 16. UNIQUE VALUES
# ------------------------------------------

arr_unique = np.array([1, 2, 2, 3, 4, 4, 5])

unique_values = np.unique(arr_unique)

print("\nUnique Values:")
print(unique_values)

# ------------------------------------------
# 17. ARGMAX & ARGMIN
# ------------------------------------------

print("\nIndex of Maximum Value:")
print(np.argmax(arr))

print("\nIndex of Minimum Value:")
print(np.argmin(arr))

# ------------------------------------------
# 18. CORRELATION
# ------------------------------------------

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

correlation = np.corrcoef(x, y)

print("\nCorrelation Matrix:")
print(correlation)

# ------------------------------------------
# 19. 2D ARRAY STATISTICS
# ------------------------------------------

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\n2D Matrix:")
print(matrix)

# Row-wise sum
print("\nRow-wise Sum:")
print(np.sum(matrix, axis=1))

# Column-wise sum
print("\nColumn-wise Sum:")
print(np.sum(matrix, axis=0))

# Row-wise mean
print("\nRow-wise Mean:")
print(np.mean(matrix, axis=1))

# Column-wise mean
print("\nColumn-wise Mean:")
print(np.mean(matrix, axis=0))

# ------------------------------------------
# 20. RANDOM DATA STATISTICS
# ------------------------------------------

random_data = np.random.randint(1, 100, 20)

print("\nRandom Data:")
print(random_data)

print("\nMean:", np.mean(random_data))
print("Median:", np.median(random_data))
print("Standard Deviation:", np.std(random_data))

# ==========================================
# IMPORTANT FORMULAS
# ==========================================

"""
Mean:
sum(values) / n

Variance:
sum((x - mean)^2) / n

Standard Deviation:
sqrt(variance)

Range:
max - min
"""

# ==========================================
# END
# ==========================================