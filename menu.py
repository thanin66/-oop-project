from settings import *
import main as Main_game
def draw_bg():
    screen.fill(green)
    width = bg.get_width()
    for x in range(4):
        screen.blit(bg,((x * width)-scroll, 0))
# ฟังก์ชันสำหรับสร้างปุ่ม
def draw_button(screen, x, y, width, height, text, color):
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(text_surface, text_rect)

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
                    main_menu(screen)
                elif easy_button_rect.collidepoint(mouse_pos):
                    print("easy Button Clicked")
                    Main_game
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
                    mode_game(screen)
                elif setting_button_rect.collidepoint(mouse_pos):
                    # ทำสิ่งที่ต้องการเมื่อคลิกที่ปุม setting
                    print("Setting Button Clicked")
                    setting_menu(screen)
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
                    main_menu(screen)
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
                    main_menu(screen)
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
