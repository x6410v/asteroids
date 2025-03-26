import pygame
from constants import *
from player import *


def main():
    # init pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    delta_time = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    # create groups


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

        pygame.display.flip()


if __name__ == "__main__":
    main()
