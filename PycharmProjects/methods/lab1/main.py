eps = 0.00001
def function(x):
    return 2*(x**5)+3*(x**2)-2*x-6
def d_function(x):
    return 10*(x**4)+6*x-2
def count_x_k(x):
    return x-function(x)/d_function(x)
def get_intervals():
    x = -1000
    arr = []
    sol = []
    while x < 1000:
        y = x + 0.01
        if function(x) * function(y) < 0:
            arr.append((x, y))
        elif function(x) * function(y) == 0:
            if function(x) == 0:
                sol.append(x)
            elif function(y) == 0:
                sol.append(y)
        x = y
    return arr
def newtown():
    arr=get_intervals()

    for i in range (len(arr)):
        a= arr[i][0]
        b= arr[i][1]
        x0=a
        x1=count_x_k(x0)
        if x1<a or x1>b:
            x0=b
            x1=count_x_k(x0)
        x_k=x0
        x_k1=x1
        numb_iteration=0
        while(abs(x_k1-x_k)>eps):
            t=x_k1
            x_k=x_k1
            x_k1=count_x_k(t)
            numb_iteration+=1
        print('Newton')
        print('Solution: ', round(x_k1,4))
        print('Result: ', round(function(round(x_k1,4)),4))
        print('Number of iterations ', numb_iteration)
def count_c(c_i,b):
    c=(c_i*function(b)-b*function(c_i))/(function(b)-function(c_i))
    return c
def chord():
    arr = get_intervals()
    for i in range (len(arr)):
        a= arr[i][0]
        b= arr[i][1]
        c_i=a
        c_i1=count_c(c_i,b)
        numb_iteration = 0
        while (abs(c_i1-c_i)>eps):
            t=c_i1
            c_i=c_i1
            c_i1=count_c(c_i,b)
            numb_iteration += 1
        print('Chord')
        print('Solution: ', round(c_i1, 4))
        print('Result: ', round(function(round(c_i1, 4)), 4))
        print('Number of iterations ', numb_iteration)
def count_middle(a,b):
    return (a+b)/2
def bisection():
    arr = get_intervals()
    for i in range(len(arr)):
        a = arr[i][0]
        b = arr[i][1]
        numb_iteration = 0
        while (abs(a-b)>eps):
            c=count_middle(a,b)
            numb_iteration += 1
            if function(a)*function(c)<0:
                b=c
            elif function(b)*function(c)<0:
                a=c
        print('Bisection')
        print('Solution: ',round(c, 4))
        print('Result: ', round(function(round(c, 4)), 4))
        print('Number of iterations ', numb_iteration)


newtown()
chord()
bisection()
