import numpy as np
import matplotlib.pyplot as plt

# Define the points as numpy arrays (matrices)
A = np.array([7, -1])
B = np.array([-3, -4])
C = np.array([3, -11.5])

# Combine the points into a matrix
points_matrix = np.array([A, B, C])

# Extract x and y coordinates
x_coords = points_matrix[:, 0]
y_coords = points_matrix[:, 1]

# Plot the points
plt.scatter(x_coords, y_coords, color='blue')

# Annotate the points with their coordinates
for i, point in enumerate(points_matrix):
    plt.text(point[0] + 0.5, point[1] + 0.5, f"({point[0]}, {point[1]})")

# Join the points with lines
plt.plot(x_coords, y_coords, color='green', linestyle='-', linewidth=2)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot of Points A, B, and C with Coordinates')

# Set the aspect ratio to be equal to ensure accurate representation
plt.gca().set_aspect('equal', adjustable='box')

# Show the grid
plt.grid(True)

# Show the plot
plt.show()

