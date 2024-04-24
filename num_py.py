import numpy as np

# Create a 2D array (matrix)
data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Original Matrix:")
print(data)

# Accessing elements
print("\nElement at row 1, column 2:", data[0, 1])

# Slicing rows and columns
print("\nFirst row:", data[0, :])
print("First column:", data[:, 0])

# Performing operations
print("\nSum of all elements:", np.sum(data))
print("Mean of all elements:", np.mean(data))
print("Transpose of the matrix:")
print(np.transpose(data))
