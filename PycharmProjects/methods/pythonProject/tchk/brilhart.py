import math
import main
from math import exp, sqrt, log, log2
from vectors import add_one
def get_row_a(n, k):
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
        #print('v = ', v, 'alpha = ', alpha, 'a = ', a, 'u = ', u)
    return arr_a
#print(get_fraction(25511,10))
def get_row_b_bsq(arr, n):
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
        if b_square in b_sq:
            pass
        else:
            b_sq.append(b_square)
    return (b_arr, b_sq)

def get_primes():
    file_name= 'prime'
    res=[]
    with open(file_name, 'r') as file:
        content=file.read()
        numbers= content.split()
    for number in numbers:
        res.append(int(number))
    return res
def get_b(n, increment = 0):
    B = []
    B.append(-1)
    primes = get_primes()
    a = 1 / (sqrt(2))
    if increment:
        a += 5 * increment / n
    L=exp((log2(n) * log2(log2(n)))** 0.5)

    limit = L ** a
    for number in primes:
        if number < limit:
            if main.jacobi_symbol(n, number) == 1:
                B.append(number)
        else:
            break
    B.pop(-2)
    return B
#print(get_b(9073))
def get_gladki_vectors(n, b_normal, b_sq, B):
    k = len(B) - 1
    arr = get_row_a(n, k)
    #b_sq = get_row_b_bsq(arr, n)[1]
    gladki = []
    gladki_normal = []
    vectors = {}
    #B.remove(-1)
    for b in b_sq:
        vector = []
        b_value = b
        for prime in B:
            vector_comp = 0
            if b < 0:
                vector_comp += 1
                b = abs(b)
            if main.gcd(b, prime) != 1:
                while main.gcd(b, prime) != 1:
                    b = b / prime
                    vector_comp += 1
            vector.append(vector_comp)
        if abs(b) == 1 and b_value != 1:
            vectors[b_value] = vector
            gladki.append(b_value)
            index = b_sq.index(b_value)
            gladki_normal.append(b_normal[index])
    return (vectors,gladki_normal, gladki)


def get_coef(vectors):
    numb_of_vect = len(vectors)
    arr = []
    for i in range (numb_of_vect):
        arr.append(0)
    #arr = add_one(arr)
    result = []
    keys = list(vectors.keys())
    length = len(vectors[keys[0]])
    for t in range (length ):
        result.append(0)
    zero_arr = result[:]
    start = 0
    while start != 1 or result != zero_arr:
        arr = add_one(arr)
        result = zero_arr[:]
        start = 1
        for k in range (length):
            i = 0
            for number in keys:
                result[k] += vectors[number][k] * arr[i]
                result[k] = result[k] % 2
                i += 1
        print(result)
        print(arr, '\n')
    return arr
#get_x(get_gladki(9073,get_b(9073)))
def get_X_Y(arr_x, vectors, gladki, B, k, n):
    x = 1
    for i in range (len(vectors)):
        x =(x * gladki[i] ** arr_x[i]) %n
    keys = list(vectors.keys())
    y = 1
    length = len(vectors[keys[0]])
    '''
    for j in range(length):
        deg_p = 0
        for number in keys:
            deg_p += vectors[number][j] * arr_x[j]
        y = y * (b[j] ** deg_p) % n
    '''
    #i = 0
    #while i < n:
    for j in range(length):
        deg_p = 0
        i = 0
        for number in keys:
            deg_p += vectors[number][j] * arr_x[i]
            i += 1
        y = y * (B[j] ** deg_p) % n

    y = int(sqrt(y))
    return (x,y)
def get_gcd(x, y, n):
    if main.gcd(x + y, n) != 1:
        return main.gcd(x + y, n)
    else:
        return main.gcd(abs(x - y), n)
'''
n = 9073
print(get_gladki_vectors(n, get_b(n)))
B = get_b(n)
k = len(B) - 1
arr = get_row_a(n, k)
b = get_row_b_bsq(arr, n)[0]
vectors = get_gladki_vectors(n, B)[0]
arr_x = get_coef(vectors)
arr_x_y = (get_X_Y(arr_x,vectors, b, k))
print(arr_x_y)
print(get_gcd(arr_x_y[0], arr_x_y[1], n))
'''
def brilhart_moris(n):
    result = 1
    increment = 0
    X_arr = []
    while result == 1:

        B = get_b(n, increment)
        print(B)
        k = len(B) -1
        arr_a = get_row_a(n, k+1)
        arr_b = get_row_b_bsq(arr_a, n)[0]
        arr_b_sq = get_row_b_bsq(arr_a, n)[1]
        vectors = get_gladki_vectors(n, arr_b, arr_b_sq, B)[0]
        gladki = get_gladki_vectors(n, arr_b, arr_b_sq, B)[1]
        gladki_square = get_gladki_vectors(n, arr_b, arr_b_sq, B)[2]
        print('B',len(B))
        print('gladki', len(gladki))
        #gladki = []
        i = 0
        '''
        while len(gladki) < k+1:
            arr_a = get_row_a(n, k + 1 + i)
            arr_b = get_row_b_bsq(arr_a, n)[0]
            arr_b_sq = get_row_b_bsq(arr_a, n)[1]
            gladki = get_gladki_vectors(n, arr_b, arr_b_sq, B) [1]
            gladki_square = get_gladki_vectors(n, arr_b, arr_b_sq, B) [2]
            i += 1
        '''
        increment += 1
        print(vectors)
        print(gladki)
        print(gladki_square)
        arr_coef = get_coef(vectors)
        X = get_X_Y(arr_coef, vectors,gladki, B, k, n)[0]
        X_arr.append(X)
        Y = get_X_Y(arr_coef, vectors,gladki, B, k, n)[1]
        result = get_gcd(X, Y, n)

    return result
print(brilhart_moris(589))
#589