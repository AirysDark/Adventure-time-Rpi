import pygame
import sys
from scenes.scene_loader import load_scene

class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("AdventureTimeClone")
        self.clock = pygame.time.Clock()
        self.running = True
        self.scene = load_scene("title")

    def run(self):
        while self.running:
            self.scene.handle_events()
            self.scene.update()
            self.scene.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)
