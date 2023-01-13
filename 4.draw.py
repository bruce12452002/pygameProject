import pygame as pg
import math

pg.init()

game_width_height = (800, 600)
w = pg.display.set_mode(size=game_width_height)
pg.display.set_caption("畫圖")

# line(畫在哪, 顏色, 起點, 終點)，給兩個點成為一條線
pg.draw.line(surface=w, color=(0, 255, 0), start_pos=(0, 10), end_pos=(50, 10))  # 橫線
pg.draw.line(surface=w, color=(255, 0, 0), start_pos=(10, 10), end_pos=(10, 60))  # 直線
pg.draw.line(surface=w, color=(0, 0, 255), start_pos=(0, 10), end_pos=(50, 60))  # 斜線

# 給好幾個點，從第一個點連第二個點，再連第三個點，依此類推
# lines(畫在哪, 顏色, 是否最後一個點連到第一個點, 線寬，預設為1)
points = [(100, 150), (250, 200), (30, 35), (80, 120)]
pg.draw.lines(w, (50, 100, 150), False, points, 8)

# circle(畫在哪, 顏色, 圓心坐標, 半徑長, 線寬，預設是0)
pg.draw.circle(w, (255, 0, 0), (100, 200), 50, 100)  # 線寬 0 為實心圓，線寬 > 0 為空心圓，< 0 看不到圓

# rect(畫在哪, 顏色, 範圍(左上角坐標寬高「兩個數字」,寬長,高長), 線寬，預設是0)
pg.draw.rect(w, (0, 255, 0), (0, 100, 100, 200), 1)  # 長方形

# ellipse(畫在哪, 顏色, rect, 線寬，預設是0)，和長方形用法相同，只不過幫我們變成楕圓
pg.draw.ellipse(w, (0, 255, 255), (0, 100, 100, 200), 1)  # 橢圓形

# arc(畫在哪, 顏色, rect, 開始弧度, 結束弧度, 線寬，預設是1), 弧度為 0~2pi
# pg.draw.arc(w, (255, 255, 255), (0, 100, 100, 200), 0, math.pi / 2, 5)
# pg.draw.arc(w, (255, 255, 255), (0, 100, 100, 200), 0, math.pi, 5)
# pg.draw.arc(w, (255, 255, 255), (0, 100, 100, 200), 0, math.pi * 1.5, 5)
pg.draw.arc(w, (255, 255, 255), (0, 100, 100, 200), 0, math.pi * 2, 5)


pg.display.flip()

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            exit()
