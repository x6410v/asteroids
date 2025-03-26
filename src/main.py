import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import CircleShape

def main() -> None:
    # init pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    delta_time = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        delta_time = game_clock.tick(60) / 1000

        updatable.update(delta_time)
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        for obj in asteroid:
            if obj.collides_with(player):
                print('Game over!')
                import sys
                sys.exit()

        pygame.display.flip()


if __name__ == "__main__":
    main()
