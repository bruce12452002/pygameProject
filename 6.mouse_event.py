import pygame as pg
import random

pg.init()

game_width = 800
game_height = 600
w = pg.display.set_mode(size=(game_width, game_height))
pg.display.set_caption("滑鼠事件")


def get_random_color():
    return random.randint(0, 255)


while True:
    for e in pg.event.get():
        # e.pos 取得坐標
        if e.type == pg.MOUSEBUTTONUP:
            print("滑鼠跳起")
        elif e.type == pg.MOUSEBUTTONDOWN:
            print("滑鼠按下", e.pos)
            pg.draw.circle(w, (255, 0, 0), e.pos, 50)
            pg.display.flip()
        elif e.type == pg.MOUSEWHEEL:
            print("滑鼠滾輪")
        elif e.type == pg.MOUSEMOTION:
            print("滑鼠移動")
            pg.draw.circle(w, (get_random_color(), get_random_color(), get_random_color()), e.pos, 50)
            pg.display.flip()
        elif e.type == pg.QUIT:
            exit()
