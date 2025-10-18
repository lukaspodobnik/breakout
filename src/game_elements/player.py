import pygame

from config import SCREEN_HEIGHT, SCREEN_WIDTH
from game_elements import GameObject


class Player(GameObject):
    speed = 300

    def __init__(self):
        super().__init__(width=60, height=10)
        self.pos.update(SCREEN_WIDTH // 2 - self.rect.width // 2, SCREEN_HEIGHT - 50)

    def update(self, delta: float) -> None:
        direction = 0
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]:
            direction -= 1
        if pressed[pygame.K_d]:
            direction += 1

        self.pos += pygame.Vector2(1, 0) * self.speed * direction * delta
        self.rect.topleft = self.pos
