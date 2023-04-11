import pygame
import random

# 初期化
pygame.init()



# ゲーム画面の幅と高さ
WIDTH = 800
HEIGHT = 600

# 色の定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# ゲーム画面の作成x
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# タイトルの設定
pygame.display.set_caption("Dodger")
# 背景画像の読み込み
background_img = pygame.image.load("haikei.png")
background_rect = background_img.get_rect()
fail_count=0
fail_limit=3
# キャラクターのクラス
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 50)
        self.speed_x = 0
    def update(self):
        self.rect.x += self.speed_x
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def move_left(self):
        self.speed_x = -5

    def move_right(self):
        self.speed_x = 5

    def stop(self):
        self.speed_x = 0

# 障害物のクラス
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((random.randint(50, 100), 20))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -20)
        self.speed_y = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > HEIGHT:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -20)
            self.speed_y = random.randrange(1, 8)

# スプライトグループの作成
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
# キャラクターの作成
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
# 初期設定
bullet_limit = 3     # 球を打てる最大数
bullet_speed = 10    # 球の速度
bullet_cooldown = 75   # 球の発射のクールダウン時間（ミリ秒）
bullet_count = 0
last_shot_time = pygame.time.get_ticks() - bullet_cooldown  # 最後に球を打った時間
bullets = pygame.sprite.Group()  # 球を格納するグループ
# 障害物の作成
for i in range(10):
    obstacle = Obstacle()
    all_sprites.add(obstacle)
    obstacles.add(obstacle)
# 玉のクラス
class Bullet(pygame.sprite.Sprite):
    def __init__(self, *args, speed):
        super().__init__()
        self.image = pygame.Surface((10, 20))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = args
        self.speedy = -speed 

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

# ゲームループ
running = True
clock = pygame.time.Clock()
game_clock=0
while running:
    if game_clock==0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            # スタート画面の描画
        font = pygame.font.SysFont("Arial", 72)
        game_start_text = font.render("GAME START", True, (255, 255, 255))
        game_start_rect = game_start_text.get_rect()
        game_start_rect.center = (WIDTH / 2, HEIGHT / 2)
        screen.blit(game_start_text, game_start_rect)
        pygame.display.flip()
        # スペースキーが押されるまで待機
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game_clock=1
    # イベント処理
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_left()
                elif event.key == pygame.K_RIGHT:
                    player.move_right()
                elif event.key == pygame.K_SPACE:
                    current_time = pygame.time.get_ticks()
                    #クールダウン中でなく、球を打てる最大数に達していない場合、球を発射する
                    if current_time - last_shot_time >= bullet_cooldown and len(bullets) < bullet_limit:
                        bullet = Bullet(player.rect.centerx, player.rect.top, speed=bullet_speed)
                        bullet_count += 1
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                        last_shot_time = current_time
            elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and player.speed_x < 0:
                            player.stop()
                    elif event.key == pygame.K_RIGHT and player.speed_x > 0:
                            player.stop()
            # スプライトの更新
        all_sprites.update()
        all_sprites.draw(screen)
    
    # 衝突判定
    hits = pygame.sprite.groupcollide(bullets, obstacles, True, True)
    for hit in hits:
        obstacle = Obstacle()
        all_sprites.add(obstacle)
        obstacles.add(obstacle)
    hits = pygame.sprite.spritecollide(player, obstacles, True)
    if hits:
        fail_count += 1
        if fail_count >= 3:
            running = False

        else:
            # プレイヤーを初期位置に戻す
            player.rect.center = (WIDTH /2, HEIGHT - 50)
    # 背景画像の描画
    # 画面の更新
    pygame.display.flip()
    pygame.font.init()
    screen.blit(background_img, background_rect)
    font = pygame.font.Font("ipag.ttf", 20)  # 適当なフォントを選択し、36ポイントの大きさで作成
    bullet_count_text = font.render(f"弾数 {bullet_limit-len(bullets)}", True, (255, 255, 255))
    screen.blit(bullet_count_text, (10, 10))
    lives_text = font.render(f"ライフ: { fail_limit-fail_count}", True, (255, 255, 255))
    screen.blit(lives_text, (10, 50))  # 追加


    # フレームレートの設定
    clock.tick(60)
# ゲームオーバー画面の描画
font = pygame.font.SysFont("Arial", 72)
game_over_text = font.render("GAME OVER", True, (255, 255, 255))
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WIDTH / 2, HEIGHT / 2)
screen.blit(game_over_text, game_over_rect)
pygame.display.flip()

# 3秒待って終了する
pygame.time.wait(3000)
pygame.quit()
