import pygame


class Square():
    def __init__(self, screen, a, b):
        self.screen = screen
        self.image = pygame.image.load('images/squaree.png')
        self.height = 100
        self.width = 100
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.right = a
        self.rect.bottom = b


    def blitme(self):
        self.screen.blit(self.image, self.rect)


