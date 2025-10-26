import pygame

from config import (
    EXP_BASE,
    EXP_GROWTH,
    PLAYER_ACCELERATION,
    PLAYER_FRICTION,
    PLAYER_HEIGHT,
    PLAYER_MAX_SPEED,
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
            vel=pygame.Vector2(0, 0),
        )
        self.hp = 100
        self.max_hp = 100
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

        if direction == 0:
            if self.vel.x > 0:
                self.vel.x -= PLAYER_FRICTION * delta
                if self.vel.x < 0:
                    self.vel.x = 0
            elif self.vel.x < 0:
                self.vel.x += PLAYER_FRICTION * delta
                if self.vel.x > 0:
                    self.vel.x = 0
        else:
            self.vel.x += direction * PLAYER_ACCELERATION * delta
            self.vel.x = max(-PLAYER_MAX_SPEED, min(self.vel.x, PLAYER_MAX_SPEED))

        self.pos += self.vel * delta
        self._clamp()
        self.rect.topleft = self.pos

    def _clamp(self):
        if self.pos.x < 0:
            self.pos.x = 0
        elif self.pos.x > SCREEN_WIDTH - self.rect.width:
            self.pos.x = SCREEN_WIDTH - self.rect.width

    def apply_damage(self, damage: int) -> None:
        bus = Services.event_bus
        self.hp -= damage
        if self.hp <= 0:
            bus.emit(GameEvent.PLAYER_DEATH)
            return
        bus.emit(GameEvent.PLAYER_HEALTH_CHANGED, hp=(self.hp / self.max_hp) * 100)

    def add_exp(self, exp) -> None:
        bus = Services.event_bus
        self.exp += exp
        if self.exp >= self.exp_to_next:
            self.exp_to_next = int(EXP_BASE * EXP_GROWTH**self.level)
            self.level += 1
            bus.emit(GameEvent.PLAYER_LEVEL_UP, level=self.level)
        bus.emit(GameEvent.PLAYER_EXP_CHANGED, exp=(self.exp / self.exp_to_next) * 100)
