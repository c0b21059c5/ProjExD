import pygame as pg
import sys
from random import randint

def check_bound(obj_rct, scr_rct):
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate


def main():
    # 練習1
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("fig/pg_bg.jpg") #背景画像の設定
    bg_rct = bg_sfc.get_rect()

    gameover_sfc = pg.image.load("fig/gameover.jpg") #ゲームオーバー画像の設定
    gameover_rct = gameover_sfc.get_rect()

    gameclear_sfc = pg.image.load("fig/gameclear.png") #ゲームクリア画像の設定
    gameclear_rct = gameclear_sfc.get_rect()

    # 練習3
    tori_sfc = pg.image.load("fig/6.png") #こうかとん画像の設定
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    # 爆弾1
    bomb_sfc = pg.Surface((20, 20)) # 空のSurface
    bomb_sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10) # 円を描く
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = randint(0, scrn_rct.width)
    bomb_rct.centery = randint(0, scrn_rct.height)
    vx, vy = +1, +1

    #爆弾2
    bomb2_sfc = pg.Surface((20, 20)) # 空のSurface
    bomb2_sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
    pg.draw.circle(bomb2_sfc, (255 , 0, 255), (10, 10), 10) # 円を描く
    bomb2_rct = bomb2_sfc.get_rect()
    bomb2_rct.centerx = randint(0, scrn_rct.width)
    bomb2_rct.centery = randint(0, scrn_rct.height)
    # 練習6
    vx2, vy2 = +1, +1

    clock = pg.time.Clock() # 練習1
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) # 練習2
        
        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return

        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]:    tori_rct.centery -= 1
        if key_states[pg.K_DOWN]:  tori_rct.centery += 1
        if key_states[pg.K_LEFT]:  tori_rct.centerx -= 1
        if key_states[pg.K_RIGHT]: tori_rct.centerx += 1
        yoko, tate = check_bound(tori_rct, scrn_rct)
        if yoko == -1:
            if key_states[pg.K_LEFT]: 
                tori_rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                tori_rct.centerx -= 1
        if tate == -1:
            if key_states[pg.K_UP]: 
                tori_rct.centery += 1
            if key_states[pg.K_DOWN]:
                tori_rct.centery -= 1            
        scrn_sfc.blit(tori_sfc, tori_rct) # 練習3

        # 練習7 
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate
        if vx > 0:
            vx += 0.001 #爆弾の加速
        if vx < 0:
            vx -= 0.001
        if vy > 0:
            vy += 0.001
        if vy < 0:
            vy -= 0.001
        bomb_rct.move_ip(vx, vy) # 練習6
        scrn_sfc.blit(bomb_sfc, bomb_rct) # 練習5

        yoko, tate = check_bound(bomb2_rct, scrn_rct)
        vx2 *= yoko
        vy2 *= tate
        if vx2 > 0:
            vx2 += 0.001
        if vx2 < 0:
            vx2 -= 0.001
        if vy2 > 0:
            vy2 += 0.001
        if vy2 < 0:
            vy2 -= 0.001
        bomb2_rct.move_ip(vx2, vy2) # 練習6
        scrn_sfc.blit(bomb2_sfc, bomb2_rct) # 練習5

        # 練習8
        if tori_rct.colliderect(bomb_rct): # こうかとんrctが爆弾rctと重なったら
            scrn_sfc.blit(gameover_sfc, gameover_rct) #ゲームオーバー画像の表示
            pg.display.update()
            clock.tick(0.2)
            return
        
        if tori_rct.colliderect(bomb2_rct): # こうかとんrctが爆弾rctと重なったら
            scrn_sfc.blit(gameover_sfc, gameover_rct) #ゲームオーバー画像の表示
            pg.display.update()
            clock.tick(0.2)
            return
        time = pg.time.get_ticks()/1000
        if time > 30:
            scrn_sfc.blit(gameclear_sfc, gameclear_rct) #ゲームクリアー画像の表示
            pg.display.update()
            clock.tick(0.2)
            return
        pg.display.update() #練習2
        clock.tick(1000)

if __name__ == "__main__":
    pg.init() # 初期化
    main() # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()
