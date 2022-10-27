import pygame
from pygame.locals import *
import os 
import sys

class Block(pygame.sprite.Sprite):
    """壁について"""
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.rect=self.image.get_rect()
        self.rect.topleft=pos




class tekikyara(pygame.sprite.Sprite):
    speed=1 #移動速度
    animcycle=18 #アニメーション速度
    frame=0
    move_width=40 #横方向の移動可能範囲
    def __init__(self,pos,shots):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.rect=self.image.get_rect()
        self.rect.center=pos
        self.left=pos[0] #移動できる左端
        self.right=self.left+self.move_width #移動できる右端
        self.shots=shots #衝突判定用


    def update(self):
        #横移動について
        self.rect.move_ip(self.speed,0)
        if self.rect.center[0] < self.left or self.rect.center[0] > self.right:
            self.speed=-self.speed
        #キャラクターアニメーション
        self.frame+=1
        self.collision()#ミサイルとの衝突判定処理
    def collision(self):
        #みさいるのしょうとつはんてい
        for shot in self.shots :
            collide=self.rect.colliderect(shot.rect)
            if collide:#衝突するミサイルあり
                self.kill()
                

class shot(pygame.sprite.Sprite):

    def __init__(self,pos,player_x,blocks):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.rect=self.image.get_rect()
        self.rect.center=pos#中心座標を主人公に
        self.player_x=player_x#プレイヤーの向き
        self.blocks=blocks#衝突判定
        self.speed=9#ミサイルの移動距離

    def update(self):
        if self.player_x==1:
            self.rect.move_ip(self.speed,0)#右に移動
        elif self.player_x==0:
            self.rect.move_ip(-self.speed,0)#左に移動
        """衝突判定"""
        for block in self.blocks:
            collide=self.rect.colliderect(block.rect)
            if collide:#衝突するブロックあり
                self.kill()
                

class tengu(pygame.sprite.Sprite):
    MOVE_SPEED=2.0
    JUMP_SPEED=6.0
    GRAVITY=0.2
    MAX_JUMP_COUNT=2
    RELOAD_TIME=20
    def __init__(self,pos,blocks,enemys):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.image=self.right_image
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.enemys=enemys
        self.blocks=blocks
        self.reload_timer=0
        self.jump_count=0
        self.fpx=float(self.rect.x)
        self.fpy=float(self.rect.y)
        self.fpvx=0.0
        self.fpvy=0.0
        self.count=0

        self.on_floor=False

        self.player_x=1

    def update(self):
        pressed_keys=pygame.key.get_pressed()
        if pressed_keys[K_RIGHT]:
            self.image=self.right_image
            self.fpvx=self.MOVE_SPEED
            self.player_x=1
        elif pressed_keys[K_LEFT]:
            self.image=self.left_image
            self.fpvx=-self.MOVE_SPEED
            self.player_x=0
        else:
            self.fpvx=0.0
        if pressed_keys[K_SPACE]:
            if self.on_floor:
                self.fpvy=-self.JUMP_SPEED
                self.on_floor=False
                self.jump_count=1
            elif not self.prev_button and self.jump_count < self.MAX_JUMP_COUNT:
                self.fpvy=-self.JUMP_SPEED
                self.jump_count+=1
        if pressed_keys[K_c]:
            if self.reload_timer>self.RELOAD_TIME:
                    shot(self.rect.center,self.player_x,self.blocks)
                    self.sound.play()
                    self.reload_timer=0
            else:
                    self.reload_timer+=1
        if not self.on_floor:
            self.fpvy+=self.GRAVITY

        self.collision_x()
        self.collision_y()
        self.collision_e()

        self.rect.x=int(self.fpx)
        self.rect.y=int(self.fpy)
        self.prev_button=pressed_keys[K_SPACE]

    def collision_e(self):
        for enemy in self.enemys:
            collide=self.rect.colliderect(enemy.rect)
            if collide:
                self.image=self.down_image
                down_flag=1
                self.fpvy=-self.JUMP_SPEED
                
            else:
                down_flag=0
    def collision_x(self):
        width=self.rect.width
        height=self.rect.height
        newx=self.fpx+self.fpvx
        newrect=Rect(newx,self.fpy,width,height)
        for block in self.blocks:
            collide=newrect.colliderect(block.rect)
            if collide:
                if self.fpvx>0:
                    self.fpx=block.rect.left-width
                    self.fpvx=0
                elif self.fpvx<0:
                    self.fpx=block.rect.right
                    self.fpvx=0
                break
            else:
                self.fpx=newx
    def collision_y(self):
        width=self.rect.width
        height=self.rect.height
        newy=self.fpy+self.fpvy
        newrect=Rect(self.fpx,newy,width,height)
        for block in self.blocks:
            collide=newrect.colliderect(block.rect)
            if collide:
                if self.fpvy>0:
                    self.fpy=block.rect.top-height
                    self.fpvy=0
                    self.on_floor=True
                    self.jump_count=0
                elif self.fpvy<0:
                    self.fpy=block.rect.bottom
                    self.fpvy=0
                break
            else:
                self.fpy=newy
                self.on_floor=False
