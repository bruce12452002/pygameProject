import pygame as pg

pg.init()

game_width_height = [800, 600]
w = pg.display.set_mode(size=game_width_height)
pg.display.set_caption("文字")

# Font(路徑, 大小)
font = pg.font.SysFont("Herculanum", 25, bold=False, italic=True)  # Impact
# font = pg.font.Font("xxx.ttf", 25)

# render(文字, 是否平滑, 顏色, 背景色（預色透明）)
text = font.render("Hello! Everybody", True, (0, 255, 0))
width, height = text.get_size()  # 取得文字寬高
# print(width, height)
w.blit(text, (game_width_height[0] / 2 - width / 2, game_width_height[1] / 2 - height / 2))  # 文字置中

text2 = pg.transform.scale(text, (width * 2, height * 2))
w.blit(text2, (0, game_width_height[1] - height * 2))  # 文字左下

text3 = pg.transform.rotozoom(text, 45, 1.5)
w.blit(text3, (game_width_height[0] - width * 1.5, 0))

pg.display.flip()

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            exit()
