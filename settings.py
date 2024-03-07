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
font = pygame.font.Font(None, 36)


#กำหนดขนาดปุ่ม
button_width = 200
button_height = 50

#เคลี่ยนที่
scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1