class map:
    GS=25
    def __init__(self,filename):
        # スプライトグループの登録
        self.all = pygame.sprite.RenderUpdates()
        self.blocks = pygame.sprite.Group()
        self.enemys = pygame.sprite.Group()  
        self.shots = pygame.sprite.Group()   
        tengu.containers = self.all
        Block.containers = self.all, self.blocks
        shot.containers = self.all, self.shots  
        tekikyara.containers = self.all, self.enemys 

        # プレイヤーの作成
        self.tengu = tengu((680,280), self.blocks, self.enemys)
        self.make_enemy(filename)

        # マップをロードしてマップ内スプライトの作成
        self.load(filename)

        # マップサーフェイスを作成
        self.surface = pygame.Surface((self.col*self.GS, self.row*self.GS)).convert()

    def draw(self):
        self.surface.fill((0,0,0))
        self.all.draw(self.surface)

    def update(self):
        """マップ内スプライトを更新"""
        self.all.update()

    def calc_offset(self):
        offsetx = self.tengu.rect.topleft[0] - SCR_RECT.width/2
        offsety = self.tengu.rect.topleft[1] - SCR_RECT.height/2
        return offsetx, offsety

    def load(self, filename):
        """マップをロードしてスプライトを作成"""
        map = []
        fp = open(filename, "r")
        for line in fp:
            line = line.rstrip()  
            map.append(list(line))
            self.row = len(map)
            self.col = len(map[0])
        self.width = self.col * self.GS
        self.height = self.row * self.GS
        fp.close()

        # マップからスプライトを作成
        for i in range(self.row):
            for j in range(self.col):
                if map[i][j] == 'B':
                    Block((j*self.GS, i*self.GS))  # ブロック

    def make_enemy(self, filename):
        """マップをロードしてスプライトを作成"""
        map = []
        fp = open(filename, "r")
        for line in fp:
            line = line.rstrip()  
            map.append(list(line))
            self.row = len(map)
            self.col = len(map[0])
        self.width = self.col * self.GS
        self.height = self.row * self.GS
        fp.close()

        # マップからスプライトを作成
        for i in range(self.row):
            for j in range(self.col):
                if map[i][j] == 'E':
                    tekikyara((j*self.GS, i*self.GS+14), self.shots)  # 敵
def load_image(filename, colorkey=None):
    filename = os.path.join(filename)
    try:
        image = pygame.transform.scale(pygame.image.load(filename),(20,20))
    except pygame.error as message:
        print("Cannot load image:", filename)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image
def load2_image(filename, colorkey=None):
    filename = os.path.join(filename)
    try:
        image = pygame.transform.scale(pygame.image.load(filename),(15,15))
    except pygame.error as message:
        print("Cannot load image:", filename)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image
