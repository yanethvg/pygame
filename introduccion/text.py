import pygame
import sys
import os

pygame.init()

width = 600
height = 600

surface = pygame.display.set_mode( (width, height)) # surface
pygame.display.set_caption('Text')
#los colores se dominan con RGB
#a traves de la clase color
red = pygame.Color(255,0,0) # 0- 255 rojo
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)
white = pygame.Color(255,255,255)
black = pygame.Color(0,0,0)

current_path = os.path.dirname(__file__) 
roboto_path = os.path.join(current_path, 'roboto')

#1. obtener una fuente
#font = pygame.font.Font('freesansbold.ttf',48)
font = pygame.font.Font(os.path.join(roboto_path,'Roboto-Thin.ttf'),48)

#2. crear el texto
text = font.render('Hola Mundo!',True,red) # nos retorna una surface
#centrarlo
rect = text.get_rect()
rect.center = ( width // 2 , height // 2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #pintando la pantalla
    surface.fill(white)

    surface.blit(text,rect)

    pygame.display.update()