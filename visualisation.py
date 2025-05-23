
"""
Triangulation - Visualisation
"""

# plot the x, y, z coordinates of joint 0

import matplotlib.pyplot as plt
% matplotlib notebook

plt.figure(figsize=(9.4, 6))
plt.plot(p3ds[:, 0, 0])
plt.plot(p3ds[:, 0, 1])
plt.plot(p3ds[:, 0, 2])
plt.xlabel("Time (frames)")
plt.ylabel("Coordinate (mm)")
plt.title("x, y, z coordinates of {}".format(bodyparts[0]))