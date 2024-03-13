import pygame,sys
from settings import *


sky_img = pygame.image.load('images/background/bg_1.png').convert_alpha()
width = sky_img.get_width()
for x in range(4):
    screen.blit(sky_img, ((x * width) - scroll, 0))


class Menu():

    def mode_game(screen):
        global back_button_rect, easy_button_rect, hard_button_rect
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if back_button_rect.collidepoint(mouse_pos):
                        print("back")
                        Menu.main_menu(screen)
                    elif easy_button_rect.collidepoint(mouse_pos):
                        print("easy Button Clicked")
                        main = Main()
                        main.run()
                    elif hard_button_rect.collidepoint(mouse_pos):
                        print("hard Button Clicked")

            screen.blit(bg, (0, 0))

            back_button_rect = pygame.Rect(10, 40, button_width, button_height)
            draw_button(screen, back_button_rect.x, back_button_rect.y, button_width, button_height, "Back", gray)

            easy_button_rect = pygame.Rect(360, 300, button_width, button_height)
            draw_button(screen, easy_button_rect.x, easy_button_rect.y, button_width, button_height, "easy", green)

            hard_button_rect = pygame.Rect(700, 300, button_width, button_height)
            draw_button(screen, hard_button_rect.x, hard_button_rect.y, button_width, button_height, "hard", red)

            pygame.display.flip()

    # ฟังก์ชันสำหรับแสดงเมนูหลัก
    def main_menu(screen):
        global start_button_rect, setting_button_rect, quit_button_rect
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if start_button_rect.collidepoint(mouse_pos):
                        # ทำสิ่งที่ต้องการเมื่อคลิกที่ปุ่ม start
                        print("Start Button Clicked")
                        Menu.mode_game(screen)
                    elif setting_button_rect.collidepoint(mouse_pos):
                        # ทำสิ่งที่ต้องการเมื่อคลิกที่ปุม setting
                        print("Setting Button Clicked")
                        Menu.setting_menu(screen)
                    elif quit_button_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()

            screen.blit(bg, (0, 0))

            # สร้างปุ่ม start
            start_button_rect = pygame.Rect(540, 200, button_width, button_height)
            draw_button(screen, start_button_rect.x, start_button_rect.y, button_width, button_height, "Start", gray)

            # สร้างปุ่ม setting
            setting_button_rect = pygame.Rect(540, 300, button_width, button_height)
            draw_button(screen, setting_button_rect.x, setting_button_rect.y, button_width, button_height, "Setting", gray)

            # สร้างปุ่ม quit
            quit_button_rect = pygame.Rect(540, 400, button_width, button_height)
            draw_button(screen, quit_button_rect.x, quit_button_rect.y, button_width, button_height, "Quit", gray)

            pygame.display.flip()

    # ฟังก์ชันสำหรับแสดงเมนูตั้งค่า
    def setting_menu(screen):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if back_button_rect.collidepoint(mouse_pos):
                        print("back")
                        Menu.main_menu(screen)
                    elif fullscreen_button_rect.collidepoint(mouse_pos):
                        print('fullscreen')
                        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)

                    elif window_button_rect.collidepoint(mouse_pos):
                        print('fullscreen')
                        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                        return

            screen.blit(bg, (0, 0))

            # สร้างปุ่ม Back
            back_button_rect = pygame.Rect(540, 500, button_width, button_height)
            draw_button(screen, back_button_rect.x, back_button_rect.y, button_width, button_height, "Back", gray)

            fullscreen_button_rect = pygame.Rect(360, 200, button_width, button_height)
            draw_button(screen, fullscreen_button_rect.x, fullscreen_button_rect.y, button_width, button_height, "fullscreen", gray)

            window_button_rect = pygame.Rect(700, 200, button_width, button_height)
            draw_button(screen, window_button_rect.x, window_button_rect.y, button_width, button_height, "window", gray)

            pygame.display.flip()
    def game_setting_menu(screen):
        main_button_rect = pygame.Rect(0, 0, 0, 0)
        fullscreen_button_rect = pygame.Rect(0, 0, 0, 0)
        window_button_rect = pygame.Rect(0, 0, 0, 0)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if back_button_rect.collidepoint(mouse_pos):
                        print("back to game")
                        return  # Return to the main_game function
                    elif main_button_rect.collidepoint(mouse_pos):
                        print("to Main menu")
                        Menu.main_menu(screen)
                    elif fullscreen_button_rect.collidepoint(mouse_pos):
                        print('fullscreen')
                        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
                    elif window_button_rect.collidepoint(mouse_pos):
                        print('window')
                        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

                        
            screen.blit(bg, (0, 0))

            # สร้างปุ่ม Back
            back_button_rect = pygame.Rect(700, 500, button_width, button_height)
            draw_button(screen, back_button_rect.x, back_button_rect.y, button_width, button_height, "back to game", gray)

            main_button_rect = pygame.Rect(360, 500, button_width, button_height)
            draw_button(screen, main_button_rect.x, main_button_rect.y, button_width, button_height, "to Main menu", gray)

            fullscreen_button_rect = pygame.Rect(360, 200, button_width, button_height)
            draw_button(screen, fullscreen_button_rect.x, fullscreen_button_rect.y, button_width, button_height, "fullscreen", gray)

            window_button_rect = pygame.Rect(700, 200, button_width, button_height)
            draw_button(screen, window_button_rect.x, window_button_rect.y, button_width, button_height, "window", gray)

            pygame.display.flip()

