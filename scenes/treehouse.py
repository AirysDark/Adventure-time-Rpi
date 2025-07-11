import pygame
import pytmx
import os
from scripts.player import Player

class Treehouse:
    def __init__(self):
        map_path = os.path.join(os.path.dirname(__file__), "..", "maps", "treehouse.tmx")
        self.map = pytmx.load_pygame(os.path.abspath(map_path))
        self.player = Player([4, 4])
        self.sprites = pygame.sprite.Group(self.player)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys)

    def draw(self, screen):
        for y in range(self.map.height):
            for x in range(self.map.width):
                tile = self.map.get_tile_image(x, y, 0)
                if tile:
                    screen.blit(tile, (x * 16, y * 16))
        self.sprites.draw(screen)
