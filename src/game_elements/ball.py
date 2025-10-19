import pygame

from game_elements import GameObject


class Ball(GameObject):
    def __init__(self):
        super().__init__(
            width=10, height=10, pos=pygame.Vector2(0, 0), vel=pygame.Vector2(0, 200)
        )

    def update(self, delta):
        self.pos += self.vel * delta
        self.rect.topleft = self.pos

    def bounce_up(self):
        self.vel.y *= -1