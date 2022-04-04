import numpy
import numpy as np
def special_print(A):
    for arr in A:
        print(arr)
    print('\n')

#A = [[ 1.20, -0.20, 0.30],
    #[-0.20, 1.60, 0.10],
    #[0.30, -0.10, 1.50]]
#B = [-0.6, 0.3, -0.4]

A=[[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
B=[8,-11, -3]
max = -100
for i in range(0, len(A)):
    for elem in A[i]:
        if abs(elem) >max:
            max =abs(elem)
            p_row = i
            q_column = A[p_row].index(elem)
main=A[p_row][q_column]
m = []
for i in range(0, len(A)):
    if i != p_row:
        m.append(A[i][q_column]/main)
    else:
        m.append(0)
#print(m)

for i in range(0, len(A)):
    for j in range (0,len (A[i])):
        B[i] = B[i] - m[i] * A[p_row][j]
        if i != p_row:
            A[i][j]=A[i][j]-m[i]*A[p_row][j]


special_print(A)
print(B)
A_new = []
for i in range(0,len(A)):
    if i != p_row:
        for j in range(0, len(A[0])):
            if j!=q_column:
                A_new.append(A[i][j])
print(A_new)

'''

def gauss(A):
    A_new = A[:]
    n=len(A)
    for k in range (0,n):
        for i in range (0,n+1):
            A_new[k][i]=A_new[k][i]/A[k][k]
        for i in range (k+1,n):
                coef = A_new[i][k]/A_new[k][k]
                for j in range (0, n+1):
                    A_new[i][j]=A_new[i][j]-A_new[k][j] * coef

        A = A_new[:]

        special_print(A)
    for k in range (n-1,-1,-1):
        for i in range (n, -1, -1):
            A_new[k][i]=A_new[k][i] / A[k][k]
        for i in range (k-1,-1,-1):
            coef = A_new[i][k] / A[k][k]
            for j in range (n, -1, -1):
                A_new[i][j] = A_new[i][j] - A_new[k][j] * coef
    res=[]
    for i in range (0,n):
        res.append( A_new[i][n])
    return res
A=[[2, 1, -1, 8], [-3, -1, 2, -11], [-2, 1, 2, -3]]
print(gauss(A))
'''
A = [[ 1.20, -0.20, 0.30, -0.6],
    [-0.20, 1.60, 0.10, 0.3],
    [0.30, -0.10, 1.50, -0.4]]