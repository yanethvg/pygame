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
    #draw
    #1.- Donde se pintara la figura
    #2.- De que color sera la figura
    #el orden del pintado si importa por eso la linea aparece encima del circulo y el rectangulo
    pygame.draw.rect(surface,red, (100,100,80,40))

    pygame.draw.circle(surface,green,(200,300),100)

    pygame.draw.line(surface,black,(100,100),(200,300),2)

    
    pygame.display.update()