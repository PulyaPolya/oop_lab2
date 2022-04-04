import numpy as np
from matrix import Matrix

class Table:
    def __init__(self, size, g_settings, keys):
        self.size = size

        self.matrix = Matrix(g_settings).matrix
        self.counter = 0
        self.wait_for_first_coord = True
        self.wait_for_second_coord = False
        self.coord1 = 0
        self.coord2 = 0
        self.cancel = False
        self.last_deleted_pos = -1
        self.last_deleted_elem = -1
        self.free_squares = []
        for key in keys:
            self.free_squares.append(key)
