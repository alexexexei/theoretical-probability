import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([0, 1, 2, 3])
X, Y = np.meshgrid(x, y)
Z = np.array([
    [0, 0, 0, 0],
    [0, 0, 0, 0.1],
    [0, 0, 0.4, 0.7],
    [0, 0.1, 0.7, 1]
])

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

surface = ax.plot_surface(X, Y, Z, cmap='viridis')

fig.colorbar(surface)

ax.set_title('Distribution function')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('F(x, y)')
ax.set_zlim(0, 1)

plt.show()
