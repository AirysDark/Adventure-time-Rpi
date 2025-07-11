import pygame

class PauseMenu:
    def __init__(self):
        self.options = ["Resume", "Save", "Load", "Quit"]
        self.font = pygame.font.SysFont("Arial", 24)
        self.selected = 0
        self.active = False

    def toggle(self):
        self.active = not self.active

    def draw(self, screen):
        if not self.active:
            return
        pygame.draw.rect(screen, (0, 0, 0), (150, 100, 300, 220))
        for i, option in enumerate(self.options):
            color = (255, 255, 255) if i != self.selected else (255, 255, 0)
            text = self.font.render(option, True, color)
            screen.blit(text, (180, 130 + i * 40))
