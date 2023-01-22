import pygame as pg

pg.init()

game_width_height = [800, 600]
w = pg.display.set_mode(size=game_width_height)
# print(type(w))  # <class 'pygame.Surface'>
pg.display.set_caption("圖片")

image = pg.image.load('images/a.jpeg')  # 增加圖片
# w.fill((255, 255, 255))  # 背景圖，RGB，都 255 為白色，要在圖片之前加，否則加在最後，會覆蓋所有東西
w.blit(image, (0, 0))  # 將圖片放在視窗裡，blit(圖片, (左右距離, 上下距離))

width, height = image.get_size()  # 取得圖片寬高
w.blit(image, (game_width_height[0] - width, game_width_height[1] - height))  # 將圖片放在右下角
w.blit(image, (game_width_height[0] / 2 - width / 2, game_width_height[1] / 2 - height / 2))  # 將圖片置中

new_image = pg.transform.scale(image, (width / 2, height / 2))  # 更改圖片尺寸，scale(圖片, (左右大小，上下大小))，和原來比例不同會失真
w.blit(new_image, (game_width_height[0] - width / 2, 0))  # 將圖片放在右上角

# rotozoom(圖片, 旋轉角度, 縮放比例)
# 旋轉角度支援負數，正的頭往左；負的頭往右
# 縮放比例 > 1 為放大； < 1 > 0 為縮小； < 0 不顯示圖片
percent = 0.5
new_image2 = pg.transform.rotozoom(image, -90, percent)
w.blit(new_image2, (0, game_width_height[1] - height * percent))  # 將圖片放在左下角

# pg.display.flip()  # 刷新頁面，全部刷新，這樣視窗才會顯示
pg.display.update()  # 刷新頁面，部分刷新，傳什麼參數就只更新什麼；如果不傳參，效果等同 flip()；如果傳 None 則什麼都沒更新

open_game = True
while open_game:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            # exit()
            open_game = False
pg.quit()
