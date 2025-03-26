from circleshape import CircleShape
from constants import *
import pygame

class Player(CircleShape):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self) -> list:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.surface.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, delta_time: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * delta_time

    def update(self, delta_time: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(delta_time)
        if keys[pygame.K_s]:
            self.move(-delta_time)
        if keys[pygame.K_a]:
            self.rotate(-delta_time)
        if keys[pygame.K_d]:
            self.rotate(delta_time)

    def move(self, delta_time: float) -> None:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * delta_time
