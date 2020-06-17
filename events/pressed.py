import pygame
import sys


pygame.init()

width = 600
height = 600

surface = pygame.display.set_mode((width, height))  # surface
pygame.display.set_caption('Eventos del teclado')
# los colores se dominan con RGB
# a traves de la clase color
red = pygame.Color(255, 0, 0)  # 0- 255 rojo
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        print('Arriba')

    if pressed[pygame.K_a]:
        print('Izquierda')

    if pressed[pygame.K_s]:
        print('Abajo')

    if pressed[pygame.K_d]:
        print('Derecha')

    # pintando la pantalla
    surface.fill(white)
    pygame.display.update()
