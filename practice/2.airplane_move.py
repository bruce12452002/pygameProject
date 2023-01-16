import pygame as pg

pg.init()
game_width = 800
game_height = 600
w = pg.display.set_mode((game_width, game_height))
pg.display.set_caption("滑鼠控制")

image = pg.image.load('../images/airplane.png')
w.blit(image, (game_width / 2 - image.get_width() / 2, game_height - image.get_height()))

pg.display.flip()

while True:
    for e in pg.event.get():
        if e.type == pg.MOUSEMOTION:
            wi, h = e.pos

            # 圖片是抓左上坐標，所以右邊和下面飛機會消失
            # 這裡使得飛機一定會在螢幕內
            if wi + image.get_width() >= game_width:
                wi = game_width - image.get_width()

            if h + image.get_height() >= game_height:
                h = game_height - image.get_height()

            w.fill((0, 0, 0))
            w.blit(image, (wi, h))
            pg.display.update()
        elif e.type == pg.QUIT:
            exit()
