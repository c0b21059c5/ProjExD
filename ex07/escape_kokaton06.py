import pygame as pg
from tkinter import messagebox as tkm
import sys
from random import randint
coin_0 = [0, 0, 0, 0, 0]
bomblist = [0]
class Screen:
    def __init__(self, title, wh, bgimg):
        pg.display.set_caption(title) #逃げろ！こうかとん
        self.sfc = pg.display.set_mode(wh) #(1600, 900)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg) #"fig/pg_bg.jpg"
        self.bgi_rct = self.bgi_sfc.get_rect()
        
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)

#クラス　こうかとん
class Bird:
    key_delta = {#上下左右
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img) # "fig/6.png"
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom) # 2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):#更新
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)


class Bomb:
    def __init__(self, color, radius, vxy, scr:Screen):
        self.sfc = pg.Surface((radius*2, radius*2)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (radius, radius), radius) # 爆弾用の円を描く
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):#更新
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)


class Coin:
    def __init__(self, scr:Screen):
        self.value = randint(1, 3) #コインの価値
        sfc = pg.image.load("fig/coin01.png")
        self.sfc = pg.transform.rotozoom(sfc, 0, self.value + 1)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(200, scr.rct.width-200)
        self.rct.centery = randint(200, scr.rct.height-200)
    
    def get_value(self):
        return self.value

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.blit(scr)

    def teleport(self, scr:Screen):
        self.rct.centerx = randint(200, scr.rct.width-200)
        self.rct.centery = randint(200, scr.rct.height-200)
        self.blit(scr)

#スコアクラス
class Score:
    def __init__(self, xy):
        self.score = 0
        self.sfc = pg.Surface((80, 80))
        self.sfc.set_colorkey((0, 0, 0))
        self.rct = self.sfc.get_rect()
        self.sysfont = pg.font.SysFont(None, 100)
        self.x, self.y = xy

    def up_score(self, value):
        self.score += value

    def get_score(self):
        return self.score

    def blit(self, scr:Screen):
        img = self.sysfont.render("SCORE:" + str(self.score), True, (255, 0, 0))
        scr.sfc.blit(img, (self.x, self.y))

#タイマークラス
class Timer:
    def __init__(self, xy):
        self.sfc = pg.Surface((80, 80))
        self.sfc.set_colorkey((0, 0, 0))
        self.rct = self.sfc.get_rect()
        self.sysfont = pg.font.SysFont(None, 100)
        self.x, self.y = xy

    def up_score(self, value):
        self.score += value

    def blit(self, scr:Screen):
        img = self.sysfont.render("TIME:" + str(int(pg.time.get_ticks()/1000)), True, (0, 0, 0))
        scr.sfc.blit(img, (self.x, self.y))


def check_bound(obj_rct, scr_rct):
    """
    obj_rct：こうかとんrct，または，爆弾rct
    scr_rct：スクリーンrct
    領域内：+1／領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate


def main():
    # 練習1
    scr = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")

    # 練習3
    kkt = Bird("fig/6.png", 2.0, (900, 400))

    # 練習5
    bomblist[0] = Bomb((255, 0, 0), 10, (+1, +1), scr)

    for i in range(len(coin_0)):
        coin_0[i] = Coin(scr)

    score = Score((30, 30))
    timer = Timer((1000, 30))

    clock = pg.time.Clock() # 練習1
    while True:
        scr.blit() # 練習2
    
        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return

        #それぞれ更新
        # 練習4
        kkt.update(scr)

        # 練習7
        for i in range(len(bomblist)):
            bomblist[i].update(scr)

        for i in range(len(coin_0)):
            coin_0[i].update(scr)

        score.blit(scr)
        timer.blit(scr)
         
        for i in range(10):
            if score.get_score() >= 15*i:#スコアが上がると15点ごとに
                if len(bomblist) <= i:#爆弾がi個以下なら
                    bomblist.append(Bomb((255, 0, 0), 10, (+1, +1), scr))#爆弾を1個増やす

        # 練習8
        for i in range(len(bomblist)):
            if kkt.rct.colliderect(bomblist[i].rct): # こうかとんrctが爆弾rctと重なったら
                tkm.showinfo("GAME OVER", "こうかとんはなくなった")#C0B21159追加
                return

        for i in range(len(coin_0)):# こうかとんrctがcoin[i]と重なったら
            if kkt.rct.colliderect(coin_0[i].rct):
                score.up_score(coin_0[i].get_value())
                coin_0[i].teleport(scr)
                
        pg.display.update() #練習2
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()