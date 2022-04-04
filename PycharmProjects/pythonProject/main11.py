import matplotlib.pyplot as plt
import numpy as np
import meta
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import LightSource
from numpy import cos, sin, pi, exp
coordsArr = []
def f(x):
    return x[0] ** 2 - 10 * np.around(np.cos(2 * np.pi * x[0])) + x[1]**2 - 10*\
np.around(np.cos(2 * np.pi * x[1])) + 20
def grad(x):
    return np.array([2*(x[0]+10*np.pi * np.around(np.sin(2 * np.pi * x[0]))),
2 * (x[1] + 10 * np.pi * np.around(np.sin(2 * np.pi * x[1])))])
x = np.array([1.2,1.2])
k=0
x_old = np.array([1.3,1.3])
epsilon = 0.001
while np.linalg.norm(x - x_old) > epsilon:
    if (all(grad(x) == 0)):
        break
    h = -grad(x)
    alpha = 0
    f_old = f(x)
    alpha = alpha + 0.01
    f_new = f(x + alpha * h)
    while f_old > f_new:
        alpha = alpha + 0.01
        f_old = f_new
        f_new = f(x + alpha * h)
    x_old = x
    x = x_old + alpha * h
    k=k+1
    coordsArr.append(x)

print(np.around(x))
print(f(x))
print(k)
print(coordsArr)

X, Y = np.meshgrid(meta.x, meta.y)
Z = meta.fn(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ls = LightSource(270, 45)
rgb = ls.shade(Z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, facecolors=rgb,
                alpha=0.15,
                linewidth=0, antialiased=False, shade=False)

for i in range(len(coordsArr) - 1):
    [x, y] = coordsArr[i]
    [xN, yN] = coordsArr[i + 1]
    ax.plot3D([x, xN], [y, yN], [meta.fn(x, y), meta.fn(xN, yN)], 'red')
plt.show()
print(coordsArr)