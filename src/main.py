import pygame

from game import Game
from utils.sound_initializer import load_sounds


def main():
    pygame.init()
    load_sounds()
    Game().run()


if __name__ == "__main__":
    main()


"""
TODO:
    - game-states: menu, pause, finished-level, player-level-up
    - player-ui: experience, hp, speed, size
    - finished-level-state: choose one of three player-enhancements, or items
    - player-enhancements: speed, size, hp
    - items: extra ball, bomb, shield
    - blocks: armored, moving, shooting
    - power-ups (block-drops): speed, size, heal
    - block-structures: armored around shooting
"""
