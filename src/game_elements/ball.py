import pygame

from config import (
    BALL_ACCELERATION,
    BALL_MAX_SPEED,
    BALL_SIZE,
    HUD_HEIGHT,
    MAX_ANGLE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SPEED_INCREASE_FACTOR,
)
from game_elements import DamageSource, GameObject
from services import Services
from services.game_events import GameEvent
from services.sound_manager import SoundID


class Ball(GameObject, DamageSource):
    def __init__(self):
        super().__init__(
            width=BALL_SIZE,
            height=BALL_SIZE,
            pos=pygame.Vector2((SCREEN_WIDTH - BALL_SIZE) // 2, SCREEN_HEIGHT // 2),
            vel=pygame.Vector2(0, 0),
        )
        self.prev_rect = self.rect.copy()
        self.damage = 10
        self.spawning = True

    def update(self, delta):
        self.prev_rect = self.rect.copy()

        if self.spawning:
            self.vel.y += BALL_ACCELERATION * delta
            if self.vel.y >= BALL_MAX_SPEED:
                self.vel.y = BALL_MAX_SPEED
                self.spawning = False

        self.pos += self.vel * delta

        if self.pos.x < 0 or self.pos.x > SCREEN_WIDTH - self.rect.width:
            self.vel.x *= -1
            Services.sound_manager.play(SoundID.BALL_WALL_COLLISION)

        if self.pos.y < HUD_HEIGHT:
            self.pos.y = HUD_HEIGHT
            self.vel.y *= -1
            Services.sound_manager.play(SoundID.BALL_WALL_COLLISION)

        self.rect.topleft = self.pos

    def bounce_from_player(self, rect: pygame.Rect):
        self.rect.bottom = rect.top
        self.pos.y = self.rect.top
        offset = self.rect.centerx - rect.centerx
        direction_x = offset / (rect.width // 2)
        self.vel.x = direction_x * MAX_ANGLE
        self.vel.y *= -SPEED_INCREASE_FACTOR

        Services.sound_manager.play(SoundID.BALL_PLAYER_COLLISION)

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

        Services.sound_manager.play(SoundID.BALL_BLOCK_COLLISION)

    def get_damage(self) -> int:
        Services.event_bus.emit(GameEvent.BALL_SPAWN)
        return self.damage
