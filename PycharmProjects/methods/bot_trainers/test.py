
import math

n=int(input())
x=math.floor(math.sqrt(n))
y=0
r=x**2-y**2-n
while r!=0:
    if r>0:
        y=y+1
    elif r<0:
        x=x+1
    r=x**2-y**2-n
    print (x,y)
a=x+y
b=x-y
print('a= ',a,'b= ',b)
print(a*b)


def gcd(x, y):
    while (y):
        x, y = y, x % y

    return x
def func(x):
    return x**2-1
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
print(count_pollard_v1(n,5))
print(count_pollard_v2(n,5))
print(count_pollard_v3(n,5))
