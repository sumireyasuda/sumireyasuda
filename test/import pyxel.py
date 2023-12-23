import pyxel
from  random import randint
 
class App:
    def __init__(self):
        pyxel.init(160, 120)
 
        pyxel.load("mychara.pyxres")
 
        #STARTFLAG
        self.START = False
 
        #GAMEOVERフラグ
        self.GAMEOVER = False
 
        #スコア用変数
        self.score = 0
 
        #プレイヤー初期地位
        self.player_x = 20
        self.player_y = 60
        
        #重力系変数
        self.gravity = 2.5
        self.MAX_GRAVITY = self.gravity
        self.POWER = 0.25
 
        #爆弾の生成用
        self.enemy = [(i * 60, randint(0, 104)) for i in range(3,15)]
 
        #遠い雲
        self.far_cloud = [(10, 25), (70, 35), (120, 15), (44, 45), (67, 75), (110, 95)]
 
        #近い雲
        self.smily_cloud = [(20, 15), (40, 75), (110, 40)]
 
        #音再生
        pyxel.playm(0, loop=True)
 
        pyxel.run(self.update, self.draw)
 
    def update(self):
 
        #終了する
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
 
        
        #スペース押された場合
        if pyxel.btn(pyxel.KEY_SPACE) or pyxel.btn(pyxel.GAMEPAD_1_START):
            self.START = True
 
        if self.GAMEOVER and (pyxel.btn(pyxel.KEY_ENTER or pyxel.btn(pyxel.GAMEPAD_1_START))) :
            self.reset()
 
 
        if not self.START or self.GAMEOVER:
            return
 
        #プレイヤーの更新
        self.update_player()
 
        #爆弾の表示
        for i, v in enumerate(self.enemy):
            self.enemy[i] = self.update_enemy(*v)
 
        # スコア
        if not self.GAMEOVER:
            self.score += 1
 
 
    def draw(self):
        if self.GAMEOVER:
 
            MESSAGE =\
"""
     GAMEOVER
 
PUSH ENTER RESTART
"""
            pyxel.text(51, 40, MESSAGE, 1)
            pyxel.text(50, 40, MESSAGE, 7)
            return
 
        #背景表示
        pyxel.blt(0, 0, 2, 0, 0, 160, 120, 0)
 
        #雲の表示(遠い)
        offset = (pyxel.frame_count // 8) % 160
        for i in range(2):
            for x, y in self.far_cloud:
                pyxel.blt(x + i * 160 - offset, y, 0, 32, 32, 32, 16, 0)
 
        #キャラクタ表示
        if not self.GAMEOVER:
            pyxel.blt(self.player_x, self.player_y, 0, 16, 0, 16, 16, 0)
 
        # 爆弾表示
        for x, y in self.enemy:
            pyxel.blt(x, y, 0, 32, 16, 16, 16, 0)
 
 
        #雲の表示(近く)
        offset = (pyxel.frame_count // 2) % 160
        for i in range(2):
            for x, y in self.smily_cloud:
                pyxel.blt(x + i * 160 - offset, y, 0, 0, 32, 32, 16, 0)
 
        #スコア表示
        s = "SCORE {:>4}".format(self.score)
        pyxel.text(5, 4, s, 1)
        pyxel.text(4, 4, s, 7)
 
        if not self.START:
            MESSAGE ="PUSH SPACE KEY"
            pyxel.text(61, 50, MESSAGE, 1)
            pyxel.text(60, 50, MESSAGE, 7)
            return
 
    #プレイヤー更新関数
    def update_player(self):
 
        if pyxel.btn(pyxel.KEY_SPACE) or pyxel.btn(pyxel.GAMEPAD_1_A):
            if self.gravity > -self.MAX_GRAVITY:
                self.gravity = self.gravity - self.POWER
        else:
            if self.gravity < self.MAX_GRAVITY:
                self.gravity = self.gravity + self.POWER
 
        self.player_y = self.player_y + self.gravity 
 
        if( 0 > self.player_y ):
            self.player_y = 0
 
        if( self.player_y > pyxel.height -16 ):
            self.player_y = pyxel.height - 16
 
 
    #爆弾更新
    def update_enemy(self, x, y):
        if abs(x - self.player_x) < 12 and abs(y - self.player_y) < 12:
            self.GAMEOVER = True
            pyxel.blt(x, y, 0, 48, 16, 16, 16, 0)
            pyxel.blt(self.player_x, self.player_y, 0, 48, 0, 16, 16, 0)
            
            pyxel.stop()
        x -= 2
 
        if x < -40:
            x += 240
            y = randint(0, 104)
 
        return (x, y)
 
    def reset(self):
        #STARTFLAG
        self.START = True
 
        #GAMEOVERフラグ
        self.GAMEOVER = False
 
        #スコア用変数
        self.score = 0
 
        #プレイヤー初期地位
        self.player_x = 20
        self.player_y = 60
        
        #重力系変数
        self.gravity = 2.5
        self.MAX_GRAVITY = self.gravity
        self.POWER = 0.25
 
        #爆弾の生成用
        self.enemy = [(i * 60, randint(0, 104)) for i in range(3,15)]
 
        #遠い雲
        self.far_cloud = [(10, 25), (70, 35), (120, 15), (44, 45), (67, 75), (110, 95)]
 
        #近い雲
        self.smily_cloud = [(20, 15), (40, 75), (110, 40)]
 
        #音再生
        pyxel.playm(0, loop=True)
 
App()