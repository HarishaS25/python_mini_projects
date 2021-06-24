import pygame
import sys
import time
import numpy as np

pygame.init()

rows = 3
cols = 3
width = 800
height = width
bg_colour = (0, 250, 154)
line_colour = (32, 178, 170)
line_width = 10
circle_colour = (238, 232, 170)
space = 50
win_line_space = 25
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("TIC-TAC-TOE")
screen.fill(bg_colour)

# creating 3 * 3 matrix
board = np.zeros((rows, cols))


def is_board_full():
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 0:
                return False
    return True


def fill_block(row, col, player):
    board[row][col] = player


def is_block_available(row, col):
    return board[row][col] == 0


def check_winner(player):
    # checking horizontal matches
    for i in range(rows):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            horizontal_winner(i, player)
            return True

    # checking vertical winner:
    for i in range(cols):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            vertical_winner(i, player)
            return True

    # checking asc diagonal winner
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        asc_diagonal_winner(player)
        return True

    # checking desc diagonal winner
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        desc_diagonal_winner(player)
        return True

    return False


def horizontal_winner(row, player):
    if player == 1:
        win_line_colour = circle_colour
    else:
        win_line_colour = line_colour
    line_start = (0+win_line_space, row*width//3+width//6)
    line_end = (width-win_line_space, row*width//3+width//6)
    pygame.draw.line(screen, win_line_colour, line_start, line_end, line_width)


def vertical_winner(col, player):
    if player == 1:
        win_line_colour = circle_colour
    else:
        win_line_colour = line_colour
    line_start = (col*width//3+width//6, win_line_space)
    line_end = (col*width//3+width//6, width-win_line_space)
    pygame.draw.line(screen, win_line_colour, line_start, line_end, line_width)


def asc_diagonal_winner(player):
    if player == 1:
        win_line_colour = circle_colour
    else:
        win_line_colour = line_colour
    line_start = (win_line_space, win_line_space)
    line_end = (width-win_line_space, width-win_line_space)
    pygame.draw.line(screen, win_line_colour, line_start, line_end, line_width)


def desc_diagonal_winner(player):
    if player == 1:
        win_line_colour = circle_colour
    else:
        win_line_colour = line_colour
    line_start = (width-win_line_space, win_line_space)
    line_end = (win_line_space, width-win_line_space)
    pygame.draw.line(screen, win_line_colour, line_start, line_end, line_width)


def draw_player_symbol(row, col, player):
    if player == 1:
        pygame.draw.circle(screen, circle_colour, (col*width//3+width//6, row*width//3+width//6), width//6-space, 15)
    else:
        line1_start = (col * width//3+space, row*width//3+space)
        line1_end = (col * width//3+width//3-space, row*width//3+width//3-space)
        line2_start = (col*width//3+width//3-space, row*width//3+space)
        line2_end = (col*width//3+space, row*width//3+width//3-space)
        pygame.draw.line(screen, line_colour, line1_start, line1_end, 20)
        pygame.draw.line(screen, line_colour, line2_start, line2_end, 20)


def draw_lines():
    pygame.draw.line(screen, line_colour, (width//3, 0), (width//3, width), line_width)  # first vertical line
    pygame.draw.line(screen, line_colour, (2 * width//3, 0), (2 * width//3, width), line_width)  # second vertical line
    pygame.draw.line(screen, line_colour, (0, width//3), (width, width//3), line_width)  # first horizontal line
    pygame.draw.line(screen, line_colour, (0, 2*width//3), (width, 2*width//3), line_width)  # second horizontal line


draw_lines()


def restart():
    screen.fill(bg_colour)
    draw_lines()
    global cur_player
    cur_player = 1
    global game_over
    game_over = False
    for i in range(rows):
        for j in range(cols):
            board[i][j] = 0


cur_player = 1

game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            x_value = event.pos[0]
            y_value = event.pos[1]

            row_num = int(y_value//(width/3))
            col_num = int(x_value//(width/3))

            if is_block_available(row_num, col_num) and not game_over:
                if cur_player == 1:
                    fill_block(row_num, col_num, cur_player)
                    draw_player_symbol(row_num, col_num, cur_player)
                    game_over = check_winner(cur_player)
                    cur_player = 2
                else:
                    fill_block(row_num, col_num, cur_player)
                    draw_player_symbol(row_num, col_num, cur_player)
                    game_over = check_winner(cur_player)
                    cur_player = 1

    pygame.display.update()
    if game_over or is_board_full():
        time.sleep(1)
        restart()
        continue
