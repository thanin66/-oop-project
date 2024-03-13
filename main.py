import pygame,sys
from settings import *


floor_img = pygame.image.load('images/Background/floor_1.png').convert_alpha()
mountain_img = pygame.image.load('images/Background/mountain_1.png').convert_alpha()
sky_img = pygame.image.load('images/Background/sky_1.png').convert_alpha()

pine1_img = ()
pine2_img = ()
print(sky_img.get_width(),mountain_img.get_width())
def draw_bg():
    screen.fill(black)
    width = sky_img.get_width()
    for x in range(11):
        screen.blit(sky_img, ((x * width) - scroll * 0.5, 0))
        screen.blit(mountain_img, ((x * width) - scroll * 0.6, 0))
        screen.blit(floor_img, ((x * width) - scroll, 0))
    for y in range(1, 11):
        screen.blit(sky_img, ((-y * width) - scroll * 0.5, 0))
        screen.blit(mountain_img, ((-y * width) - scroll * 0.6, 0))
        screen.blit(floor_img, ((-y * width) - scroll, 0))

class Menu():
    def mode_game(screen):
        global back_button_rect, easy_button_rect, hard_button_rect,mode
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if back_button_rect.collidepoint(mouse_pos):
                        Menu.main_menu(screen)
                    elif easy_button_rect.collidepoint(mouse_pos):
                        mode = [10, 100, 100]
                        main = Main()
                        main.run()
                    elif hard_button_rect.collidepoint(mouse_pos):
                        mode = [20, 200, 200]
                        main = Main()
                        main.run()
            screen.blit(bg, (0, 0))

            back_button_rect = pygame.Rect(10, 40, button_width, button_height)
            draw_button(screen, back_button_rect.x, back_button_rect.y, button_width, button_height, "Back", gray)

            easy_button_rect = pygame.Rect(360, 300, button_width, button_height)
            draw_button(screen, easy_button_rect.x, easy_button_rect.y, button_width, button_height, "easy", green)

            hard_button_rect = pygame.Rect(700, 300, button_width, button_height)
            draw_button(screen, hard_button_rect.x, hard_button_rect.y, button_width, button_height, "hard", red)

            pygame.display.flip()

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
                        Menu.mode_game(screen)
                    elif setting_button_rect.collidepoint(mouse_pos):
                        Menu.setting_menu(screen)
                    elif quit_button_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()

            screen.blit(bg, (0, 0))

            start_button_rect = pygame.Rect(540, 200, button_width, button_height)
            draw_button(screen, start_button_rect.x, start_button_rect.y, button_width, button_height, "Start", gray)

            setting_button_rect = pygame.Rect(540, 300, button_width, button_height)
            draw_button(screen, setting_button_rect.x, setting_button_rect.y, button_width, button_height, "Setting", gray)

            quit_button_rect = pygame.Rect(540, 400, button_width, button_height)
            draw_button(screen, quit_button_rect.x, quit_button_rect.y, button_width, button_height, "Quit", gray)

            pygame.display.flip()
    def over_menu(screen):
        global start_button_rect, setting_button_rect, quit_button_rect
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if again_button.collidepoint(mouse_pos):
                        Menu.mode_game(screen)
                    elif setting_button_rect.collidepoint(mouse_pos):
                        Menu.setting_menu(screen)
                    elif back_button_rect.collidepoint(mouse_pos):
                        Menu.main_menu(screen)
                    elif quit_button_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()

            screen.blit(bg, (0, 0))

            back_button_rect = pygame.Rect(10, 40, button_width, button_height)
            draw_button(screen, back_button_rect.x, back_button_rect.y, button_width, button_height, "Back", gray)


            again_button = pygame.Rect(540, 200, button_width, button_height)
            draw_button(screen, again_button.x, again_button.y, button_width, button_height, "play again", gray)

            setting_button_rect = pygame.Rect(540, 300, button_width, button_height)
            draw_button(screen, setting_button_rect.x, setting_button_rect.y, button_width, button_height, "Setting", gray)

            quit_button_rect = pygame.Rect(540, 400, button_width, button_height)
            draw_button(screen, quit_button_rect.x, quit_button_rect.y, button_width, button_height, "Quit", gray)

            pygame.display.flip()
    def setting_menu(screen):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if back_button_rect.collidepoint(mouse_pos):
                        Menu.main_menu(screen)
                    elif fullscreen_button_rect.collidepoint(mouse_pos):
                        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)

                    elif window_button_rect.collidepoint(mouse_pos):
                        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                        return

            screen.blit(bg, (0, 0))

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
                        return  # Return to the main_game function
                    elif main_button_rect.collidepoint(mouse_pos):
                        Menu.main_menu(screen)
                    elif fullscreen_button_rect.collidepoint(mouse_pos):
                        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
                    elif window_button_rect.collidepoint(mouse_pos):
                        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

                        
            screen.blit(bg, (0, 0))

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
    GRAVITY = 0.5

    def __init__(self,action = 'player', x = 0, y = 720 , hp = 100 ,max_hp = 100, speed = 5,frame = 0):
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

        if self.name == 'Mage':
            self.speed = 5
            self.dmg = 5 + (mode[0] * 10/100)*(score_kill * 10/100)

        if self.name == 'Giant':

            self.speed = 1
            self.dmg = 40 + (mode[0] * 10/100)*(score_kill * 10/100)
        self.time = 1000
        if pygame.sprite.collide_rect(self.player, self) and self.attack_cooldown == 0:
            self.player.hp -= self.dmg
            print(self.dmg)
            self.attack_cooldown = 60
            self.time = 0
        if pygame.sprite.collide_rect(self.player, self):
            draw_text(f"-{self.dmg}", 665, 475,color=red)


