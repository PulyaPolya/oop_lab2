import sys
import numpy as np
import win_combinations as w
from square import Square
import pygame
from number_square import Number
from custom_exception import FullTable, TakenSpot
import button as btt
import pygame
from settings import Settings
from random_square import RandomSquare
from randomizer import Random
from text import Text
from table import Table
from game import Game


def get_square_positions():
    arr = []
    x = 100
    y = 100
    for j in range(5):
        for i in range(5):
            position = []
            position.append(y)
            position.append(x)
            arr.append(position)
            x += 100
        x = 100
        y += 100
    return arr


def np_to_arr(col):
    array = []
    for elem in col:
        array.append(elem)
    return array

def run_game(game):
    pygame.init()
    if game.start:
        game = init_game()
        game.start = False
    screen = game.screen
    square_positions = game.square_positions
    dict_squares = game.dict_squares
    g_settings = game.g_settings
    squares = game.squares
    random = game.random
    random_square = game.random_square
    table = game.table
    '''
    g_settings = Settings()
    screen = pygame.display.set_mode((g_settings.screen_width, g_settings.screen_height))
    square_positions = get_square_positions()
    squares = get_squares(screen,  square_positions)[0]
    dict_squares =get_squares(screen,  square_positions)[1]
    keys = dict_squares.keys()
    table = Table(5,g_settings, keys)
    random = Random()
    random_square = RandomSquare(screen)
    '''
    arr_numbers = []
    text = Text(screen,g_settings)
    while True:
        update_screen(screen, g_settings, squares, random, random_square, dict_squares,
                         arr_numbers,  text,  table, game)

def init_game():
    game = Game()
    return game


def count_points(A):
    sum = 0
    for i in range (len(A)):
        arr = np_to_arr(A[i])
        d = w.count_row(arr)
        sum += d
    for j in range (len(A)):
        arr = np_to_arr(A[:,j])
        d = w.count_row(arr)
        sum += d

    diag_1 = []
    for i in range(len(A)):
        diag_1.append(A[i][i])
    sum += w.count_row(diag_1, 1)
    diag_2 = []
    for j in range (len(A)-1, -1, -1):
        diag_2.append(A[j][len(A) - j - 1])
    sum += w.count_row(diag_2, 1)
    return sum


def get_squares(screen, squares_pos):
    squares = []
    dict_squares = {}
    for position in squares_pos:
        square = Square(screen, position[0], position[1])
        i = int(position[0] / 100)
        j = int(position[1] / 100)
        index = str(i) + str(j)
        dict_squares[index] = square
        squares.append(square)
    return (squares, dict_squares)


def check_events(random, random_square, g_settings, arr_numbers, table):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            random_square.show_number = True
            if event.key == pygame.K_1:
               get_coords(1, random_square, random, table)
            elif event.key == pygame.K_2:
               get_coords(2, random_square, random, table)
            elif event.key == pygame.K_3:
               get_coords(3, random_square, random, table)
            elif event.key == pygame.K_4:
               get_coords(4, random_square, random, table)
            elif event.key == pygame.K_5:
               get_coords(5, random_square, random, table)
            elif event.key == pygame.K_z:
                mods = pygame.key.get_mods()
                if mods & pygame.KMOD_CTRL:
                    if not table.cancel:
                        table.wait_for_first_coord = True
                        table.wait_for_second_coord = False
                        arr_numbers.pop(-1)
                        table.free_squares.insert(table.last_deleted_pos,
                                                          table.last_deleted_elem)
                        random.wait_for_random_numb = False
                        random.number = random.previous_number
                        table.counter -= 1
                        table.cancel = True
        elif event.type == pygame.QUIT:
                sys.exit()


def check_buttons(b1, b2, text, g_settings):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if b1.col.collidepoint(pygame.mouse.get_pos()):
                g_settings.show_rules = True
                text.show_greetings = False
            elif b2.col.collidepoint(pygame.mouse.get_pos()):
                g_settings.start_game = 1
        elif event.type == pygame.QUIT:
                sys.exit()


def randomize(random, random_square, table):
    random.wait_for_random_numb = True
    table.wait_for_first_coord = True
    table.wait_for_second_coord = False
    random_square.display_number = False


def get_coords(number, random_square, random, table):
    table.cancel = False
    if table.wait_for_first_coord:
        table.coord2 = number
        table.wait_for_first_coord = False
        table.wait_for_second_coord = True
        random_square.display_number = False
        random.wait_for_random_numb = False
    elif table.wait_for_second_coord:
        table.coord1 = number
        table.wait_for_first_coord = True
        table.wait_for_second_coord = False
        random_square.display_number = True
        random.wait_for_random_numb = True


