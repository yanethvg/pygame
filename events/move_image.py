import sys
import pygame
import os

pygame.init()

width = 600
height = 600

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Mover imagen')

# RGB
white = (255, 255, 255)
red = (134, 45, 83)

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'images')

image = pygame.image.load(os.path.join(image_path, 'medium_circle.png'))

rect = image.get_rect()
rect.center = (width // 2, height // 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        # modificar el atributo y
        rect.y -= 5

    if pressed[pygame.K_a]:
        rect.x -= 5

    if pressed[pygame.K_s]:
        rect.y += 5

    if pressed[pygame.K_d]:
        rect.x += 5

    # validaciones
    if rect.left < 0:
        rect.left = 0

    if rect.right > width:
        rect.right = width

    if rect.top < 0:
        rect.top = 0

    if rect.bottom > height:
        rect.bottom = height

    surface.fill(white)
    surface.blit(image, rect)

    pygame.display.update()
