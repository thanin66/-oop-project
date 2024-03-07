import pygame,sys
from settings import *
from menu import *


sky_img = pygame.image.load('images/background/bg_1.png').convert_alpha()
width = sky_img.get_width()
for x in range(4):
    screen.blit(sky_img, ((x * width) - scroll, 0))

class Player(pygame.sprite.Sprite) :
    ACTIONS = [ 'Idle', 'Attack', 'Move', 'Jump',]
    GRAVITY = 0.5

    def __init__(self,action = 'Idle', x = 0, y = 720 , hp = 100 ,max_hp = 100, dmg = 25, speed = 5, attack_de_cooldown = 30,frame = 0):
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
    def __init__(self, player,Name , dmg, hp, max_hp, speed=2, attack_cooldown =80, *groups):
        super().__init__(*groups)
        self.player = player
        self.dmg = dmg
        self.hp = hp
        self.max_hp = max_hp
        self.Name = Name
        self.image = pygame.image.load(f'images/character/{self.Name}01.png')  
        self.image = pygame.transform.scale(self.image, (self.image.get_width()//2 , self.image.get_height() //2))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice([-300,SCREEN_WIDTH+300])
        self.rect.y = SCREEN_HEIGHT // 2
        self.speed = speed
        self.attack_cooldown = attack_cooldown  # เพิ่มตัวแปรคูลดาวน์การโจมตี
        

        
    def update(self):
        print(self.Name)
        if self.rect.x < self.player.rect.x:
            self.rect.x += self.speed
        elif self.rect.x > self.player.rect.x:
            self.rect.x -= self.speed
        if scroll_left == True:
            self.rect.x += 5
        if scroll_right == True:
            self.rect.x -= 5
        # ตรวจสอบคูลดาวน์การโจมตี
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        if self.Name == 'Wolf':
            self.speed = 4
            self.dmg = 1

                # ตรวจสอบการชนของ player กับ enemy
        if pygame.sprite.collide_rect(self.player, self) and self.attack_cooldown == 0:
            self.player.hp -= self.dmg  # ค่าความเสียหายจากการโจมตี
            self.attack_cooldown = 60  # รีเซ็ตคูลดาวน์หลังจากโจมตี 


pygame.init()
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
# สร้างรายการภาพพื้นหลังตามลำดับที่กำหนด
player = Player()
all_sprites.add(player)
# ghost = Enemy(player, 40, 40, 2)
# wolf = Enemy(player, 40, 40, 2)
# giant = Enemy(player, 40, 40, 2)
# wolf = Enemy(player, 40, 40, 2)
Name = 'Mage'
enemy_spawn_timer = 0  # เพิ่มตัวแปรสำหรับจับเวลาสำหรับการสุ่ม spawn enemy
score_kill = 0
hp = 0

width = sky_img.get_width()
for x in range(4):
    screen.blit(sky_img, ((x * width) - scroll, 0))

class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()


    def run(self):
        while True :
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        scroll_left = True
                    elif event.key == pygame.K_d:
                        scroll_right = True
                    elif event.key == pygame.K_r:
                        player.hp = 100
                    elif event.key == pygame.K_SPACE:
                        player.jump()
                    elif event.key == pygame.K_f and player.attack_cooldown == 30:
                        player.attack()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a and scroll_left == True:
                        scroll_left = False
                    elif event.key == pygame.K_d and scroll_right == True:
                        scroll_right = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if pause_button_rect.collidepoint(mouse_pos):
                        if game_setting_menu(screen):  # Check the return value
                            return  # Exit the main_game loop and return to the main_menu

            screen.blit(sky_img, (0 - scroll, 0))
            pause_button_rect = pygame.Rect(1100, 30, 50, button_height)
            draw_button(screen, pause_button_rect.x, pause_button_rect.y, 50, button_height, "ll", gray)
        
            pygame.display.update()




if __name__ == '__main__':
	main = Main()
	main.run() 

