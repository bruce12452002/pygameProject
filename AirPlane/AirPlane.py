import math
import random

import pygame as pg

pg.init()
WIDTH = 800
HEIGHT = 600
w = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("打飛機")
pg.display.set_icon(pg.image.load("../images/airplane.png"))
PLAYER_STEP = 50
score = 0  # 玩家分數
# game_over = False

# 背景圖
background_picture = pg.transform.scale(pg.image.load("background.jpeg"), (WIDTH, HEIGHT))

# 背景音樂
pg.mixer.music.load("../music/bacteria.mp3")
pg.mixer.music.play(-1)

# 音效
bomb = pg.mixer.Sound("../sound/bomb.mp3")  # 敵人死掉的爆炸聲
ju = pg.mixer.Sound("../sound/laser.mp3")  # 子彈發出的音效

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


def show_score():
    font = pg.font.SysFont("applesdgothicneo", 45)
    text = font.render(f"score：{score}", True, (0, 255, 0))
    w.blit(text, (0, 0))


class Bullet:
    def __init__(self):
        self.img = pg.transform.rotozoom(pg.image.load("../images/bullet.png"), 0, 0.2)
        self.x = airplane_pos_x + airplane_width // 2 - self.img.get_width() // 2
        self.y = airplane_pos_y + 10
        self.step = 10  # 子彈速度

    def hit(self):
        global score
        for m in monsters:
            if distance(self.x, self.y, m.x, m.y) < 30:
                bomb.play()
                remove_bullet(self)
                m.reset()
                score += 1


bullets = []


class Monster:
    h = 20  # 初始化時，怪物比較下面，之後生成怪物就要高一點

    def __init__(self):
        self.img = random.sample([monster1, monster2, monster3, monster4, monster5, monster6, monster7, monster8], 1)[0]
        # self.height = self.img.get_height()
        self.x = random.randint(0, WIDTH - self.img.get_width())
        self.y = random.randint(0, HEIGHT // 3 + self.h)
        self.step = random.uniform(2, 3)

    def reset(self):
        self.x = random.randint(0, WIDTH - self.img.get_width())
        self.y = random.randint(0, HEIGHT // 3 - self.h)


monsters = []
for i in range(10):
    monsters.append(Monster())


def show_bullets():
    for b in bullets:
        w.blit(b.img, (b.x, b.y))
        b.hit()
        b.y -= b.step
        if b.y < 0:
            remove_bullet(b)


def remove_bullet(b: Bullet):
    for bs in bullets:
        if bs == b:
            bullets.remove(b)


def show_monster():
    global game_over
    for m in monsters:
        w.blit(m.img, (m.x, m.y))
        m.x += m.step

        if 0 > m.x or m.x > WIDTH - m.img.get_width():
            m.step *= -1
            m.y += 30
            if m.y + m.img.get_height() > HEIGHT - airplane_height:
                # game_over = True
                monsters.clear()  # 遊戲結束，清空怪物


def show_game_over():
    font = pg.font.SysFont("applesdgothicneo", 64)
    text = font.render("Game Over", True, (255, 0, 0))
    w.blit(text, (WIDTH // 3, HEIGHT // 3))


def distance(bullet_x, bullet_y, monster_x, monster_y):
    x = bullet_x - monster_x
    y = bullet_y - monster_y
    return math.sqrt(x ** 2 + y ** 2)


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
            elif e.key == pg.K_SPACE:
                bullets.append(Bullet())
                ju.play()

    w.blit(background_picture, (0, 0))
    show_monster()
    show_bullets()
    w.blit(airplane, (airplane_pos_x, airplane_pos_y))
    show_score()
    pg.display.update()
