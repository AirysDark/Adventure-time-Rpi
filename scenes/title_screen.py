import pygame
import sys
import core.engine

class TitleScreen:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 30)
        self.title = self.font.render("AdventureTimeClone", True, (255, 255, 0))
        self.option = self.font.render("Press any key to start", True, (255, 255, 255))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                from scenes.scene_loader import load_scene  # moved here to prevent circular import
                core.engine.current_scene = load_scene("treehouse")

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 128))
        screen.blit(self.title, (160, 180))
        screen.blit(self.option, (160, 240))
