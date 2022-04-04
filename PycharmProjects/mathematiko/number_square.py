import pygame


class Number:
    def __init__(self, screen, rect, a, g_settings, color=False, big=False ):
        self.screen = screen
        if big:
            self.font = pygame.font.SysFont(None, g_settings.random_font_size)
        else:
            self.font = pygame.font.SysFont(None, g_settings.little_font)
        if not color:
            self.color = g_settings.font_color
        else:
            self.color = g_settings.font_special_color
        self.img = self.font.render(str(a), True, self.color)
        self.x = rect.x
        self.y = rect.y

    def blit(self):
        self.screen.blit(self.img, (self.x, self.y))
