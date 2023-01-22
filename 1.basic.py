import pygame as pg

# pip install pygame
# 如果報錯： pip install pygame --pre

pg.init()

game_width_height = [800, 600]
'''　flags 參數：
pg.FULLSCREEN
pg.RESIZABLE
pg.NOFRAME：沒有顯示放大、縮小、關閉
'''
w = pg.display.set_mode(size=game_width_height, flags=pg.RESIZABLE)
# print(type(w))  # <class 'pygame.Surface'>
pg.display.set_caption("我的標題")

open_game = True
while open_game:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            # exit()
            open_game = False
pg.quit()
