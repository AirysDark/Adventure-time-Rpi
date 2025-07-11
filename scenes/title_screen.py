import pygame
import sys

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
                print("Start game")  # Here, load map scene

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 128))
        screen.blit(self.title, (160, 180))
        screen.blit(self.option, (160, 240))
