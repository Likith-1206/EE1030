import matplotlib.pyplot as plt

# Coordinates of the points
points = {
    'A': (7, -2),
    'B': (1, -5),
    'P': (5, -3),
    'Q': (3, -4)
}

# Colors for each point
colors = {
    'A': 'red',
    'B': 'green',
    'P': 'blue',
    'Q': 'orange'
}

# Create a new figure
plt.figure()

# Plot each point with its corresponding color and label it
for label, (x, y) in points.items():
    plt.scatter(x, y, color=colors[label])
    plt.text(x + 0.1, y + 0.1, f'{label}({x}, {y})', fontsize=12)

# List of points in the order they should be connected
lines = ['A', 'P', 'Q', 'B', 'A']

# Draw lines connecting the points in the specified order
for i in range(len(lines) - 1):
    plt.plot(
        [points[lines[i]][0], points[lines[i+1]][0]], 
        [points[lines[i]][1], points[lines[i+1]][1]], 
        color='black', linestyle='-', linewidth=2
    )

# Set x and y limits
plt.xlim(0, 8)
plt.ylim(-6, 0)

# Add grid, labels, and title
plt.grid(True)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()
plt.savefig('Fig.png')


