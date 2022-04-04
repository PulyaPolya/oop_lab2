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
    eps = 0.001
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
        print(f'function is {f(x,y)}')
    return (arr_x, arr_y, arr_z)
result = gradient_descent(11,-6)
#arr_x = np.array(result[0])
x = result[0]
y = result[1]
arr_x = []
arr_y = []
i = 0
for elem in x:
    if i % 1000 == 0:
        arr_x.append(elem)
        arr_y.append(y[i])
    i += 1

#arr_y = np.array(result[1])
#print(f'arr_x is {arr_x}, \n  arr_y is {arr_y}')
x = np.arange(0, 10000, 1000)

arr_x = np.array(arr_x)
arr_y = np.array(arr_y)
#plt.xticks(range(1000))
print(len(arr_x), len(arr_y), len(x))
plt.plot(x,f(arr_x, arr_y))
plt.show()