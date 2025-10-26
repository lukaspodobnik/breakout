import pygame

from config import (
    EXP_BASE,
    EXP_GROWTH,
    PLAYER_HEIGHT,
    PLAYER_SPEED,
    PLAYER_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from game_elements import GameObject
from services import Services
from services.game_events import GameEvent


class Player(GameObject):
    def __init__(self):
        super().__init__(
            width=PLAYER_WIDTH,
            height=PLAYER_HEIGHT,
            pos=pygame.Vector2((SCREEN_WIDTH - PLAYER_WIDTH) // 2, SCREEN_HEIGHT - 50),
            vel=pygame.Vector2(PLAYER_SPEED, 0),
        )
        self.hp = 20
        self.level = 1
        self.exp = 0
        self.exp_to_next = EXP_BASE

    def update(self, delta):
        direction = 0
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
            direction -= 1
        if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
            direction += 1

        self.pos += self.vel * direction * delta
        self.clamp()
        self.rect.topleft = self.pos

    def clamp(self):
        if self.pos.x < 0:
            self.pos.x = 0
        elif self.pos.x > SCREEN_WIDTH - self.rect.width:
            self.pos.x = SCREEN_WIDTH - self.rect.width

    def apply_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp <= 0:
            Services.event_bus.emit(GameEvent.PLAYER_DEATH)

    def add_exp(self, exp) -> None:
        self.exp += exp
        if self.exp >= self.exp_to_next:
            self.exp_to_next = int(EXP_BASE * EXP_GROWTH**self.level)
            self.level += 1
            Services.event_bus.emit(GameEvent.PLAYER_LEVEL_UP, {"level": self.level})
