import random

import pygame as pg

pg.init()
WIDTH = 800
HEIGHT = 600
w = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("打飛機")
pg.display.set_icon(pg.image.load("../images/airplane.png"))
PLAYER_STEP = 50
# MONSTER_STEP = 3

# 背景圖
background_picture = pg.transform.scale(pg.image.load("background.jpeg"), (WIDTH, HEIGHT))

# 畫飛機
airplane = pg.image.load("../images/airplane.png")
airplane_width, airplane_height = airplane.get_size()
airplane_pos_x = WIDTH // 2 - airplane_width // 2
airplane_pos_y = HEIGHT - airplane_height

# 怪物
zoom = 0.5
monster1 = pg.transform.rotozoom(pg.image.load("../images/m1.png"), 0, zoom)
monster2 = pg.transform.rotozoom(pg.image.load("../images/m2.png"), 0, zoom)
monster3 = pg.transform.rotozoom(pg.image.load("../images/m3.png"), 0, zoom)
monster4 = pg.transform.rotozoom(pg.image.load("../images/m4.png"), 0, zoom)
monster5 = pg.transform.rotozoom(pg.image.load("../images/m5.png"), 0, zoom)
monster6 = pg.transform.rotozoom(pg.image.load("../images/m6.png"), 0, zoom)
monster7 = pg.transform.rotozoom(pg.image.load("../images/m7.png"), 0, zoom)
monster8 = pg.transform.rotozoom(pg.image.load("../images/m8.png"), 0, zoom)


class Monster:
    def __init__(self):
        self.img = random.sample([monster1, monster2, monster3, monster4, monster5, monster6, monster7, monster8], 1)[0]
        self.x = random.randint(0, WIDTH - self.img.get_width())
        self.y = random.randint(0, HEIGHT // 3)
        self.step = random.uniform(2, 3)


monsters = []
for i in range(10):
    monsters.append(Monster())


def show_monster():
    for m in monsters:
        w.blit(m.img, (m.x, m.y))
        m.x += m.step

        if 0 > m.x or m.x > WIDTH - m.img.get_width():
            m.step *= -1
            m.y += 30


while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            exit()
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_LEFT:
                if 0 <= airplane_pos_x:
                    airplane_pos_x -= PLAYER_STEP
            elif e.key == pg.K_RIGHT:
                if airplane_pos_x <= WIDTH - airplane_width:
                    airplane_pos_x += PLAYER_STEP

    w.blit(background_picture, (0, 0))
    show_monster()
    w.blit(airplane, (airplane_pos_x, airplane_pos_y))

    pg.display.update()
