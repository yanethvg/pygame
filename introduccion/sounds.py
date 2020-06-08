import pygame
import sys
import os


pygame.init()

width = 600
height = 600

surface = pygame.display.set_mode( (width, height)) # surface
pygame.display.set_caption('Sounds')
#los colores se dominan con RGB
#a traves de la clase color
red = pygame.Color(255,0,0) # 0- 255 rojo
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)
white = pygame.Color(255,255,255)
black = pygame.Color(0,0,0)

current_path = os.path.dirname(__file__) 
image_path = os.path.join(current_path, 'sounds')
pygame.mixer.music.load(os.path.join(image_path,'Haggstrom.mp3'))
pygame.mixer.music.set_volume(1.0) #flotante 0.0 - 1.0 
#parametros opcionales
# se reproduzca dos veces para que nunca deje de sonar -1
#y que comienze en el minuto 1.30
pygame.mixer.music.play(-1,0.0)

#reiniciar la cancion
pygame.mixer.music.rewind()
#pausar la cancion
pygame.mixer.music.pause()
#detener la cancion
pygame.mixer.music.stop()
#detener la cancion de forma poco a poco, la cantidad de milisegundos para que se detenga
pygame.mixer.music.fadeout(5000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

   
    #pintando la pantalla
    surface.fill(white)


    pygame.display.update()