import pygame
import sys

pygame.init()

width = 600
height = 600

surface = pygame.display.set_mode( (width, height)) # surface
pygame.display.set_caption('Updated Text')
#los colores se dominan con RGB
#a traves de la clase color
red = pygame.Color(255,0,0) # 0- 255 rojo
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)
white = pygame.Color(255,255,255)
black = pygame.Color(0,0,0)

font = pygame.font.Font('freesansbold.ttf', 48)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

   
    #pintando la pantalla
    surface.fill(white)

    seconds = pygame.time.get_ticks() // 1000
    text = font.render(str(seconds), True, red)
    rect = text.get_rect()
    rect.center = ( width // 2, height // 2)

    surface.blit(text, rect)

    pygame.display.update()