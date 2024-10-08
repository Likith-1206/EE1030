import numpy as np
import matplotlib.pyplot as plt

# Load the points from the text file
points = []
with open("asgn2.txt", 'r') as file:
    for line in file:
        # Check if the line contains coordinates
        if '(' in line and ')' in line:
            # Isolate the part with the coordinates
            coords_part = line.split('(')[-1].split(')')[0].strip()  # Get part between '(' and ')'
            try:
                # Split the coordinates and convert them to floats
                x, y = map(float, coords_part.split(','))
                points.append((x, y))  # Append as a tuple
            except ValueError as e:
                print(f"Error converting coordinates in line: '{line.strip()}': {e}")

# Convert to numpy array for easier manipulation
points = np.array(points)

# Check if points were loaded correctly
if points.shape[0] < 4:
    raise ValueError("Data must contain at least four coordinates.")

# Extract the coordinates of points P, Q, B, and A
A = points[0]  # Trisection point Q
B = points[1]  # Trisection point P
P = points[2]  # Point B
Q = points[3]  # Point A


# Plot the points
plt.figure()

# Plot thick lines between points A and B, and P and Q
plt.plot([A[0], B[0]], [A[1], B[1]], color='gray', linewidth=2, label='Line AB')
plt.plot([P[0], Q[0]], [P[1], Q[1]], color='gray', linewidth=2, label='Line PQ')

# Plot the points A, B, P, and Q
plt.scatter(A[0], A[1], color='red', marker='o')  # Point A
plt.scatter(B[0], B[1], color='green', marker='o')  # Point B
plt.scatter(P[0], P[1], color='blue', marker='o')   # Point P
plt.scatter(Q[0], Q[1], color='purple', marker='o')  # Point Q

# Label the points with coordinates
plt.text(A[0], A[1], f"A ({A[0]:.6f}, {A[1]:.6f})", fontsize=9, verticalalignment='bottom', horizontalalignment='right')
plt.text(B[0], B[1], f"B ({B[0]:.6f}, {B[1]:.6f})", fontsize=9, verticalalignment='bottom', horizontalalignment='right')
plt.text(P[0], P[1], f"P ({P[0]:.6f}, {P[1]:.6f})", fontsize=9, verticalalignment='bottom', horizontalalignment='right')
plt.text(Q[0], Q[1], f"Q ({Q[0]:.6f}, {Q[1]:.6f})", fontsize=9, verticalalignment='bottom', horizontalalignment='right')

# Label the axes and add a title
plt.xlabel("x")
plt.ylabel("y")
plt.title("Trisection Points P and Q with Points A and B")
plt.grid(True)

# Save the resulting figure

plt.show()

