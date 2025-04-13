from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_SPEED, SHOT_COOLDOWN
import pygame
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(x, y, radius = PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
    
        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        return super().draw(screen)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt/2)
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot()
        
        if self.timer > 0:
            self.timer -= dt

    def shoot(self):
        pew = Shot(self.position.x, self.position.y)
        pew.velocity = pygame.Vector2(0,1).rotate(self.rotation) * SHOT_SPEED
        self.timer = SHOT_COOLDOWN

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt