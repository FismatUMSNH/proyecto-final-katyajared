from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def randrange(n, vmin, vmax):

    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = 100


for c, m, zlow, zhigh in [('y', 'o', -60, -50), ('b', '^', -30, -30)]:
    xs = randrange(n, 60, 3)
    ys = randrange(n, 60, 100)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=m)
plt.legend( ('Aceite', 'Agua'), loc = 'right')
ax.set_title('Muy frio')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
