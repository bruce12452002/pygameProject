import pygame as pg

pg.init()
game_width = 800
game_height = 600
w = pg.display.set_mode((game_width, game_height))
pg.display.set_caption("自訂按鈕")
font = pg.font.SysFont("Impact", 25)

rect_width_point = 20
ok_rect_height_point = 200
cancel_rect_height_point = 400
rect_width = 100
rect_height = 50
ok_color = (0, 255, 0)
cancel_color = (0, 0, 255)

# 長方形設定
pg.draw.rect(w, ok_color, (rect_width_point, ok_rect_height_point, rect_width, rect_height))
pg.draw.rect(w, cancel_color, (rect_width_point, cancel_rect_height_point, rect_width, rect_height))

# 文字設定
text_color = (255, 255, 255)
ok = font.render("OK", True, text_color)
cancel = font.render("Cancel", True, text_color)


def display_ok():
    # 將文字放在圖的中間
    w.blit(ok, (
        rect_width_point + rect_width / 2 - ok.get_width() / 2,
        ok_rect_height_point + rect_height / 2 - ok.get_height() / 2))


def display_cancel():
    # 將文字放在圖的中間
    w.blit(cancel, (rect_width_point + rect_width / 2 - cancel.get_width() / 2,
                    cancel_rect_height_point + rect_height / 2 - cancel.get_height() / 2))


display_ok()
display_cancel()

pg.display.update()


def is_rect_width_scope():
    return rect_width_point <= wi <= rect_width_point + rect_width


while True:
    for e in pg.event.get():
        if e.type == pg.MOUSEBUTTONUP:
            wi, h = e.pos

            # 按下後拖曳到非按鈕區在放開，不會產生效果，所以將 if 註解了
            # if is_rect_width_scope() and \
            #         ok_rect_height_point <= h <= ok_rect_height_point + rect_height:
            pg.draw.rect(w, ok_color, (rect_width_point, ok_rect_height_point, rect_width, rect_height))
            display_ok()

            # pg.display.flip()

            # Cancel 按鈕範圍
            # elif is_rect_width_scope() and \
            #         cancel_rect_height_point <= h <= cancel_rect_height_point + rect_height:
            pg.draw.rect(w, cancel_color, (rect_width_point, cancel_rect_height_point, rect_width, rect_height))
            display_cancel()
            pg.display.flip()

        elif e.type == pg.MOUSEBUTTONDOWN:
            wi, h = e.pos
            gray = (200, 200, 200)
            # OK 按鈕範圍
            if is_rect_width_scope() and \
                    ok_rect_height_point <= h <= ok_rect_height_point + rect_height:
                pg.draw.rect(w, gray, (rect_width_point, ok_rect_height_point, rect_width, rect_height))
                display_ok()
                pg.display.flip()

            # Cancel 按鈕範圍
            elif is_rect_width_scope() and \
                    cancel_rect_height_point <= h <= cancel_rect_height_point + rect_height:
                pg.draw.rect(w, gray, (rect_width_point, cancel_rect_height_point, rect_width, rect_height))
                display_cancel()
                pg.display.flip()
        elif e.type == pg.QUIT:
            exit()
