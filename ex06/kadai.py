import pygame as pg
import sys
from random import randint

bomblist=[]

class Screen:
    def __init__(self, title, wh, bgimg):
        pg.display.set_caption(title) #逃げろ！こうかとん
        self.sfc = pg.display.set_mode(wh) #(1600, 900)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg) #"fig/pg_bg.jpg"
        self.bgi_rct = self.bgi_sfc.get_rect()
        
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img) # "fig/6.png"
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom) # 2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy # 900, 400

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
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

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)
    def set_bkd(self, vxy):
        self.vx, self.vy = vxy

class Esa:
    def __init__(self, color, radius, scr:Screen):
        self.sfc = pg.Surface((radius*2, radius*2)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (radius, radius), radius) # 爆弾用の円を描く
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
    
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)
        
    def update(self, scr:Screen):
        self.blit(scr)

class Move_Esa:
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
        
    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)

class Score:
    def __init__(self, x, y):
        self.sfc = pg.Surface((100, 100))
        self.sfc.set_colorkey((0, 0, 0))
        self.rct = self.sfc.get_rect()
        self.sysfont = pg.font.SysFont(None, 100)
        self.score = 0
        self.bom_num = 0
        (self.x, self.y) = (x, y)
    def blit(self, scr:Screen):
        img = self.sysfont.render("SCORE:"+str(self.score), True, (255, 0, 0))
        scr.sfc.blit(img, (self.x, self.y))
    def add_score(self, a):
        self.score += a
    def get_score(self):
        return self.score

class GameClear:
    def __init__(self, img):
        self.sfc = pg.image.load(img)
        self.rct = self.sfc.get_rect()
        
    def blit(self, scr:Screen):
        self.sfc.blit(scr)

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
    bomblist.append(Bomb((255, 0, 0), 10, (+1, +1), scr))

    esa = Esa((0, 255, 0), 10, scr)

    move_esa = Move_Esa((0, 0, 255), 10, (+2, +2),  scr)

    score = Score(10, 10)

    clock = pg.time.Clock() # 練習1
    while True:
        scr.blit() # 練習2
        score.blit(scr)
        
        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return

        # 練習4
        kkt.update(scr)

        # 練習7
        for i in range(len(bomblist)):
            bomblist[i].update(scr)

        esa.update(scr)

        move_esa.update(scr)

        if kkt.rct.colliderect(esa.rct):
            score.add_score(1)
            esa = Esa((0, 255, 0), 10, scr)

        if kkt.rct.colliderect(move_esa.rct):
            score.add_score(3)
            move_esa = Move_Esa((0, 0, 255), 10, (+2, +2),  scr)

        # 練習8
        for i in range(len(bomblist)):
            if kkt.rct.colliderect(bomblist[i].rct): # こうかとんrctが爆弾rctと重なったら
                print(score)
                return
         
        for i in range(10):
            if score.get_score() >= 10*i:    
                if len(bomblist) == i:
                    bomblist.append(Bomb((255, 0, 0), 10, (+1, +1), scr))

        if score.get_score() >= 100:
            gameclear=GameClear("fig/gameclear.png")
            gameclear.blit(scr)

        pg.display.update() #練習2
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()