import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a line plot
plt.figure(figsize=(8, 6))  # Set figure size
plt.plot(x, y, marker='o', color='blue', linestyle='-')  # Line plot with markers
plt.title('Simple Line Plot')  # Add title
plt.xlabel('X-axis')  # Add label for X-axis
plt.ylabel('Y-axis')  # Add label for Y-axis
plt.grid(True)  # Add grid
plt.show()  # Display the plot

