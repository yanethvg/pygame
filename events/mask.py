import sys
import math
import pygame
import os

pygame.init()

width = 600
height = 600

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Mascara')

# RGB
white = (255, 255, 255)
red = (134, 45, 83)
green = (52, 157, 89)
blue = (59, 87, 181)
black = (0, 0, 0)


current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'images')

image1 = pygame.image.load(os.path.join(image_path, 'medium_circle.png'))
rect1 = image1.get_rect()
rect1.center = (width // 2, height // 2)
mask_circle = pygame.mask.from_surface(image1)

image2 = pygame.image.load(os.path.join(image_path, 'small_rectangle.png'))
rect2 = image2.get_rect()
mask_rect = pygame.mask.from_surface(image2)


font = pygame.font.Font('freesansbold.ttf', 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)

    rect2.center = pygame.mouse.get_pos()

    surface.blit(image1, rect1)
    surface.blit(image2, rect2)

    message = ''

    offset = (rect2.x - rect1.x, rect2.y - rect1.y)
    if mask_circle.overlap(mask_rect, offset):
        message = 'Existe una colisión'

    text = font.render(message, True, blue)
    rect3 = text.get_rect()
    rect3.midtop = (width // 2, 50)

    surface.blit(text, rect3)

    pygame.display.update()
