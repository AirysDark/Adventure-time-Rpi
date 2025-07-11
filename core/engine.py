import pygame
import sys
from scenes.scene_loader import load_scene

current_scene = None

class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("AdventureTimeClone")
        self.clock = pygame.time.Clock()
        self.running = True
        import core.engine
        core.engine.current_scene = load_scene("title")

    def run(self):
        import core.engine
        while self.running:
            scene = core.engine.current_scene
            scene.handle_events()
            scene.update()
            scene.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)
