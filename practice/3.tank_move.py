import pygame as pg

pg.init()
game_width = 800
game_height = 600
w = pg.display.set_mode([game_width, game_height])
pg.display.set_caption("鍵盤控制")

up = pg.transform.scale(pg.image.load('../images/tank_up.png'), (80, 80))
down = pg.transform.scale(pg.image.load('../images/tank_down.png'), (80, 80))
left = pg.transform.scale(pg.image.load('../images/tank_left.png'), (80, 80))
right = pg.transform.scale(pg.image.load('../images/tank_right.png'), (80, 80))

tank_w, tank_h = game_width / 2 - up.get_width() / 2, game_height - up.get_height()
tank_pic = up  # 預設出現是往上的圖
w.blit(tank_pic, (tank_w, tank_h))

pg.display.flip()
is_move = False  # 是否按下指定的鍵
lr_move = 0  # 左右移動
ud_move = 0  # 上下移動
step = 1


def change_tank(lr, ud, pic):
    global is_move, lr_move, ud_move, tank_pic
    is_move = True
    lr_move = lr
    ud_move = ud
    tank_pic = pic


while True:
    if is_move:  # 寫在這才會按著不放還能繼續動
        w.fill((0, 0, 0))
        tank_w += lr_move
        tank_h += ud_move

        # 這裡使得戰車一定會在螢幕內
        if tank_w + tank_pic.get_width() >= game_width:
            tank_w = game_width - tank_pic.get_width()

        if tank_w <= 0:
            tank_w = 0

        if tank_h + tank_pic.get_height() >= game_height:
            tank_h = game_height - tank_pic.get_height()

        if tank_h <= 0:
            tank_h = 0

        w.blit(tank_pic, (tank_w, tank_h))
        pg.display.update()

    for e in pg.event.get():
        if e.type == pg.KEYDOWN:
            match e.key:
                # case 119 | 1073741906:  # w 或上鍵
                #     change_tank(0, step * -1, up)
                # case 115 | 1073741905:  # s 或下鍵
                #     change_tank(0, step, down)
                # case 97 | 1073741904:  # a 或左鍵
                #     change_tank(step * -1, 0, left)
                # case 100 | 1073741903:  # d 或右鍵
                #       change_tank(step, 0, right)

                case pg.K_w | pg.K_UP:  # w 或上鍵
                    change_tank(0, step * -1, up)
                case pg.K_s | pg.K_DOWN:  # s 或下鍵
                    change_tank(0, step, down)
                case pg.K_a | pg.K_LEFT:  # a 或左鍵
                    change_tank(step * -1, 0, left)
                case pg.K_d | pg.K_RIGHT:  # d 或右鍵
                    change_tank(step, 0, right)
        elif e.type == pg.KEYUP:
            is_move = False
        elif e.type == pg.QUIT:
            exit()
