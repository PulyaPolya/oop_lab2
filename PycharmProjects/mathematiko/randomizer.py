from random import randint
import random

class Random():
    def __init__(self):
        self.dict = {}
        for i in range (1, 14):
            self.dict[i] = 0
        self.number = self.get_random_numbet()
        self.wait_for_random_numb = False
    def get_random_numbet(self):
        number = random.randint(1, 13)
        while self.dict[number] >= 4:
            number = random.randint(1, 13)
        self.dict[number] += 3
        self.number = number
        return number

