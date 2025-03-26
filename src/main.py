import pygame
from constants import *
from player import *


def main():
    # init pygame
    pygame.init()
    game_clock = pygame.time.Clock()
    delta_time = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        delta_time = game_clock.tick(60) / 1000
        screen.fill("black")
        player.draw(screen)
        player.update(delta_time)
        pygame.display.flip()











if __name__ == "__main__":
    main()
