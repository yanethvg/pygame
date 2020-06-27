import pygame
import sys
import random
from .config import *
from .platform import Platform
from .player import Player
from .wall import Wall


class Game:
    def __init__(self):
        pygame.init()

        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        self.running = True

    def start(self):
        self.new()

    def new(self):
        self.generate_elements()
        self.run()

    def generate_elements(self):
        self.platform = Platform()
        self.player = Player(100, self.platform.rect.top - 200)

        # generando pared
        #self.wall = Wall(500, self.platform.rect.top)

        self.sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()

        self.sprites.add(self.platform)
        self.sprites.add(self.player)
        # self.sprites.add(self.wall)

        self.generate_walls()

    def generate_walls(self):

        last_position = WIDTH + 100
        if not len(self.walls) > 0:

            for w in range(0, MAX_WALLS):
                left = random.randrange(
                    last_position + 200, last_position + 400)
                wall = Wall(left, self.platform.rect.top)
                last_position = wall.rect.right

                self.sprites.add(wall)
                self.walls.add(wall)

    def run(self):
        while self.running:
            self.events()
            self.draw()
            self.update()

    def events(self):
        # modificando la velocidad de salto
        clock = pygame.time.Clock()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.player.jump()

    def draw(self):
        self.surface.fill(BLACK)

        self.sprites.draw(self.surface)

    def update(self):
        pygame.display.flip()
        # todos los elementos de la lista se actualizaran
        self.sprites.update()

        self.player.validate_platform(self.platform)

        wall = self.player.collide_with(self.walls)
        if wall:
            self.stop()

    def stop(self):
        print("Existe una colisión")