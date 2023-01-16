import pygame as pg

pg.init()
game_width = 800
game_height = 600
w = pg.display.set_mode((game_width, game_height))
pg.display.set_caption("鍵盤控制")

image = pg.image.load('../images/airplane.png')
w.blit(image, (game_width / 2 - image.get_width() / 2, game_height - image.get_height()))

pg.display.flip()

while True:
    for e in pg.event.get():
        if e.type == pg.MOUSEMOTION:
            # todo 右和下會超過畫面，所以必需有以下設定
            # wi, h = e.pos
            # if wi >= game_width:
            #     wi = game_width - image.get_width()

            w.fill((0, 0, 0))
            w.blit(image, e.pos)
            pg.display.update()
        elif e.type == pg.QUIT:
            exit()
