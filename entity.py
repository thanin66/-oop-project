import pygame,sys
from settings import *

class Player(pygame.sprite.Sprite) :
    ACTIONS = [ 'Idle', 'Attack', 'Move', 'Jump',]
    GRAVITY = 0.5

    def __init__(self,action = 'Idle', x = 0, y = 720 , hp = 300 ,max_hp = 300, dmg = 25, speed = 5, attack_de_cooldown = 30,frame = 0):
        super().__init__()
        self.action = action # ท่าทาง
        self.image =pygame.image.load(f'images/character/{self.action}.png')
        self.image = pygame.transform.scale(self.image, (self.image.get_width()//4 , self.image.get_height() //4))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.jump_power = -10  # แรงกระโดด
        self.gravity = 0.5  # แรงโน้มถ่วง
        self.x = x #ต่ำแหน่ง
        self.y = y #ต่ำแหน่ง
        self.hp = hp # เลือด
        self.max_hp = max_hp # maxเลือด
        self.dmg = dmg 
        self.speed = speed
        self.velocity_y = 0
        self.attack_de_cooldown = attack_de_cooldown
        self.attack_cooldown = 0
        self.frame = frame
        self.deltatime = 0
        self.direction = 1
        self.rate = 0

    def apply_gravity(self):
        # ในแต่ละเฟรม ความเร็วในแนวตั้งจะเพิ่มขึ้นตามค่าแรงโน้มถ่วง
        self.velocity_y += Player.GRAVITY
        self.y += self.velocity_y

    def jump(self, jump_strength):
        # เมื่อกระโดด ความเร็วในแนวตั้งจะถูกเซ็ตให้เป็นค่าของ jump_strength
        self.velocity_y = -jump_strength
    def jump(self):
        # กระโดดเฉพาะเมื่ออยู่บนพื้น
        if self.rect.bottom >= SCREEN_HEIGHT - 100:
            self.y = self.jump_power

    def update(self,):
        # อัพเดทตำแหน่งของผู้เล่น
        self.rect.x += self.x
        self.rect.y += self.y
        # ฟิสิกส์: ใช้แรงโน้มถ่วง
        self.y += self.gravity
        # ฟิสิกส์: เบรกหลังถ้าชนขอบหน้าต่าง
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > SCREEN_HEIGHT-100:
            self.rect.bottom = SCREEN_HEIGHT - 100


class Enemy(pygame.sprite.Sprite):
    def __init__(self, player, name, dmg, hp, max_hp, speed=2, attack_cooldown=80):
        super().__init__()
        self.player = player
        self.dmg = dmg
        self.hp = hp
        self.max_hp = max_hp
        self.name = name
        self.image = pygame.image.load(f'images/character/{self.name}01.png')  
        self.image = pygame.transform.scale(self.image, (self.image.get_width()//2, self.image.get_height()//2))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice([-300, SCREEN_WIDTH+300])
        self.rect.y = SCREEN_HEIGHT // 2
        self.speed = speed
        self.attack_cooldown = attack_cooldown


    def update(self):

        if self.rect.x < self.player.rect.x:
            self.rect.x += self.speed
        elif self.rect.x > self.player.rect.x:
            self.rect.x -= self.speed
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        if self.name == 'Wolf':
            self.speed = 4
            self.dmg = 1

        if self.name == 'Giant':

            self.speed = 1
            self.dmg = 40
        self.time = 1000
        if pygame.sprite.collide_rect(self.player, self) and self.attack_cooldown == 0:
            self.player.hp -= self.dmg
            print(self.dmg)
            self.attack_cooldown = 60
            self.time = 0
        if pygame.sprite.collide_rect(self.player, self):
            draw_text(f"-{self.dmg}", 665, 475,color=red)


class Weaphon():
    ()