class Player(pygame.sprite.Sprite) :
    ACTIONS = [ 'Idle', 'Attack', 'Move', 'Jump',]
    GRAVITY = 0.5

    def __init__(self,action = 'Idle', x = 0, y = 720 , hp = 300 ,max_hp = 300, speed = 5,frame = 0):
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
        self.speed = speed
        self.attack_cooldown = 0
        self.frame = frame
        self.deltatime = 0
        self.direction = 1
        self.rate = 0



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
    global scroll_left, scroll_right
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
        if scroll_left == True:
            self.rect.x += 5
        if scroll_right == True:
            self.rect.x -= 5
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


class Weapon:
    def __init__(self, name, damage, attack_speed):
        self.name = name                # ชื่อของอาวุธ
        self.damage = damage            # ความเสียหายที่สร้างให้กับศัตรู
        self.attack_speed = attack_speed  # ความเร็วในการโจมตี (ยิง/โจมตีต่อหนึ่งหน่วยเวลา)
        self.images = []                # รายการภาพของ animation
        self.current_frame = 0          # เฟรมปัจจุบันใน animation
        # โหลดและปรับขนาดรูปภาพของ animation
        for r in range(1, 5):  # มีภาพ 4 เฟรม จะเปลี่ยนตามความเหมาะสม
            image = pygame.image.load(f'images/character/Attack0{r}.png')
            image = pygame.transform.scale(image, (100, 100))  # ปรับขนาดเป็น 50x50 pixels
            self.images.append(image)

    def attack(self, player_x, player_y):
        
        # แสดงรูปภาพอาวุธที่ตำแหน่งของผู้เล่น
        screen.blit(self.images[self.current_frame], (player_x, player_y))
        # เลื่อนไปยังเฟรมถัดไปใน animation
        self.current_frame = (self.current_frame + 1) % len(self.images)

    def reload(self):
        # นับเวลาแสดงอาวุธใหม่ตามความเร็วในการโจมตี
        pass
#game currency
#shop
#trader
#coins
#items
#randon level item

#game model
            
#wall hp spike image
#fire hp skill exp image
#base image 
#auto defene image level dmg

slime = Weapon('slime',10,2)

class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Your Game Title")

    def run(self):
        global scroll, scroll_left, scroll_right

        player = Player()
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)
        enemy_spawn_timer = 0
        score_kill = 0
        # ghost = Enemy(player, 40, 40, 2)
        # Giant = Enemy(player, 40, 40, 2)
        # wolf = Enemy(player, 40, 40, 2)
        self.Name = ['Wolf', 'Mage','Giant']
        while True:
            dt = self.clock.tick() / 1000
            if scroll_left == True:
                scroll -= 5
            if scroll_right == True:
                scroll += 5 

            if enemy_spawn_timer > 0:
                enemy_spawn_timer -= 1

            if enemy_spawn_timer == 0:
                name = random.choice(self.Name)
                new_enemy = Enemy(player, name, 10, 40, 40, 2)
                all_sprites.add(new_enemy)
                enemy_spawn_timer = 100 


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
                        player.hp = player.max_hp
                    elif event.key == pygame.K_SPACE:
                        player.jump()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a and scroll_left == True:
                        scroll_left = False
                    elif event.key == pygame.K_d and scroll_right == True:
                        scroll_right = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if pause_button_rect.collidepoint(mouse_pos):
                        if Menu.game_setting_menu(screen):  # Check the return value
                            return  # Exit the main_game loop and return to the main_menu
                        

            screen.blit(sky_img, (0 - scroll, 0))


                # โค้ดอื่นๆ ที่ต้องการให้ทำงานร่วมกับเกม
            screen.blit(sky_img, (0 - scroll, 0))
            pause_button_rect = pygame.Rect(1100, 30, 50, button_height)
            draw_button(screen, pause_button_rect.x, pause_button_rect.y, 50, button_height, "ll", gray)
            
            all_sprites.update()

            # วาด
            all_sprites.draw(screen)

            slime.attack(player.rect.x - 125 ,player.rect.y)
            slime.attack(player.rect.x +150 ,player.rect.y)

            ered_hp_bar = pygame.Rect(player.rect.x , player.rect.y, 50,button_height)
            draw_button(screen, ered_hp_bar.x+15, ered_hp_bar.y-15 , 100, 20, "", red)
            ehp_bar = pygame.Rect(player.rect.x, player.rect.y, player.hp, 50)
            draw_button(screen, ehp_bar.x+15, ehp_bar.y-15 , ((hit.hp/player.max_hp) * 100) , 20, f"HP{player.hp}", green)

            red_hp_bar = pygame.Rect(player.rect.x , player.rect.y, 50,button_height)
            draw_button(screen, red_hp_bar.x+15, red_hp_bar.y-15 , 100, 20, "", red)
            hp_bar = pygame.Rect(player.rect.x, player.rect.y, player.hp, 50)
            draw_button(screen, hp_bar.x+15, hp_bar.y-15 , ((player.hp/player.max_hp) * 100) , 20, f"HP{player.hp}", green)

            pygame.display.flip()


            # จำกัดเฟรมเรต
            self.clock.tick(60)

if __name__ == '__main__':
    Menu.main_menu(screen)

