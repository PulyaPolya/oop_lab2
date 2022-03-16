class Settings():
    def __init__(self):
        self.size = 5
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (241, 168, 255)
        self.square_color = (0, 0, 0)
        self.font_tiles_size = 24
        self.random_window_x =  700
        self.random_window_y = 200
        self.random_window_size = 100
        self.random_font_size = 80
        self.random_font_color = (0, 0, 0)
        self.little_font = 24
        self.random_rect_color = (0, 100, 255)
        self.random_rect_width = 3
        self.warning_text_position = (600, 100)
        self.warning_text_size = 50
        self.result_position = (600, 400)
        self.start_game = 0
        self.start_game_position = (self.screen_width/2, self.screen_height/2)
        self.rules_height = 500
        self.show_rules = False
        self.button1_position = (200, 500)
        self.button2_position = (500, 500)
        self.button_font_size = 40
        self.button_font_color = (0, 0, 0)





    def get_square_positions(self):
        arr = []
        x = 100
        y = 100
        for j in range (5):

            for i in range (5):
                position = []
                position.append(y)
                position.append(x)
                arr.append(position)
                x += 100
            x = 100
            y += 100
        return arr
