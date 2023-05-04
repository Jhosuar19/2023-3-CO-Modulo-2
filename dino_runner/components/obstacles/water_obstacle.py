import pygame

class Water:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (56, 117, 215)  # Color azul para el agua

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

