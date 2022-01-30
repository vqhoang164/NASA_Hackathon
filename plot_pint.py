import numpy as np
import matplotlib.pyplot as plt

x = [0, 1, 2, 3]
y = [0, 0, 0, 0]
z = [0, 2, 3, 3]

print(z)

fig = plt.figure()
plt.figure(figsize=(10, 10))
ax = plt.axes(projection='3d')
ax.plot3D(x, y, z, 'green', marker='o')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()


ax.plot3D(xline, yline, zline, 'gray')

