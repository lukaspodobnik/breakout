import pygame

from ui import UserInterface


class LevelUpUI(UserInterface):
    def __init__(self, manager):
        super().__init__(manager, pygame.Rect(0, 0, 100, 100))
