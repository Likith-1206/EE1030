import numpy as np

# Define the normal vector to the plane
normal_vector = np.array([6, -3, 2])

# Calculate the magnitude (norm) of the normal vector
magnitude = np.linalg.norm(normal_vector)

# Calculate the unit vector
unit_vector = normal_vector / magnitude

# Extract the direction cosines
l, m, n = unit_vector

# Display the results
print("Normal vector to the plane: ", normal_vector)
print("Magnitude of the normal vector: ", magnitude)
print("Unit vector perpendicular to the plane: ", unit_vector)
print("Direction cosines (l, m, n): ", (l, m, n))

