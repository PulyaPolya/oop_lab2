import numpy as np
import decimal
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt




def f(x, y):
    #return 5*np.sin(np.sqrt(x ** 2 + y ** 2))
    return (x**4 + y**4 +  2*x + 3*y) / 2000

def d_f_x(x, y):
    return (4*(x**3) +2)/2000
    #return np.cos(np.sqrt(x ** 2 + y ** 2)) * (1 / (np.sqrt(x ** 2 + y ** 2))) * x

def d_f_y(x, y):
    return (4*(y**3) +3)/2000
    #return np.cos(np.sqrt(x ** 2 + y ** 2)) * (1 / (np.sqrt(x ** 2 + y ** 2))) * y

def gradient_descent(x, y):
    learning_rate = 0.1
    eps = 0.01
    arr_x = []
    arr_y = []
    arr_z = []
    arr_y.append(y)
    arr_x.append(x)
    z = f(x, y)
    arr_z.append(z)
    print(x, y, f(x, y))
    while d_f_x(x,y) > eps:
        temp_x = x - learning_rate * d_f_x(x,y)
        temp_y = y - learning_rate * d_f_y(x,y)
        x = temp_x
        y = temp_y
        arr_y.append(y)
        arr_x.append(x)
        arr_z.append(f(x,y))
        print(x, y, f(x,y))
    return (arr_x, arr_y, arr_z)

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
#ax.plot_surface(X, Y, Z, rstride=2, cstride=1,
                #cmap='PuRd', edgecolor='none')
ax.contour3D(X, Y, Z, 50, cmap='PuRd')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
result = gradient_descent(4,-1)
arr_x = result[0]
arr_y = result[1]
arr_z = result[2]
'''
for elem in zip(arr_x, arr_y):
    arr_z.append(f(elem[0], elem[1]))
'''
plt.scatter(arr_x, arr_y, arr_z, 'g', 10)

x = [1]
y = [0]
t = [0.8414]
plt.scatter(x, y, t, 'r')
#plt.plot(x,y, 'r')
x = arr_x
y = arr_y
z = arr_z
plt.plot(x,y, z)
plt.show()
print('result')
print(f(1,0))

'''
def function(x):
    return x**6 - 2*(x**3) + 1

def func3d(x, y):
    return -np.sin(10 * (x**2 + y**2)) / 10

def d_function(x):
    return 6*(x**5) - 6*(x**2)

def gradient_descent(x):
    array = []
    array.append(x)
    learning_rate = 0.01
    while d_function(x) != 0:
        x =- learning_rate * d_function(x)
        array.append(x)
        print(x, function(x))
    return array
#array = gradient_descent(1.2)
x = np.arange(-50, 50)
y = function(x)

plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x,y)

#for x in array:
    #plt.scatter(x, function(x))
    
x_interval = (-2, 2)
y_interval = (-2, 2)
x_points = np.linspace(x_interval[0], x_interval[1], 100)
y_points = np.linspace(y_interval[0], y_interval[1], 100)
X, Y = np.meshgrid(x_points, y_points)
func3d_vectorized = np.vectorize(func3d)
Z = func3d_vectorized(X, Y)
plt.figure(figsize=(20, 10))
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap=’terrain’, edgecolor=None)

'''
