import pygame

from game_elements import GameObject


class Block(GameObject):
    def __init__(self, pos_x, pos_y):
        super().__init__(
            width=20,
            height=15,
            pos=pygame.Vector2(pos_x, pos_y),
            color=pygame.Color("red"),
        )
        self.rect.topleft = self.pos

    def update(self, delta):
        pass
