import pygame
import pygame_gui

from game import Game
from game_states import GameState
from services.config import SCREEN_HEIGHT, SCREEN_WIDTH
from utils.sound_initializer import load_sounds


def main():
    pygame.init()
    GameState.ui_manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
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
