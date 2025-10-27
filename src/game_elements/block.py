import pygame

from config import BLOCK_HEIGHT, BLOCK_WIDTH
from game_elements import GameObject


class Block(GameObject):
    def __init__(self, pos_x, pos_y, exp=0):
        super().__init__(
            width=BLOCK_WIDTH,
            height=BLOCK_HEIGHT,
            pos=pygame.Vector2(pos_x, pos_y),
            color=pygame.Color("red"),
        )
        self.rect.topleft = self.pos
        self.exp = exp

    def update(self, delta):
        pass
