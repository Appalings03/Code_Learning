import pygame
from game import Game

def main():
    pygame.init()

    # Game code
    # variables

    game = Game()

    game.runGameLoop()

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()