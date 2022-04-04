A=[[2, 1, -1, 8], [-3, -1, 2, -11], [-2, 1, 2, -3]]
A=[[3, 2, -5, -1], [2, -1, 3, 13], [1, 2, -1, 9]]
A_beg=A[:]
def special_print(A):
    for arr in A:
        print(arr)
    print('\n')
n=len(A)
for e in range (n):
    for i in range (e,n):
        if A[i][e] != e:
            elem = A[i][e]
            break
    A_new=A[:]
    for k in range (e+1, n):
        p=A[k][e]

        #m = A[k][e] / elem
        for j in range(e,n+1):
            A_new[k][j]=A_new[k][j] - A[e][j] * p / elem
        A=A_new[:]
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
#print(res)
answ=[]
A_beg=[[3, 2, -5, -1], [2, -1, 3, 13], [1, 2, -1, 9]]
for i in range (n):
    sum=0
    for j in range (n):
        sum += A_beg[i][j] * res[j]
    answ.append(sum)

print(answ)