def show_little_numbers(squares, screen, g_settings, table):
    a = 1
    i = 2
    for square in squares:
        if a <= 5:
            if table.coord2 == a:
                color = True
            else:
                color = False
            number = Number(screen, square.rect, str(a), g_settings, color)
            number.blit()
        elif a % 5 == 1:
            if table.coord1 == i:
                color = True
            else:
                color = False
            number = Number(screen, square.rect,str(i), g_settings, color)
            number.blit()
            i += 1
        a += 1


def update_matrix(coord1, coord2, number, table):
    table.matrix[coord1 -1][coord2 -1] = number
    table.counter += 1


def show_squares(squares):
    for square in squares:
        square.blitme()


def add_new_number(random_square, dict_squares, screen, number,g_settings,
                   arr_numbers, table):
    if table.counter == 25:
        raise FullTable
    if random_square.display_number:
        a = table.coord1
        b = table.coord2
        coord_found = 0
        if table.free_squares:
            #print(table.free_squares)
            for elem in table.free_squares:
                if elem == str(a) + str(b):
                    square = dict_squares[elem]
                    square.width = 500
                    display_number = Number(screen, square.rect,str(number), g_settings,False, True)
                    arr_numbers.append(display_number)
                    table.last_deleted_pos = table.free_squares.index(elem)
                    table.last_deleted_elem = elem
                    table.free_squares.remove(elem)
                    coord_found = 1
                    random_square.display_number = False
                    update_matrix(a, b,  number, table)
                    break
            if coord_found == 0:
                raise TakenSpot
        else:
            raise FullTable


def show_big_numbers(arr_numbers):
    for number in arr_numbers:
        number.blit()


def show_random_rect(g_settings, number, screen):
    font = pygame.font.SysFont(None, g_settings.random_font_size)
    img = font.render(str(number), True, g_settings.random_font_color)
    rect = pygame.draw.rect(screen, g_settings.random_rect_color, (g_settings.random_window_x, g_settings.random_window_y,
                                                    g_settings.random_window_size, g_settings.random_window_size),
                            g_settings.random_rect_width)
    screen.blit(img, (g_settings.random_window_x + rect.width / 2 - img.get_width() / 2,
                      g_settings.random_window_y + rect.height / 2 - img.get_height() / 2))


def start(g_settings, screen, text):
    screen.fill(g_settings.bg_color)
    if text.show_greetings:
        text.start_game()


def menu(g_settings, screen, text):
    start(g_settings, screen, text)
    b1 = btt.Button(screen, g_settings.button1_position, "Show rules", g_settings)
    b2 = btt.Button(screen, g_settings.button2_position, "Start a new game", g_settings)
    check_buttons(b1, b2, text, g_settings)
    if g_settings.show_rules:
        text.show_rules()

def check_buttons_new(b3, b4, text, g_settings, game):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if b3.col.collidepoint(pygame.mouse.get_pos()):
                g_settings.show_rules = True
                text.show_greetings = False
            elif b4.col.collidepoint(pygame.mouse.get_pos()):
                print('aaaa')
                game.start = True
                run_game(game)
                g_settings.start_game = 1
        elif event.type == pygame.QUIT:
            sys.exit()

def update_screen(screen, g_settings, squares, random, random_square, dict_squares,
                  arr_numbers, text, table, game):

    check_events(random, random_square, g_settings, arr_numbers,  table)
    if g_settings.start_game == 0:
        menu(g_settings, screen, text)
    else:
        screen.fill(g_settings.bg_color)
        show_squares(squares)
        number = random.number
        try:
            if random_square.show_number:
                add_new_number(random_square, dict_squares, screen, number, g_settings, arr_numbers, table)
        except TakenSpot:
            text.error_message('taken')
            game.show_start_buttons = True

        except FullTable:
            text.error_message('full')
            m = np.array(table.matrix)
            text.result(count_points(m))
            print(table.matrix)
        if game.show_start_buttons:
            b3 = btt.Button(screen, g_settings.button1_position, "Show rules", g_settings)
            b4 = btt.Button(screen, g_settings.button2_position, "Start a new game", g_settings)
            check_buttons_new(b3, b4, text, g_settings, game)
        show_little_numbers(squares, screen, g_settings, table)
        show_random_rect(g_settings, number, screen)
        show_big_numbers(arr_numbers)
        if random.wait_for_random_numb:
            random.previous_number = random.number
            random.get_random_number()
            random.wait_for_random_numb = False
    pygame.display.flip()

