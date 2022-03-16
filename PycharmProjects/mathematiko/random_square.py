import pygame


class RandomSquare():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/squaree.png')
        self.height = 200
        self.width = 200
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = 900
        self.rect.bottom = 400
        self.wait_for_first_coord = True
        self.wait_for_second_coord = False
        self.coord1 = 0
        self.coord2 = 0
        self.display_number = False


    def blitme(self):
        self.screen.blit(self.image, self.rect)
