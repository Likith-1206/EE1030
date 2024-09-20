import ctypes
import matplotlib.pyplot as plt
import numpy as np

# Load the shared library
lib = ctypes.CDLL('./asgn2.so')

# Define the Point struct in Python
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double)]

# Define the C function signature
lib.calculateTrisectionPoints.argtypes = [Point, Point, ctypes.POINTER(Point), ctypes.POINTER(Point)]

# Initialize points A and B
A = Point(7, -2)
B = Point(1, -5)

# Initialize points P and Q to store the results
P = Point()
Q = Point()

# Call the C function to calculate points P and Q
lib.calculateTrisectionPoints(A, B, ctypes.byref(P), ctypes.byref(Q))

# Extract the coordinates of P and Q
P_x, P_y = P.x, P.y
Q_x, Q_y = Q.x, Q.y

# Plotting the points A, B, P, and Q
x_values = [A.x, P_x, Q_x, B.x]
y_values = [A.y, P_y, Q_y, B.y]

plt.plot(x_values, y_values, 'bo-')  # Plot the line
plt.scatter(x_values, y_values, color='red')  # Scatter points

# Label the points with their coordinates
plt.text(A.x, A.y, f'A({A.x}, {A.y})', fontsize=12, ha='right')
plt.text(B.x, B.y, f'B({B.x}, {B.y})', fontsize=12, ha='right')
plt.text(P_x, P_y, f'P({P_x}, {P_y})', fontsize=12, ha='right')
plt.text(Q_x, Q_y, f'Q({Q_x}, {Q_y})', fontsize=12, ha='right')

# Configure the plot
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Trisection of Line Segment AB with Labeled Points')
plt.grid(True)
plt.show()

