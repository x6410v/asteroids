import pygame
from constants import *


def main():
    # init pygame
    pygame.init()
    game_clock = pygame.time.Clock()
    delta_time = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # starting message
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color=(0, 0, 0))
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000

        







if __name__ == "__main__":
    main()
