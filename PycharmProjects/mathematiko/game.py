from settings import Settings
from random_square import RandomSquare
from randomizer import Random
from text import Text
from table import Table
import pygame
import sys
import game_functions as gf
class Game:
    def __init__(self):
        self.g_settings = Settings()
        self.screen = pygame.display.set_mode((self.g_settings.screen_width, self.g_settings.screen_height))
        self.square_positions = gf.get_square_positions()
        self.squares = gf.get_squares(self.screen, self.square_positions)[0]
        self.dict_squares = gf.get_squares(self.screen, self.square_positions)[1]
        keys = self.dict_squares.keys()
        self.table = table = Table(5,self.g_settings, keys)
        self.random = Random()
        self.random_square = RandomSquare(self.screen)
        self.start = True
        self.show_start_buttons = False
