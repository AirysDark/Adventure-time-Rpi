import pygame
import pytmx
import json
from scripts.player import Player
from core.save_system import save_game

class CandyKingdom:
    def __init__(self):
        self.map = pytmx.load_pygame("maps/candy_kingdom.tmx")
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
