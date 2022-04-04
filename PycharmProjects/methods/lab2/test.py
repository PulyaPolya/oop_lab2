A = [[1, 5, 3, -4, 20], [3, 1, -2, 0, 9], [5, -7, 0, 10, -9], [0, 3, -5, 0, 1]]
A_new = A[:]
A_new.pop(A_new[1][1])
print(A)
print(A_new)
for i in range(n):
    for j in range(n + 1):
        if i not in forbidden_rows and j not in forbidden_col:
            print(A[i][j])