import pygame
import sys

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode( (width, height)) # surface
pygame.display.set_caption('Surfaces')
#los colores se dominan con RGB
#a traves de la clase color
red = pygame.Color(255,0,0) # 0- 255 rojo
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)
white = pygame.Color(255,255,255)
black = pygame.Color(0,0,0)

surface2 = pygame.Surface( (200,200) )
surface2.fill(green)

#dibujando un rectangulo
rect = surface2.get_rect()
rect.center = ( width // 2 , height // 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #pintando la pantalla
    surface.fill(white)

    surface.blit(surface2, rect)

    pygame.draw.rect(surface2,red,(100,50,80,40))
    pygame.display.update()