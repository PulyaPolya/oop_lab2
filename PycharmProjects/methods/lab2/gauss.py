def gaus_way_one(A):
    A_res = A[:]
    forbidden_col = []
    forbidden_rows = []
    n = len(A)
    while n > 0:
        main = find_main(A,forbidden_rows, forbidden_col)[0]
        p = find_main(A, forbidden_rows, forbidden_col)[1]
        q = find_main(A, forbidden_rows, forbidden_col)[2]
        A = change_matrix(A, p, q, forbidden_rows, forbidden_col)
        print_martix(A)
        #A = cross_rows_cols(A, p, q)
        forbidden_rows.append(p)
        forbidden_col.append(q)
        n -= 1
    solutions = get_sol(A,forbidden_rows, forbidden_col)
    check(A, solutions)
def find_main(A, forbidden_rows, forbidden_col):
    n = len(A)
    row = 0
    column = 0
    max = abs(A[0][0])
    for p in range (n):
        for q in range(n):
            if p not in forbidden_rows and q not in forbidden_col:
                if abs(A[p][q]) > max:
                    max = abs(A[p][q])
                    row = p
                    column = q
    return (max, row, column)

def change_matrix(A, p, q, forbidden_rows, forbidden_col):
    n = len(A)
    m = []
    for i in range(n):
        if i != p and p not in forbidden_rows:
            m_i = - A[i][q] / A[p][q]
        else:
            m_i = 0
        m.append(m_i)
    for i in range(n):
        for j in range(n + 1):
            if i not in forbidden_rows and j not in forbidden_col:
                if i != p:
                    A[i][j] += A[p][j] * m[i]
    return A

def print_martix(A):
    for arr in A:
        print(arr)
    print('\n')

def cross_rows_cols(A, p, q):
    A_new = []
    for arr in A:
        arr.pop(q)
    for arr in A:
        if A.index(arr) != p:
            A_new.append(arr)
    return A_new

def copy_A(A):
    A_res = []
    for arr in A:
        A_res.append(arr)
    return A_res

def get_sol(A,forbidden_rows, forbidden_col ):
    n = len(A)
    solutions = []
    for t in range(n):
        solutions.append(0)
    '''
    for t in range(n):
        solutions.append(0)
        if t not in forbidden_rows:
            i = t
        if t not in forbidden_col:
            j = t
    '''
    while forbidden_rows:
        i = forbidden_rows[-1]
        j = forbidden_col[-1]
        sum = 0
        for k in range(n):
            sum += solutions[k] * A[i][k]
        sum = A[i][n] - sum
        x = sum / A[i][j]
        #solutions[j] = A[i][n] / A[i][j]
        forbidden_rows.pop(-1)
        forbidden_col.pop(-1)
        solutions[j] = x
    for i in range(n):
        solutions[i] = round(solutions[i], 6)
    print(solutions)
    return solutions

def check(A, solutions):
    n = len(A)
    result = []
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += solutions[j] * A[i][j]
        sum -= A[i][n]
        result.append(sum)
    print(result)
#def edit_res_matrix(A, A_res, arr_coef):

#A=[[3, 2, -5, -1], [2, -1, 3, 13], [1, 2, -1, 9]]
A = [[1, 5, 3, -4, 20], [3, 1, -2, 0, 9], [5, -7, 0, 10, -9], [0, 3, -5, 0, 1]]
A1 = [[3.81, 0.25, 1.28, 1.75, 4.21], [2.25, 1.32, 5.58, 0.49, 7.47], [5.31, 7.28, 0.98, 1.04, 2.38], [10.39, 2.45, 3.35, 2.28, 11.48]]
gaus_way_one(A1)
