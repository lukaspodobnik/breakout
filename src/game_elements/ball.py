import pygame

from config import SCREEN_WIDTH
from game_elements import GameObject


class Ball(GameObject):
    def __init__(self):
        super().__init__(
            width=10, height=10, pos=pygame.Vector2(0, 0), vel=pygame.Vector2(0, 300)
        )
        self.pos.update(200, 0)

    def update(self, delta):
        self.pos += self.vel * delta
        self.rect.topleft = self.pos

        if self.pos.x < 0 or self.pos.x > SCREEN_WIDTH - self.rect.width:
            self.vel.x *= -1

    def bounce_up(self, direction_x):
        self.vel.x = direction_x * 200
        self.vel.y *= -1
