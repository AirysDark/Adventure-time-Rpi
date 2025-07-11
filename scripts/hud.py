import pygame

def draw_hud(screen, hp):
    heart = pygame.Surface((16, 16))
    heart.fill((255, 0, 0))
    for i in range(hp):
        screen.blit(heart, (10 + i * 18, 10))
