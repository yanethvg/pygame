import pygame
import sys

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode( (width, height)) # surface
pygame.display.set_caption('Colores')
#los colores se dominan con RGB
#a traves de la clase color
red = pygame.Color(255,0,0) # 0- 255 rojo
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)

white = pygame.Color(255,255,255)
black = pygame.Color(0,0,0)

#hacer un rectangulo sobre la superficie
#mediante la clase Rect
#pygame.Rect(x,y,width,heigth) posiciones en el plano cartesiano, ancho y alto del rectangulo
rect = pygame.Rect(100,150,120,60)
#para centrar el elemento rect.center = (x, y)
rect.center = (width // 2, height // 2) #doble // para que sea entero

print(rect.x)
print(rect.y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #pintando la pantalla
    surface.fill(white)
    # se ubica en la esquina superior izquierda 
    #colocando el rectangulo
    pygame.draw.rect(surface,red,rect)
    #actualizando el espacio
    pygame.display.update()