def load3_image(filename, colorkey=None):
    filename = os.path.join(filename)
    try:
         image = pygame.transform.scale(pygame.image.load(filename),(25,25))
    except pygame.error as message:
        print("Cannot load image:", filename)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image
    
class tengu_game:
    def __init__(self):
        pygame.init()
        screen=pygame.display.set_mode(SCR_RECT.size)
        pygame.display.set_caption("マップスクロール")
        tengu.left_image= load_image("22026595.png")
        tengu.right_image= pygame.transform.flip(tengu.left_image,1,0)
        tengu.down_image= pygame.transform.flip(tengu.left_image,0,1)
        Block.image=load3_image("22077716.jpg",-1)
        tekikyara.image= load_image("22142087.png",-1)
        shot.image= load2_image("20202.jpg",-1)
        tengu.sound=pygame.mixer.Sound("se_gun_fire1.mp3")#サウンド効果音
        pygame.mixer.music.load("MusMus-CT-NV-47.mp3")#BGM
        pygame.mixer.music.play(-1)
        self.map1=map("gemu1.map")
        self.game_state=START
        clock=pygame.time.Clock()
        while True :
            clock.tick(70)
            self.update()
            self.draw(screen)
            pygame.display.update()
            self.key_handler()
    def update(self):
        if self.game_state==PLAY:
            self.map1.update()
    def draw(self,screen):
        
        if self.game_state == START:  # スタート画面
            # タイトルを描画
            title_font = pygame.font.SysFont(None, 80)
            title = title_font.render("INVADER GAME", False, (255,0,0))
            screen.blit(title, ((SCR_RECT.width-title.get_width())/2, 100))
            # PUSH STARTを描画
            push_font = pygame.font.Font("ipag.ttf",20,)
            push_space = push_font.render("TAB KEYを押して始めてください。すべての敵を倒したらd KEYで終了してください ",False , (255,255,255))
            screen.blit(push_space, ((SCR_RECT.width-push_space.get_width())/2, 300))
            # クレジットを描画
            credit_font = pygame.font.SysFont(None, 20)
            credit = credit_font.render(u"2008 http://pygame.skr.jp", False, (255,255,255))
            screen.blit(credit, ((SCR_RECT.width-credit.get_width())/2, 380))
        elif self.game_state == PLAY:
         self.map1.draw()
         offsetx,offsety=self.map1.calc_offset()
         if offsetx <0:
             offsetx=0
         elif offsetx >self.map1.width-SCR_RECT.width:
            offsetx =self.map1.width-SCR_RECT.width
         if offsety <0:
            offsety=0
         elif offsety>self.map1.height-SCR_RECT.height:
            offsety=self.map1.height-SCR_RECT.height
         screen.blit(self.map1.surface,(0,0),(offsetx,offsety,SCR_RECT.width,SCR_RECT.height))
        elif self.game_state == GAMEOVER:  # ゲームオーバー画面
            # GAME OVERを描画
            gameover_font = pygame.font.SysFont(None, 80)
            gameover = gameover_font.render("GAME END", False, (255,0,0))
            screen.blit(gameover, ((SCR_RECT.width-gameover.get_width())/2, 100))
 # PUSH STARTを描画
            push_font = pygame.font.Font("ipag.ttf", 40)
            push_space = push_font.render("ESCAPE KEYを押して終了してください", False, (255,255,255))
            screen.blit ( push_space, ((SCR_RECT.width-push_space.get_width())/2, 300)) 
    def key_handler(self):
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN and event.key==K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN and event.key==K_d:
                if self.game_state == PLAY:
                    self.game_state = GAMEOVER
            elif event.type == KEYDOWN and event.key == K_TAB:
                if self.game_state == START:  # スタート画面でスペースを押したとき
                    self.game_state = PLAY
                elif self.game_state == GAMEOVER:  # ゲームオーバー画面でスペースを押したとき
                    map.__init__()  # ゲームを初期化して再開
                    self.game_state = PLAY

START,PLAY,GAMEOVER=(0,1,2)

SCR_RECT=Rect(0,0,1140,500)
tengu_game()