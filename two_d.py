def create_2d_array(rows, cols):
    """Create a 2D array with the specified number of rows and columns."""
    return [[0 for _ in range(cols)] for _ in range(rows)]

def set_value_2d(array, row, col, value):
    """Set the value at the specified row and column in the 2D array."""
    if row < len(array) and col < len(array[0]):
        array[row][col] = value
    else:
        print("Invalid index")

def get_value_2d(array, row, col):
    """Get the value at the specified row and column from the 2D array."""
    if row < len(array) and col < len(array[0]):
        return array[row][col]
    else:
        print("Invalid index")
        return None

def display_2d_array(array):
    """Display the 2D array."""
    for row in array:
        print(row)

# Create a 3x3 2D array
rows = 3
cols = 3
array_2d = create_2d_array(rows, cols)

# Set values in the 2D array
set_value_2d(array_2d, 0, 0, 1)
set_value_2d(array_2d, 0, 1, 2)
set_value_2d(array_2d, 0, 2, 3)
set_value_2d(array_2d, 1, 0, 4)
set_value_2d(array_2d, 1, 1, 5)
set_value_2d(array_2d, 1, 2, 6)
set_value_2d(array_2d, 2, 0, 7)
set_value_2d(array_2d, 2, 1, 8)
set_value_2d(array_2d, 2, 2, 9)

# Display the 2D array
print("2D Array:")
display_2d_array(array_2d)

# Get value from the 2D array
print("\nValue at (1, 1):", get_value_2d(array_2d, 1, 1))
