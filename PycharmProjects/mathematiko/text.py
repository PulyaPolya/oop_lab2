import pygame

class Text:
    def __init__(self, screen, g_settings):
        self.full_table = 'This table is full'
        self.position_taken = 'This position is taken'
        self.screen = screen

        self.g_settings = g_settings
        self.start = 'Welcome to mathematiko!'
        self.image = pygame.image.load('images/rules.jpg')
        self.image = pygame.transform.scale(self.image, (g_settings.rules_height, g_settings.rules_height))
        self.rect = self.image.get_rect()

        self.show_greetings = True


    def error_message(self, problem):
        font = pygame.font.SysFont(None, self.g_settings.warning_text_size)
        if problem == 'full':
            img = font.render(self.full_table, True, self.g_settings.random_font_color)
        else:
            img = font.render(self.position_taken, True, self.g_settings.random_font_color)
        self.screen.blit(img, self.g_settings.warning_text_position)
    def result(self, number):
        text = 'Your score is ' + str(number)
        font = pygame.font.SysFont(None, self.g_settings.warning_text_size)
        img = font.render(text, True, self.g_settings.random_font_color)
        self.screen.blit(img, self.g_settings.result_position)
    def start_game(self):
        font = pygame.font.SysFont(None, self.g_settings.warning_text_size)
        img = font.render(self.start, True, self.g_settings.random_font_color)
        self.screen.blit(img, (pygame.display.get_surface().get_width()/2 - font.size(self.start)[0]/2,
                               pygame.display.get_surface().get_height()/2 - font.size(self.start)[1]/2))
    def show_rules(self):
        self.screen.blit(self.image, self.rect)