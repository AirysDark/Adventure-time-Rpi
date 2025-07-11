import pygame
import json
import os

TILE_SIZE = 16

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.spritesheet = pygame.image.load("assets/sprites/finn.png").convert_alpha()
        self.animations = self.load_animations()
        self.direction = "down"
        self.frame = 0
        self.image = self.animations[self.direction][self.frame]
        self.rect = self.image.get_rect(topleft=(pos[0] * TILE_SIZE, pos[1] * TILE_SIZE))
        self.velocity = 2
        self.counter = 0

    def load_animations(self):
        animations = {"down": [], "left": [], "right": [], "up": []}
        for i, key in enumerate(animations.keys()):
            for j in range(2):
                frame = self.spritesheet.subsurface(pygame.Rect(j * 16, i * 16, 16, 16))
                animations[key].append(frame)
        return animations

    def handle_keys(self, keys):
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx = -self.velocity
            self.direction = "left"
        elif keys[pygame.K_RIGHT]:
            dx = self.velocity
            self.direction = "right"
        elif keys[pygame.K_UP]:
            dy = -self.velocity
            self.direction = "up"
        elif keys[pygame.K_DOWN]:
            dy = self.velocity
            self.direction = "down"

        self.rect.x += dx
        self.rect.y += dy

    def update(self, keys):
        self.handle_keys(keys)
        self.counter += 1
        if self.counter % 10 == 0:
            self.frame = (self.frame + 1) % 2
            self.image = self.animations[self.direction][self.frame]
