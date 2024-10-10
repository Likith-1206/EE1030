import numpy as np
import matplotlib.pyplot as plt

# Function to read points from the asgn3.txt file
def read_parabola_points(filename):
    intersection_points = []
    
    parabola_points = []
    
    with open(filename, 'r') as file:
        for line in file:
            if 'Parabola point for x' in line:
                # Extract the x, y values for the parabola points
                parts = line.split(':')
                x = float(parts[0].split('=')[1].strip())
                y_vals = parts[1].strip().strip('()').split(',')
                y = float(y_vals[1])
                parabola_points.append((x, y))
                    
            elif 'For x =' in line:
                # Extract the x, y values for the intersection points
                parts = line.split(':')
                x = float(parts[0].split('=')[1].strip())
                y_vals = parts[1].split('and')
                y1 = float(y_vals[0].strip().strip('()').split(',')[1])
                y2 = float(y_vals[1].strip().strip('()').split(',')[1])
                intersection_points.append((x, y1))
                intersection_points.append((x, y2))
    
    return np.array(parabola_points), np.array(intersection_points)

# Read points from the text file
parabola_points, intersection_points = read_parabola_points('asgn3.txt')

# Extract x and y values of the parabola points
x_vals_parabola = parabola_points[:, 0]
y_vals_parabola = parabola_points[:, 1]

# Generate a smoother x range (finer resolution) for interpolation
x_smooth = np.linspace(min(x_vals_parabola), max(x_vals_parabola), 500)

# Interpolating both positive and negative y-values using the equation y = ±√x
y_smooth_pos = np.sqrt(x_smooth)
y_smooth_neg = -np.sqrt(x_smooth)

# Plot the smooth parabola points (positive and negative branches)
plt.plot(x_smooth, y_smooth_pos, color="blue", linewidth=2, label="Parabola: $y^2 = x$")
plt.plot(x_smooth, y_smooth_neg, color="blue", linewidth=2)

# Shading between the parabola and the x-axis, only between x = 0.25 and x = 1
x_shade_range = np.linspace(0.25, 1, 500)  # Only between x = 0.25 and x = 1
y_shade_pos = np.sqrt(x_shade_range)      # Positive branch for shading

plt.fill_between(x_shade_range, y_shade_pos, 0, color="blue", alpha=0.1)

# Plotting the points of intersection
for i, (x, y) in enumerate(intersection_points):
    if i == 0:
        plt.scatter(x, y, color='red', marker='o', zorder=5)
        plt.annotate(r'$a_0$' + f' ({x:.2f}, {y:.2f})', (x, y), textcoords="offset points", xytext=(0,10), ha='center', color='red')
    elif i == 1:
        plt.scatter(x, y, color='red', marker='o', zorder=5)
        plt.annotate(r'$a_1$' + f' ({x:.2f}, {y:.2f})', (x, y), textcoords="offset points", xytext=(0,10), ha='center', color='red')
    elif i == 2:
        plt.scatter(x, y, color='green', marker='o', zorder=5)
        plt.annotate(r'$a_2$' + f' ({x:.2f}, {y:.2f})', (x, y), textcoords="offset points", xytext=(0,10), ha='center', color='green')
    elif i == 3:
        plt.scatter(x, y, color='green', marker='o', zorder=5)
        plt.annotate(r'$a_3$' + f' ({x:.2f}, {y:.2f})', (x, y), textcoords="offset points", xytext=(0,10), ha='center', color='green')

# Plot the vertical lines for x = 0.25 and x = 1
x_vert_025 = 0.25
x_vert_1 = 1.0

plt.axvline(x=x_vert_025, color='green', linestyle='--', label="x = 0.25")
plt.axvline(x=x_vert_1, color='red', linestyle='--', label="x = 1")

# Customize the plot
plt.xlabel("x-axis")
plt.ylabel("y-axis")

# Add the legend box in a corner (top-left) of the plot
plt.legend(loc='upper left', frameon=True)

plt.grid(True)


plt.show()

