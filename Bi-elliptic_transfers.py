import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 600)

# Orbit radii
r1 = 1.0   # Initial orbit
r3 = 3.0   # Final orbit
rb = 4.0   # Intermediate apoapsis

# First elliptical transfer (r1 -> rb)
a1 = (r1 + rb)/2
b1 = np.sqrt(r1 * rb)
theta1 = np.linspace(0, np.pi, 300)  # half ellipse
x1 = a1 * np.cos(theta1)
y1 = b1 * np.sin(theta1)

# Second elliptical transfer (rb -> r3)
a2 = (rb + r3)/2
b2 = np.sqrt(rb * r3)
theta2 = np.linspace(np.pi, 2*np.pi, 300)  # second half ellipse
x2 = a2 * np.cos(theta2)
y2 = b2 * np.sin(theta2)

# Circular orbits
x_r1 = r1 * np.cos(theta)
y_r1 = r1 * np.sin(theta)
x_r3 = r3 * np.cos(theta)
y_r3 = r3 * np.sin(theta)

# Plot
plt.figure(figsize=(8,8))
plt.plot(x_r1, y_r1, label='Initial Orbit r1', color='blue')
plt.plot(x_r3, y_r3, label='Final Orbit r3', color='red')
plt.plot(x1, y1, label='First Transfer Ellipse', color='orange')
plt.plot(x2, y2, label='Second Transfer Ellipse', color='green')
plt.scatter([0], [0], color='yellow', s=100, label='Central Body')
plt.title("Bi-Elliptic Transfer Orbit")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.show()