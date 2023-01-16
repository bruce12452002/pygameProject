import pygame as pg

pg.init()

game_width = 800
game_height = 600
w = pg.display.set_mode(size=(game_width, game_height))
pg.display.set_caption("鍵盤事件")
font = pg.font.SysFont("Herculanum", 40, bold=False, italic=False)
word = 0
line = game_height / 2

while True:
    for e in pg.event.get():
        # e.key 取得按下哪個按鍵
        if e.type == pg.KEYUP:
            print("鍵盤跳起")
        elif e.type == pg.KEYDOWN:
            print("鍵盤按下", e.key)

            try:
                # chr() ord() 可將數字和字元轉換
                print("按下的按鍵=", chr(e.key))  # chr 只支援到 0x110000，也就是 1048576，2 ** 20
                text = font.render(chr(e.key), True, (0, 0, 255))

                # 一次打一個字
                # w.fill((0, 0, 0))  # 每次清空之前打的字
                # w.blit(text, (0, game_height / 2))

                # 打多個字，中間換行
                if word <= game_width / 2:
                    w.blit(text, (word, line))
                    word += 25
                else:
                    line += 30
                    word = 0
                    w.blit(text, (word, line))

                pg.display.flip()
            except ValueError as e:
                print(e)

        elif e.type == pg.QUIT:
            exit()
