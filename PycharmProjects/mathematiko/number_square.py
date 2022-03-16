import pygame

class Number:
    def __init__(self, screen,rect, square, a,g_settings, big = False):
        self.screen = screen
        if big:
            self.font = pygame.font.SysFont(None, g_settings.random_font_size)
        else:
            self.font = pygame.font.SysFont(None, g_settings.little_font)
        self.img = self.font.render(str(a), True, (0, 0, 0))
        self.x = rect.x
        self.y = rect.y
    def blit(self):
        self.screen.blit(self.img, (self.x, self.y))
