import numpy as np
import collections
import game_functions as gf
A = [[6,8, 10, 9, 11], [6, 3, 10, 9, 11], [7, 8, 5, 5, 11], [3, 4, 4, 4, 4], [12, 13, 13, 2, 2]]
A = [[4, 2, 8, 8, 13], [10, 2, 7, 7, 10], [4, 11, 3, 6, 11], [5, 12, 6, 5, 12], [1, 3, 9, 9, 1]]
A = np.array(A)
print(gf.count_points(A))