class Weapon:
    def __init__(self, name, damage):
        self.name = name     
        self.damage = damage  
        self.image = pygame.image.load(f'images/character/Attack01.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
    def attack(self, x,y, enemies):
        global score_kill
        for enemy in enemies:
            if enemy.rect.collidepoint(x, y) :
                enemy.hp -= self.damage

            if enemy.hp < 1 :
                enemies.remove(enemy)
                score_kill +=1

        screen.blit(self.image, (x,y))
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


class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Your Game Title")

    def run(self):
        global scroll, scroll_left, scroll_right, enemy, weapon_right,weapon_left,score_kill

        player = Player()
        player_sprites = pygame.sprite.Group()


        enemy_sprites = pygame.sprite.Group()

        w_pos = player.rect.x
        magic = Weapon('slime',5)

        player_sprites.add(player)
        enemy_spawn_timer = 0
        # ghost = Enemy(player, 40, 40, 2)
        # Giant = Enemy(player, 40, 40, 2)
        # wolf = Enemy(player, 40, 40, 2)
        self.Name = ['Wolf', 'Mage','Giant']
        while True:
            draw_bg()

            if scroll_left == True:
                scroll -= 5
            if scroll_right == True:
                scroll += 5 

            if enemy_spawn_timer > 0:
                enemy_spawn_timer -= 1

            if enemy_spawn_timer == 0 and player.hp < player.max_hp - 5:
                draw_text(f"+5", 630, 475,color=green)
                player.hp += 5

            if enemy_spawn_timer == 0:
                name = random.choice(self.Name)
                if score_kill >= 0:
                    new_enemy = Enemy(player, name,mode[0] + (mode[0] * 10/100)*(score_kill * 10/100) ,mode[1] + (mode[1] * 50/100)*(score_kill * 10/100), mode[2] + (mode[2] * 50/100)*(score_kill * 10/100) , 3)
                enemy_sprites.add(new_enemy)
                if score_kill >= 0:
                    enemy_spawn_timer = 200
                if score_kill >= 20:
                    enemy_spawn_timer = 150
                if score_kill >= 30:
                    enemy_spawn_timer = 100

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        w_pos = player.rect.x
                        scroll_left = True
                        weapon_left = True
                        weapon_right = False
                    elif event.key == pygame.K_d:
                        w_pos = player.rect.x
                        scroll_right = True
                        weapon_right = True
                        weapon_left = False
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
            if player.hp <= 0 :
                Menu.over_menu(screen)    

            pause_button_rect = pygame.Rect(1100, 30, 50, button_height)
            draw_button(screen, pause_button_rect.x, pause_button_rect.y, 50, button_height, "ll", gray)
            
            enemy_sprites.update()

            # วาด
            enemy_sprites.draw(screen)
            player_sprites.update()

            # วาด
            player_sprites.draw(screen)

            if weapon_left == True:
                w_pos -= 10
            if weapon_right == True:
                w_pos += 10
            if abs(w_pos - player.rect.x) > 500:
                w_pos = player.rect.x

            
            magic.attack(w_pos, player.rect.y, enemy_sprites)

            for enemy in enemy_sprites:
                ered_hp_bar = pygame.Rect(enemy.rect.x , enemy.rect.y, 50,button_height)
                draw_button(screen, ered_hp_bar.x+80, ered_hp_bar.y-15 , 100, 20, "", red)
                ehp_bar = pygame.Rect(enemy.rect.x, enemy.rect.y, enemy.hp, 50)
                draw_button(screen, ehp_bar.x+80, ehp_bar.y-15 , ((enemy.hp/enemy.max_hp) * 100) , 20, "", green)
                        
            draw_text(f'scorekill = {score_kill}', 1000, 50)
            draw_text(f'HP ENEMY {int(mode[1] + (mode[1] * 50/100)*(score_kill * 10/100))} ', 400, 50)


            red_hp_bar = pygame.Rect(player.rect.x , player.rect.y, 50,button_height)
            draw_button(screen, red_hp_bar.x+15, red_hp_bar.y-15 , 100, 20, "", red)
            hp_bar = pygame.Rect(player.rect.x, player.rect.y, player.hp, 50)
            draw_button(screen, hp_bar.x+15, hp_bar.y-15 , ((player.hp/player.max_hp) * 100) , 20, f"HP{int(player.hp)}", green)

            pygame.display.flip()
            pygame.display.update()

            self.clock.tick(60)

if __name__ == '__main__':
    Menu.main_menu(screen)

