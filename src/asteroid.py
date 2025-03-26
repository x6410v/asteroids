from circleshape import CircleShape
from constants import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x: int, y: int, radius) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.surface.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, delta_time: float) -> None:
        self.position += (self.velocity * delta_time)


