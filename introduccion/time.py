import pygame
import sys

pygame.init()

width = 600
height = 600

surface = pygame.display.set_mode( (width, height)) # surface
pygame.display.set_caption('Time')
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

    time = pygame.time.get_ticks() // 1000 # milisegundos para obtener segundos
    print(time)
    #pintando la pantalla
    surface.fill(white)

    pygame.display.update()