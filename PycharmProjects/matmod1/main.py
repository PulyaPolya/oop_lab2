from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
import math

x = [0.024, 0.038, 0.04, 0.045, 0.047, 0.0578, 0.0629, 0.0629, 0.063, 0.064, 0.0678, 0.0691, 0.071, 0.0742, 0.0752, 0.077, 0.0779,
     0.0781,
     0.0787,
     0.0789,
     0.0791,
     0.0862,
     0.0867,
     0.0877,
     0.089,
     0.0897,
     0.096,
     0.098,
     0.099]
y = [11.7, 12.7, 15.5, 16.8, 16.7, 17.5, 18.5, 18.7, 18.8, 19.5, 20.8, 20.3, 23.3, 23.2, 23.7, 24.4, 28.9,
     25.8,
     29.5,
     23.3,
     22.5,
     26.2,
     29.7,
     33.8,
     35,
     32,
     40,
     41,
     43.8]
i = 0
aver_x = 0
while i < 29:
    aver_x += x[i]
    i = i + 1
aver_x = aver_x / 29
i = 0
aver_y = 0
while i < 29:
    aver_y += y[i]
    i = i + 1
aver_y = aver_y / 29
sum_x = aver_x * 29
sum_y = aver_y * 29
i = 0
s_x2 = 0
while i < 29:
    s_x2 += x[i] * x[i]
    i = i + 1
myltiply_xy = 0
i = 0
while i < 29:
    myltiply_xy = myltiply_xy + x[i] * y[i]
    i = i + 1
determinant = 29 * s_x2 - sum_x * sum_x
det1 = sum_y * s_x2 - sum_x * myltiply_xy
det2 = 29 * myltiply_xy - sum_y * sum_x
a1 = det1 / determinant
a2 = det2 / determinant
yT1= [0] * 29
i=0
while i<29:
    yT1[i]= a2 * x[i] + a1
    i=i+1
sum4_1=0
sum5_1 =0
i=0
while i<29:
    sum4_1 = sum4_1 + (y[i] - yT1[i]) * (y[i] - yT1[i])
    sum5_1 = sum5_1 + (y[i]-aver_y)*(y[i]-aver_y)
    i=i+1
coef_det1= 1- sum4_1/sum5_1
print("Coef a2", a2)
print("Coef_det1=", coef_det1)

x1= np.array(x)
y1= x1*a2+a1
#plt.plot(x1,y1)
#plt.show()
i=0
s1=0
s2=0
s_sqx=0
s_sqy=0
while i<29:
    s1= s1+ (x[i]-aver_x)*(y[i]-aver_y)
    s_sqx=s_sqx+ (x[i]-aver_x)**2
    s_sqy = s_sqy + (y[i] - aver_y) ** 2
    i=i+1
s_sqx= sqrt(s_sqx)
s_sqy= sqrt(s_sqy)
coef_corel= s1/s_sqx/s_sqy
print ("Coef corellation =", coef_corel)
s_x3=0
i=0
while i<29:
    s_x3= s_x3 + x[i] ** 3
    i=i+1
s_x4=0
i=0
while i<29:
    s_x4= s_x4 + x[i] ** 4
    i=i+1
x2_y=0
i=0
while i<29:
    x2_y= x2_y + x[i] * x[i] * y[i]
    i=i+1
determinant = 29 * s_x2 * s_x4 + sum_x * s_x3 * s_x2 + s_x3 * sum_x * s_x2 - s_x2 ** 3 - s_x4 * sum_x * sum_x - s_x3 * s_x3 * 29
d1= sum_y * s_x2 * s_x4 + s_x2 * myltiply_xy * s_x3 + x2_y * sum_x * s_x3 - x2_y * s_x2 * s_x2 - s_x3 * sum_y * s_x3 - s_x4 * myltiply_xy * sum_x
d2= 29 * myltiply_xy * s_x4 + s_x2 * s_x3 * sum_y + x2_y * sum_x * s_x2 - s_x2 * myltiply_xy * s_x2 - s_x4 * sum_x * sum_y - x2_y * 29 * s_x3
d3= 29 * s_x2 * x2_y + sum_x * myltiply_xy * s_x2 + sum_y * sum_x * s_x3 - s_x2 * s_x2 * sum_y - x2_y * sum_x * sum_x - 29 * s_x3 * myltiply_xy
b0= d1/determinant
a1= d2/determinant
a2= d3/ determinant
i=0
yT2= [0] * 29
while i<29:
    yT2[i]= b0+ a1*x[i]+ a2*x[i]**2
    i=i+1
sum4_2=0
sum5_2 =0
i=0
while i<29:
    sum4_2 = sum4_2 + (y[i] - yT2[i]) **2
    sum5_2 = sum5_2 + (y[i]-aver_y)*(y[i]-aver_y)
    i=i+1
coef_det2= 1- sum4_2/sum5_2
print("Coef_det2= ", coef_det2)
x2= np.array(x)
y2= b0+ a1*x2+ a2*x2**2
#plt.plot(x2,y2)
#plt.show()
#log
ln_x=0
i=0
lnx_y=0
while i<29:
    ln_x= ln_x+math.log(x[i])
    i=i+1
i = 0
ln_xln=0
while i < 29:
    lnx_y= lnx_y + y[i] * math.log(x[i])
    ln_xln= ln_xln + (math.log((x[i]))) ** 2
    i = i + 1
ar1=np.array([[ln_x, 29], [ln_xln, ln_x]])
ar2= np.array([sum_y, lnx_y])
sol1= np.linalg.solve(ar1, ar2)
a1= sol1[0]
b1=sol1[1]
y3= a1*np.log(x2)+b1
i=0
yT_ln= [0] * 29
while i<29:
    yT_ln[i]=a1*math.log(x[i])+b1
    i=i+1
sum4_ln=0
sum5_ln =0
i=0
while i<29:
    sum4_ln = sum4_ln + (y[i] - yT_ln[i]) **2
    sum5_ln = sum5_ln + (y[i]-aver_y)**2
    i=i+1
coef_det_ln= 1- sum4_ln/sum5_ln
print("Coef_det_ln= ", coef_det_ln)
plt.plot(x2,y3)
#plt.show()
ln_y=0
x_lny=0
i=0
while i<29:
    ln_y= ln_y+ math.log(y[i])
    x_lny= x_lny+ x[i]*math.log(y[i])
    i= i+1
ar3= np.array([[29, sum_x],[sum_x, s_x2]])
ar4= np.array([ln_y, x_lny])
sol2= np.linalg.solve(ar3, ar4)
#print(sol2)

t1= sol2[0]
t2=sol2[1]
a= math.exp(t1)
b= math.exp(t2)
y4= a*np.power(b, x2)
plt.plot(x2,y4)
plt.show()
i=0
yT_exp= [0] * 29
while i<29:
    yT_exp[i]=a*b**x[i]
    i=i+1
sum4_exp=0
sum5_exp =0
i=0
while i<29:
    sum4_exp = sum4_exp + (y[i] - yT_exp[i]) **2
    sum5_exp = sum5_exp + (y[i]-aver_y)**2
    i=i+1
coef_det_exp= 1- sum4_exp/sum5_exp
print("Coef_detexp= ", coef_det_exp)