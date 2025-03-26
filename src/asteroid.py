from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x: int, y: int, radius) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.surface.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, delta_time: float) -> None:
        self.position += (self.velocity * delta_time)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        rangle = random.uniform(20.0, 50.0)
        pos_asteroid_vec = self.velocity.rotate(rangle)
        neg_asteroid_vec = self.velocity.rotate(-rangle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = pos_asteroid_vec * 1.2

        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2.velocity = neg_asteroid_vec * 1.2
