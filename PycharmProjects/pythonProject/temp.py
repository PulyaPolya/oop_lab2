import matplotlib.pyplot as plt
import numpy as np
from numpy import cos, sin, pi, exp
def f(x):
    #return x[0]**2 + x[1]**2 - np.cos(18*x[0]) - np.cos(18*x[1])
    return x[0]**4 + x[1]**4+ np.sqrt(2 + x[0]**2 + x[1]**2) - 2*x[0] - 3*x[1]
def grad(x):
    #return np.array([x[0]*2 + 18*np.sin(18*x[0]), x[1]*2 + 18*np.sin(18*x[1])])
    return np.array([4*(x[0]**3)+ x[0]/np.sqrt(x[0]**2+x[1]**2+2)-2,4*(x[1]**3)+ x[1]/np.sqrt(x[0]**2+x[0]**2+2)-3])
x = np.array([1,1])
k=0
x_old = np.array([1.1,1.1])
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
print(np.around(x))
print(f(x))
print(k)