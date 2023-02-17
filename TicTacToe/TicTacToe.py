import pygame as pg
import numpy as np

pg.init()

WH = 600  # 600 * 600，所有相關程式碼都要以這個為比例調整
w = pg.display.set_mode(size=(WH, WH))

pg.display.set_caption("井字遊戲")
BG_COLOR = (100, 100, 100)
w.fill(BG_COLOR)

PAD = 3  # 3*3，格子數
board = np.zeros((PAD, PAD))  # 產生 3*3 二維陣列
AVG_PAD = WH // 3  # 每一個格子的平均數
CIRCLE_COLOR = (255, 0, 0)
CROSS_COLOR = (0, 0, 255)
LINE_WIDTH = WH // 40
game_over = False
INIT_PLAYER = 2  # 初始化時，第一個是畫 X 或畫 O，1為 O；2為 X
player = INIT_PLAYER


def check_winner(p):
    for col in range(PAD):
        if board[0][col] == p and board[1][col] == p and board[2][col] == p:
            draw_vertical(col, p)
            return True

    for row in range(PAD):
        if board[row][0] == p and board[row][1] == p and board[row][2] == p:
            draw_horizontal(row, p)
            return True

    if board[0][2] == p and board[1][1] == p and board[2][0] == p:
        draw_asc_diagonal(p)
        return True

    if board[0][0] == p and board[1][1] == p and board[2][2] == p:
        draw_desc_diagnoal(p)
        return True

    return False


def draw_vertical(col, p):
    x = col * AVG_PAD + AVG_PAD // 2
    pg.draw.line(w, get_color(p), (x, LINE_WIDTH), (x, WH - LINE_WIDTH), LINE_WIDTH)
    turn_game_over()


def draw_horizontal(row, p):
    y = row * AVG_PAD + AVG_PAD // 2
    pg.draw.line(w, get_color(p), (LINE_WIDTH, y), (WH - LINE_WIDTH, y), LINE_WIDTH)
    turn_game_over()


def draw_asc_diagonal(p):
    pg.draw.line(w, get_color(p), (LINE_WIDTH, WH - LINE_WIDTH),
                 (WH - LINE_WIDTH, LINE_WIDTH), LINE_WIDTH)
    turn_game_over()


def draw_desc_diagnoal(p):
    pg.draw.line(w, get_color(p), (LINE_WIDTH, LINE_WIDTH),
                 (WH - LINE_WIDTH, WH - LINE_WIDTH), LINE_WIDTH)
    turn_game_over()


def turn_game_over():
    global game_over
    game_over = True


def restart():
    w.fill(BG_COLOR)
    draw_lines()

    global player, game_over
    player = INIT_PLAYER
    game_over = False

    for row in range(PAD):
        for col in range(PAD):
            board[row][col] = 0
    pg.display.flip()


def get_color(p):
    if p == 1:
        return CIRCLE_COLOR
    elif p == 2:
        return CROSS_COLOR


def draw_figures():
    for row in range(PAD):
        for col in range(PAD):
            if board[row][col] == 1:
                x = int(col * AVG_PAD + AVG_PAD // 2)  # 圓心坐標 x
                y = int(row * AVG_PAD + AVG_PAD // 2)  # 圓心坐標 y
                pg.draw.circle(w, CIRCLE_COLOR, (x, y), WH // 10, LINE_WIDTH)
            if board[row][col] == 2:
                space = WH // 12
                pg.draw.line(w, CROSS_COLOR, (col * AVG_PAD + space, row * AVG_PAD + AVG_PAD - space),
                             (col * AVG_PAD + AVG_PAD - space, row * AVG_PAD + space), LINE_WIDTH)
                pg.draw.line(w, CROSS_COLOR, (col * AVG_PAD + space, row * AVG_PAD + space),
                             (col * AVG_PAD + AVG_PAD - space, row * AVG_PAD + AVG_PAD - space), LINE_WIDTH)


def mark_square(row, col, p):
    board[row, col] = p


def available_square(row, col):
    return board[row][col] == 0


def is_board_full():
    for row in range(PAD):
        for col in range(PAD):
            if board[row][col] == 0:
                return False
    return True


# print(available_square(1, 1))
# mark_square(0, 0, 1)
# mark_square(1, 1, 2)
# print(available_square(1, 1))
# print(board)


def draw_lines():
    line_color = (0, 255, 0)
    line_width = 10
    pg.draw.line(surface=w, color=line_color, start_pos=(0, AVG_PAD), end_pos=(WH, AVG_PAD), width=line_width)
    pg.draw.line(surface=w, color=line_color, start_pos=(0, AVG_PAD * 2), end_pos=(WH, AVG_PAD * 2), width=line_width)
    pg.draw.line(surface=w, color=line_color, start_pos=(AVG_PAD, 0), end_pos=(AVG_PAD, WH), width=line_width)
    pg.draw.line(surface=w, color=line_color, start_pos=(AVG_PAD * 2, 0), end_pos=(AVG_PAD * 2, WH), width=line_width)


draw_lines()
pg.display.flip()

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            exit()
        elif e.type == pg.MOUSEBUTTONDOWN and not game_over:
            mouseX = e.pos[0]
            mouseY = e.pos[1]
            # print(mouseX, mouseY)
            clicked_col = int(mouseX // AVG_PAD)
            clicked_row = int(mouseY // AVG_PAD)
            # print(clicked_row, clicked_col)

            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, player)
                    check_winner(player)
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, player)
                    check_winner(player)
                    player = 1
                # print(board)
                draw_figures()
                pg.display.update()
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_r:
                restart()
