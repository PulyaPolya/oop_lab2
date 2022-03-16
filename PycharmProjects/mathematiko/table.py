import numpy as np


class Table():
    def __init__(self, size):
        self.size = size
        matrix = []
        self.Matix = []
        row = []
        for j in range(self.size):
            row.append(0)
        matrix.append(row)
        self.Matix = np.array(matrix)