import pygame

class Inventory:
    def __init__(self):
        self.items = []
        self.visible = False
        self.font = pygame.font.SysFont("Arial", 18)

    def toggle(self):
        self.visible = not self.visible

    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)

    def draw(self, screen):
        if self.visible:
            pygame.draw.rect(screen, (0, 0, 0), (100, 100, 200, 200))
            pygame.draw.rect(screen, (255, 255, 255), (100, 100, 200, 200), 2)
            for i, item in enumerate(self.items):
                text = self.font.render(f"- {item}", True, (255, 255, 255))
                screen.blit(text, (110, 110 + i * 20))
