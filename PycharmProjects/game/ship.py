import pygame.image
class Ship():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.image = pygame.image.load('images/rocket.bmp')
        self.height = 100
        self.width = 50
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx

        self.ai_settings = ai_settings
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.bottom > self.height:
            self.rect.bottom -= self.ai_settings.ship_speed_factor
        if self.moving_down and self. rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
        #self.rect.bottom = self.bottom