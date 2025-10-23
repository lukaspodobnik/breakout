import pygame

from config import BALL_SIZE, BALL_SPEED, MAX_ANGLE, SCREEN_WIDTH
from game_elements import GameObject


class Ball(GameObject):
    sounds: dict[str, pygame.mixer.Sound] = {}

    def __init__(self):
        super().__init__(
            width=BALL_SIZE,
            height=BALL_SIZE,
            pos=pygame.Vector2(0, 0),
            vel=pygame.Vector2(0, BALL_SPEED),
        )
        self.pos.update(200, 0)
        self.prev_rect = self.rect.copy()

    def update(self, delta):
        self.prev_rect = self.rect.copy()

        self.pos += self.vel * delta
        self.rect.topleft = self.pos

        if self.pos.x < 0 or self.pos.x > SCREEN_WIDTH - self.rect.width:
            self.vel.x *= -1
        if self.pos.y < 0:
            self.vel.y *= -1

    def bounce_from_player(self, rect: pygame.Rect):
        offset = self.rect.centerx - rect.centerx
        direction_x = offset / (rect.width // 2)
        self.vel.x = direction_x * MAX_ANGLE
        self.vel.y *= -1

    def bounce_from_block(self, rect: pygame.Rect):
        if self.prev_rect.right <= rect.left and self.rect.right > rect.left:
            self.vel.x *= -1
            self.rect.right = rect.left

        elif self.prev_rect.left >= rect.right and self.rect.left < rect.right:
            self.vel.x *= -1
            self.rect.left = rect.right

        elif self.prev_rect.bottom <= rect.top and self.rect.bottom > rect.top:
            self.vel.y *= -1
            self.rect.bottom = rect.top

        elif self.prev_rect.top >= rect.bottom and self.rect.top < rect.bottom:
            self.vel.y *= -1
            self.rect.top = rect.bottom

        self.sounds["block_collision"].play()
