import pygame
pygame.init()


class Button:
    def __init__(self, screen, position, text, g_settings):
        self.font = pygame.font.SysFont('calibri', g_settings.button_font_size)
        text_render = self.font.render(text, 1, g_settings.button_font_color)
        x, y, w, h = text_render.get_rect()
        x, y = position
        self.g_settings = g_settings
        y = self.g_settings.screen_height - 2 * self.font.get_height()
        self.screen_rect = screen.get_rect()
        self.rect = pygame.draw.rect(screen, (255, 255, 255), (x - 10, y - 10, w + 20, h + 20))
        self.rect.bottom = self.screen_rect.bottom
        self.rect.bottom = self.screen_rect.bottom
        self.col = screen.blit(text_render, (x, y))






