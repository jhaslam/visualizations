"""
Visualizes a random walk using matplotlib
"""

import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk(50000)
rw.fill_walk()

# Set the size of the plotting window
plt.figure(dpi=128, figsize=(6, 6))

# Draw waypoints using a colour gradient from oldest to newest
point_indices = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_indices,
            cmap=plt.cm.Blues, edgecolor='none', s=1)

# Ephasize first and last points
plt.scatter(0, 0, c='green', edgecolor='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1],
            c='red', edgecolor='none', s=100)

plt.axis('off')

plt.show()
