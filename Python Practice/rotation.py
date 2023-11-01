import numpy as np

# Define the angle of rotation in radians (e.g., pi/4 for 45 degrees)
theta = np.pi / 4

# Create the rotation matrix for a counterclockwise rotation about the x-axis
Rx = np.array([[1, 0, 0],
               [0, np.cos(theta), -np.sin(theta)],
               [0, np.sin(theta), np.cos(theta)]])

# Display the rotation matrix
print("Rotation matrix Rx(θ) for counterclockwise rotation about the x-axis:")
print(Rx)
