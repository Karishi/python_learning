from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.duration = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "lightblue", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        self.duration += 1
        if self.duration >= 200:
            self.kill()