import numpy as np
import matplotlib.pyplot as plt

# Define the range for x values
x = np.linspace(-10, 10, 400)

# Define the equations of the lines
y1 = (6 - x) / 2   # Line 1: x + 2y = 6
y2 = (2*x - 12) / 5  # Line 2: 2x - 5y = 12

# Plot the lines
plt.plot(x, y1, label='x + 2y = 6', color='blue')
plt.plot(x, y2, label='2x - 5y = 12', color='red')

# Plot the point of intersection C(6,0)
C = np.array([6, 0])
plt.scatter(*C, color='green')
plt.text(C[0] + 0.3, C[1] + 0.3, f"C{tuple(C)}", color='green')

# Set labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot of Lines x + 2y = 6 and 2x - 5y = 12 with Intersection Point C(6,0)')

# Add a grid and legend
plt.grid(True)
plt.legend()

# Set the aspect ratio to be equal
plt.gca().set_aspect('equal', adjustable='box')

# Show the plot
plt.show()

