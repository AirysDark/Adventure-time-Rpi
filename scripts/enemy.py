import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((16, 16))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = random.choice(["up", "down", "left", "right"])
        self.speed = 1
        self.health = 3
        self.hit_timer = 0

    def update(self):
        if self.hit_timer > 0:
            self.hit_timer -= 1
            self.image.set_alpha(128)
        else:
            self.image.set_alpha(255)

        if self.direction == "up":
            self.rect.y -= self.speed
        elif self.direction == "down":
            self.rect.y += self.speed
        elif self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "right":
            self.rect.x += self.speed

        if random.random() < 0.01:
            self.direction = random.choice(["up", "down", "left", "right"])

    def hit(self):
        if self.hit_timer == 0:
            self.health -= 1
            self.hit_timer = 30
        return self.health <= 0
