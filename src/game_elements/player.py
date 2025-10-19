import pygame

from config import SCREEN_HEIGHT, SCREEN_WIDTH
from game_elements import GameObject


class Player(GameObject):
    def __init__(self):
        super().__init__(
            width=60,
            height=10,
            pos=pygame.Vector2(SCREEN_WIDTH // 2 - 60 // 2, SCREEN_HEIGHT - 50),
            vel=pygame.Vector2(300, 0),
        )

    def update(self, delta: float) -> None:
        direction = 0
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_a]:
            direction -= 1
        if pressed[pygame.K_d]:
            direction += 1

        self.pos += self.vel * direction * delta
        self.clamp()
        self.rect.topleft = self.pos

    def clamp(self):
        if self.pos.x < 0:
            self.pos.x = 0
        elif self.pos.x > SCREEN_WIDTH - self.rect.width:
            self.pos.x = SCREEN_WIDTH - self.rect.width
