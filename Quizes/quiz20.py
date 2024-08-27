import numpy as np

# Define the direction vectors
d1 = np.array([3, 5, 4])
d2 = np.array([1, 1, 1])

# Calculate the dot product of the direction vectors
dot_product = np.dot(d1, d2)

# Calculate the magnitudes of the direction vectors
magnitude_d1 = np.linalg.norm(d1)
magnitude_d2 = np.linalg.norm(d2)

# Calculate the cosine of the angle between the lines
cos_theta = dot_product / (magnitude_d1 * magnitude_d2)

# Calculate the angle in radians and then convert to degrees
theta_radians = np.arccos(cos_theta)
theta_degrees = np.degrees(theta_radians)

# Display the result
print(f"The angle between the two lines is {theta_degrees:.2f} degrees.")

