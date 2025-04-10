import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "brown", self.position, 20.0)
        return super().draw(screen)
    
    def update(self, dt):
        self.position += self.velocity * dt