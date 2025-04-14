import pygame, random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "brown", self.position, self.radius)
        return super().draw(screen)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20.0, 50.0)
        v1, v2 = self.velocity.rotate(angle), self.velocity.rotate(-angle)
        newSize = self.radius - ASTEROID_MIN_RADIUS
        self.spawn(newSize, self.position, v1 * 1.2)
        self.spawn(newSize, self.position, v2 * 1.2)
        
    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity