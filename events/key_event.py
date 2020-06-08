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
        if event.type == pygame.KEYDOWN:
            # if event.key == 115:
            """
            if event.key == pygame.K_s:
                print('Tecla s presionada')
            #print('Tecla presionada')
            """
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                message = 'Izquierda'

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                message = 'Derecha'

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                message = 'Abajo'

            if event.key == pygame.K_UP or event.key == pygame.K_w:
                message = 'Arriba'

            print(message)
        if event.type == pygame.KEYUP:
            #print('Tecla liberada')
            pass
    # pintando la pantalla
    surface.fill(white)
    pygame.display.update()
