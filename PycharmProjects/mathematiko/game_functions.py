import sys

import numpy as np

import win_combinations as w
from square import Square
import pygame
from number_square import Number
from custom_exception import FullTable, TakenSpot
import  button as btt
def np_to_arr(col):
    array = []
    for elem in col:
        array.append(elem)
    return array


def count_points(A):
    sum = 0
    for i in range (len(A)):
        arr = np_to_arr(A[i])
        d = w.count_row(arr)
        sum += d
    for j in range (len(A)):
        arr = np_to_arr(A[:,j])
        d = w.count_row(arr)
        if arr == [1, 10, 11, 12, 13]:
            #print('d is ')
            #print(d)
            pass
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


def check_events(random, random_square, g_settings):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                randomize(random, random_square)
                g_settings.start_game = 1
                '''
                random.wait_for_random_numb = True
                random_square.wait_for_first_coord = True
                random_square.wait_for_second_coord = False
                random_square.display_number = False
                '''
            elif event.key == pygame.K_1:
               get_coords(1, random_square, random)
            elif event.key == pygame.K_2:
               get_coords(2, random_square, random)
            elif event.key == pygame.K_3:
               get_coords(3, random_square, random)
            elif event.key == pygame.K_4:
               get_coords(4, random_square, random)
            elif event.key == pygame.K_5:
               get_coords(5, random_square, random)

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

def randomize(random, random_square):
    random.wait_for_random_numb = True
    random_square.wait_for_first_coord = True
    random_square.wait_for_second_coord = False
    random_square.display_number = False

def get_coords(number, random_square, random):
    if random_square.wait_for_first_coord:
        random_square.coord2 = number
        random_square.wait_for_first_coord = False
        random_square.wait_for_second_coord = True
        random_square.display_number = False
    elif random_square.wait_for_second_coord:
        random_square.coord1 = number
        random_square.wait_for_first_coord = True
        random_square.wait_for_second_coord = False
        random_square.display_number = True
        random.wait_for_random_numb = True

def show_little_numbers(squares, screen, g_settings):
    a = 1
    i = 2
    for square in squares:
        square.blitme()
        if a <= 5:
            number = Number(screen, square.rect, square, str(a), g_settings)
            number.blit()
        elif a % 5 == 1:
            number = Number(screen, square.rect, square, str(i), g_settings)
            number.blit()
            i += 1
        a += 1


def update_matrix(coord1, coord2, matrix, number):
    matrix.matrix[coord1 -1][coord2 -1] = number
    matrix.counter += 1


def add_new_number(random_square, dict_squares, screen, number,g_settings,
                   arr_numbers, free_squares, matrix):
    if matrix.counter == 25:
        raise FullTable
    if random_square.display_number:
        a = random_square.coord1
        b = random_square.coord2
        coord_found = 0
        if free_squares:
            print(free_squares)
            for elem in free_squares:
                if elem == str(a) + str(b):
                    square = dict_squares[elem]
                    square.width = 500
                    display_number = Number(screen, square.rect, square, str(number), g_settings, True)
                    arr_numbers.append(display_number)
                    free_squares.remove(elem)
                    coord_found = 1
                    random_square.display_number = False
                    update_matrix(a, b, matrix, number)
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

    if g_settings.show_rules == True:
        text.show_rules()
def update_screen(screen, g_settings, squares, random, random_square, dict_squares,
                  arr_numbers, free_squares, text, matrix):
    if g_settings.start_game == 0:

        menu(g_settings, screen, text)
        #g_settings.start_game = 1

    else:
        screen.fill(g_settings.bg_color)
        show_little_numbers(squares, screen, g_settings)
        number = random.number

        try:
            add_new_number(random_square, dict_squares, screen, number, g_settings, arr_numbers, free_squares, matrix)
        except TakenSpot:
            text.error_message('taken')
        except FullTable:
            text.error_message('full')
            m = np.array(matrix.matrix)
            text.result(count_points(m))
            print(matrix.matrix)
        show_random_rect(g_settings, number, screen)
        show_big_numbers(arr_numbers)
        if random.wait_for_random_numb:
            number = random.get_random_numbet()
            random.wait_for_random_numb = False
    pygame.display.flip()
