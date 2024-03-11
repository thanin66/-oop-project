import pygame,sys,random
from pygame import mixer
# Initialize pygame font module
pygame.font.init()
mixer.init()

#ขนาดหน้าจอ
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

pygame.init()
pygame.display.set_caption("slime")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# กำหนดภาพพื้นหลัง
bg = pygame.image.load('images/background/bg_1.png').convert_alpha()

#สี
white = (255, 255, 255)
gray = (150, 150, 150) 
green = (0, 255, 0)
red =  (255, 0, 0)
magen = (255, 0, 255)
black = (0, 0, 0)

# กำหนด font
font = pygame.font.Font(None, 24)


#กำหนดขนาดปุ่ม
button_width = 200
button_height = 50



# ฟังก์ชันสำหรับสร้างปุ่ม
def draw_button(screen, x, y, width, height, text, color):
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(text_surface, text_rect)

# Function to draw text
def draw_text(text, x, y, font_size=30, color=black):
    font = pygame.font.Font(None, font_size)  # Default font and size
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

#เคลี่ยนที่
scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1

weapon_left = False
weapon_right = False