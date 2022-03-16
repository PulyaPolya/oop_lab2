from settings import Settings
import numpy as np
import game_functions as gf
class Matrix:
    def __init__(self, g_settings):
        self.g_setttings = g_settings
        self.size = g_settings.size
        self.matrix = self.fill_matrix_with_zero()
        self.counter = 0
    def fill_matrix_with_zero(self):
        matrix = []
        for j in range(5):
            row = []
            for i in range(self.size):
                row.append(0)
            matrix.append(row)
        return matrix

