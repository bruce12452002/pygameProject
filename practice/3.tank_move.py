import pygame as pg

pg.init()
game_width = 800
game_height = 600
w = pg.display.set_mode((game_width, game_height))
pg.display.set_caption("鍵盤控制")

up = pg.image.load('../images/tank_up.png')
down = pg.image.load('../images/tank_down.png')
left = pg.image.load('../images/tank_left.png')
right = pg.image.load('../images/tank_right.png')

pg.display.flip()

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            exit()
