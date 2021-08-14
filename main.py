import pygame #載入模組 pygame

import random 

import os


FPS = 60

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
YELLOW = (255,255,0)

WIDTH = 500
HEIGHT = 600
#遊戲初始化 and 創建視窗
pygame.init()
screen = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("Survival!") #設定標題
clock = pygame.time.Clock()

#載入圖片
background = pygame.image.load(os.path.join("img" , "background.png")).convert()


class player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill((GREEN))
        self.rect = self.image.get_rect() #定位
        self.rect.centerx = WIDTH/2 
        self.rect.bottom = HEIGHT - 10
        self.speedx = 8

    def update(self):
        key_presses = pygame.key.get_pressed()
        if key_presses[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        if key_presses[pygame.K_LEFT]:
            self.rect.x -= self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        Bullet = bullet(self.rect.centerx , self.rect.top)
        all_sprite.add(Bullet)
        Bullets.add(Bullet)

class rock(pygame.sprite.Sprite):
    def __init__(self): 
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25,40))
        self.image.fill((RED))
        self.rect = self.image.get_rect() #定位
        self.rect.x = random.randrange(0,WIDTH - self.rect.width )
        self.rect.y = random.randrange(-100,-40 )
        self.speedy = random.randrange(2,10 )
        self.speedx = random.randrange(-3,3)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.rect = self.image.get_rect() #定位
            self.rect.x = random.randrange(0,WIDTH - self.rect.width )
            self.rect.y = random.randrange(-100,-40 )
            self.speedy = random.randrange(2,10 )
            self.speedx = random.randrange(-3,3)

class bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,20))
        self.image.fill((YELLOW))
        self.rect = self.image.get_rect() #定位
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10
    
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

all_sprite = pygame.sprite.Group()
rocks = pygame.sprite.Group()
Bullets = pygame.sprite.Group()
Player = player()
all_sprite.add(Player)
for i in range(8):   
    r = rock()
    all_sprite.add(r)
    rocks.add(r)
running = True
#遊戲迴圈
while running: #當遊戲運行時
    clock.tick(FPS) #在一秒鐘之內最多只能跑10次
    #取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #如果點紅色×，就關閉。
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Player.shoot()
    #更新遊戲
    all_sprite.update()
    hits = pygame.sprite.groupcollide(rocks , Bullets , True , True)
    for hit in hits:
        r = rock()
        all_sprite.add(r)
        rocks.add(r)

    hits = pygame.sprite.spritecollide(Player , rocks , False)
    if hits:
        running = False
    
    #畫面顯示
    screen.fill((BLACK))   
    screen.blit(background , (0,0))
    all_sprite.draw(screen)
    pygame.display.update() #將畫面更新為紅色

pygame.quit() 