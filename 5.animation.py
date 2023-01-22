import pygame as pg
import time

pg.init()

game_width = 800
game_height = 600
w = pg.display.set_mode(size=[game_width, game_height])
background_color = (255, 255, 255)
w.fill(background_color)
pg.display.set_caption("動畫")

separator = 0.01  # 單位為秒，不加這個間隔會以 CPU 的時間為主，導致忽快忽慢


def old_ball():
    """
    每次改動就將原本的圖變成和背景色一樣，也就是將圖變不見
    """
    time.sleep(separator)
    pg.draw.circle(w, background_color, (400, h), 100)


def new_ball():
    time.sleep(separator)
    pg.draw.circle(w, (255, 0, 0), (400, h), 100)
    pg.display.flip()


h = 0
down = True
step = 10
while True:
    print(h)
    old_ball()  # 每次改動就將原本的圖變成和背景色一樣，也就是將圖變不見
    h += step

    if h >= game_height or h == 0:
        step *= -1

    new_ball()

    # if h <= game_height and down:
    #     old_ball()  # 每次改動就將原本的圖變成和背景色一樣，也就是將圖變不見
    #     h += step
    #     new_ball()
    #
    #     if h == game_height:
    #         down = False
    # elif h <= game_height and not down:
    #     old_ball()
    #     h -= step
    #     new_ball()
    #
    #     if h == 0:
    #         down = True

    for e in pg.event.get():
        if e.type == pg.QUIT:
            exit()
