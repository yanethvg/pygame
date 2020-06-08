import pygame
import sys

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode( (width, height)) # surface
pygame.display.set_caption('Objetos')
#los colores se dominan con RGB
#a traves de la clase color
red = pygame.Color(255,0,0) # 0- 255 rojo
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)
white = pygame.Color(255,255,255)
black = pygame.Color(0,0,0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #pintando la pantalla
    surface.fill(white)
    #triangulo
    pygame.draw.polygon(surface,green,( (0,400),(100,300),(200,400) ))

    #pentagono
    pygame.draw.polygon(surface,red,( 
        (146,0),
        (291,106),
        (236,277),
        (56,277),
        (0,106)
      ))
    pygame.display.update()