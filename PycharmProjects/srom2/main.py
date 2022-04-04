import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
def initial(my_func, xmin,xmax):
  x, y = np.linspace(xmin,xmax,1001), np.linspace(xmin,xmax,1001)
  X, Y = np.meshgrid(x,y)
  Z = my_func(X,Y)
  return X,Y,Z
def plot(func,xmin,xmax):
  X,Y,Z = initial(func,xmin,xmax)
  fig = plt.figure(figsize=(7,7))
  ax = plt.axes(projection='3d')
  ax.plot_surface(X, Y, Z, cmap='jet')
  ax.set_xlabel('x1')
  ax.set_ylabel('x2')
  ax.set_zlabel('y')
  plt.show()
def multimodal_1(x1,x2):
  return x1*np.exp(-(x1**2+x2**2))
def exponential(x1,x2):
  return x1*+x2**2+np.exp((x1**2+x2**2))
def rastrigin(x1,x2):
  return (20+x1**2+x2**2-10*np.cos(2*np.pi*x1)-10*np.cos(2*np.pi*x2))
def isom(x1,x2):
  return -np.cos(x1)*np.cos(x2)*np.exp(-((x1-np.pi)**2 + (x2-np.pi)**2))
def multimodal_2(x1,x2):
  return x1*np.sin(4*np.pi*x1)-x2*np.sin(4*np.pi*x2+np.pi)+1