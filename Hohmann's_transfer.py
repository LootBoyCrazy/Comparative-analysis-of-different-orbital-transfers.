import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 600)
r_start = 1.0  # Radius of the initial circular orbit
r_end = 2.0    # Radius of the final circular orbit
r_transfer_a = (r_start + r_end) / 2  # Semi-major axis of the transfer ellipse
r_transfer_b = np.sqrt(r_start * r_end)  # Semi-minor axis of the transfer ellipse
# Parametric equations for the orbits
x_start = r_start * np.cos(theta)
y_start = r_start * np.sin(theta)
x_end = r_end * np.cos(theta)
y_end = r_end * np.sin(theta)
# Parametric equations for the transfer ellipse
theta_transfer = np.linspace(0, np.pi, 300)
x_transfer = r_transfer_a * np.cos(theta_transfer)
y_transfer = r_transfer_b * np.sin(theta_transfer)
# Plotting the orbits and transfer ellipse
plt.figure(figsize=(8, 8))
plt.plot(x_start, y_start, label='Initial Orbit (r=1)', color='blue')
plt.plot(x_end, y_end, label='Final Orbit (r=2)', color='red')
plt.plot(x_transfer, y_transfer, label='Hohmann Transfer Ellipse', color='orange')=='orange'
plt.scatter([0], [0], color='yellow', s=100, label='Central Body')
plt.title("Hohmann's Transfer Orbit")
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()
plt.plot(x_transfer, y_transfer, label='Hohmann Transfer Ellipse', color='orange')