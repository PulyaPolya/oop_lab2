import random
import math
def gcd(x, y):
    if x > 0:
        x = -x
    if y < 0:
        y = -y
    while (y):
        x, y = y, x % y

    return x
def func(x):
    return x**2+1
def count_pollard_v1(n,x_0):
    arr=[]
    arr.append(x_0)
    r = 1
    i=0
    while r==1 or r==n:
        for x_i in arr:
            r=gcd(arr[-1]-x_i,n)
            i += 1
            if r!=1 and r!=n:
                break
        x=func(arr[-1])%n
        arr.append(x)

    return (r,i, arr)
def count_pollard_v2(n,x_0):
    arr = []
    arr.append(x_0)
    r = 1
    i=0
    while r == 1 or r == n:
        k=arr.index(arr[-1])
        if k%2==0:
            j=k//2
            r = gcd(arr[k] - arr[j], n)
            i += 1
        x = func(arr[-1])%n
        arr.append(x)

    return (r,i,arr)
def count_k(j):
    h=0
    while 1==1:
        if 2**h<=j and 2**(h+1)>j:
            return 2**h-1
        else:
            h=h+1
def count_pollard_v3(n,x_0):
    arr = []
    arr.append(x_0)
    r = 1
    i = 0
    while r == 1 or r == n:
        j=arr.index(arr[-1])
        if j!=0:
            k=count_k(j)
            r = gcd(arr[j] - arr[k], n)
            i += 1
        x = func(arr[-1]) % n
        arr.append(x)

    return (r, i, arr)
n=7031
print(count_pollard_v1(44729396957,2))
def jacobi_symbol(a,n):
    if gcd(a,n) != 1:
        return 0
    res = 1
    while a != 1:
        if a < 0:
            a = -a
            res = res * (-1)** ((n-1)/2)
        while a % 2 == 0:
            a = a / 2
            res = res * (-1) ** ((n**2 - 1) / 8)
        if a == 1 :
            break

        if a < n:
           temp = a
           a = n
           n = temp
           res = res * (-1) ** ((n - 1) / 2 * ((a-1)/ 2))
        if a > n:
            a = a % n
    if a == 1:
        return 1 * res
def pseudo_simple(a,p):
    if gcd(a,p) != 1:
        return 'no'
    else:
        jac = jacobi_symbol(a, p)
        if jac == -1:
            jac = p - 1
        deg = int((p - 1) / 2)
        pow = a ** deg
        pow = a ** deg
        if jac == pow % p:
            return 'yes'
        else:
            return 'no'
def count_solovei(p, k):
    i = 0
    while i < k:
        x= random.randint(2,p-1)
        if gcd(x,p) == 1:
           if pseudo_simple(a = x, p = p) == 'no':
               return 'no'
           else:
               i += 1
        else:
            return 'no'
    if i == k:
        return 'yes'

def count_r(m, t):
    r = []
    r_prev = 1
    r.append(r_prev)
    for i in range (1, t):
        r_i = (r_prev * 10)
        r_i = r_i % m
        r.append(r_i)
        r_prev = r_i
    return r
def try_divide(n):
    t = len(str(n))
    top_verge = int(math.sqrt(n))
    for m in range (2, top_verge):
        sum = 0
        r = count_r(m, t)
        n_rev= str(n)[::-1]
        for i in range (t):
            sum += int(n_rev[i]) * r[i]
        if sum % m == 0 :
            return m
    return 'plain'
#print(try_divide(44729396957))
def get_fraction(n, k):
    v = 1
    alpha_0=math.sqrt(n)
    alpha = alpha_0
    a=int(alpha)
    u=a
    arr_a=[]
    arr_a.append(a)
    i = 0
    while i < k:
        v = (n - u ** 2) / v
        alpha = (alpha_0 + u) / v
        a = int(alpha)
        u = a * v -u
        arr_a.append(a)
        i += 1
        print('v = ', v, 'alpha = ', alpha, 'a = ', a, 'u = ', u)
    return arr_a

def count_row(arr, n):
    b=1
    b_prev = 0
    b_arr=[]
    b_arr.append(b)
    b_sq = []
    b_sq.append(b)
    for a in arr:
        temp = b
        b = b * a + b_prev
        b = b % n

        b_arr.append(b)
        b_prev = temp
        b_square = (b ** 2) % n
        if b_square > n/2:
            b_square = b_square - n
        b_sq.append(b_square)
    return (b_arr, b_sq)
#print(count_row(get_fraction(25511,15),25511))
print(jacobi_symbol(9073,43))