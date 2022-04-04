import meta
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import LightSource
def fn(x, y):
    return x**2 + y**2 - np.cos(18*x) - np.cos(18*y)
def dfn(x, y):
    return [x*2 + 18*np.sin(18*x), y*2 + 18*np.sin(18*y)]

x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
radius = 1
start = [0.5, 0.5]

max_steps = 400
step = 1
step_divider = 0.5
quality = 0.00001
quality1 = 0.00001
quality2 = 0.00001


def absV(x):
    return np.sqrt(x[0] ** 2 + x[1] ** 2)


def gradientDescent(coords, step, max):
    coordsArr = []
    k = 0
    while (True):
        grad = dfn(coords[0], coords[1])
        if abs(grad[0]) < quality1 and abs(grad[1]) < quality1:
            return coordsArr
        if k >= max:
            return coordsArr
        delta = 0
        while (True):
            newCoords = [coords[0] - step * grad[0] / absV(grad), coords[1] - step * grad[1] / absV(grad)]
            delta = meta.fn(newCoords[0], newCoords[1]) - meta.fn(coords[0], coords[1])
            k += 1
            if delta < 0 or delta < quality * absV(grad) ** 2:
                break
            else:
                step = step * step_divider
        first = absV([newCoords[0] - coords[0], newCoords[1] - coords[1]])
        second = abs(delta)
        if first < quality2 and second < quality2:
            return coordsArr
        else:
            coords = newCoords
            k += 1
        coordsArr.append(coords)


coordsArr = gradientDescent(start, step, max_steps)
# x and y axis


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



