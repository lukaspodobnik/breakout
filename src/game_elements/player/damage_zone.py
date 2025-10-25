import pygame

from config import DAMAGE_ZONE_HEIGHT, SCREEN_HEIGHT, SCREEN_WIDTH


class DamageZone(pygame.sprite.Sprite):
    groups = ()

    def __init__(self):
        super().__init__(*self.groups)
        self.rect = pygame.Rect(
            0, SCREEN_HEIGHT - DAMAGE_ZONE_HEIGHT, SCREEN_WIDTH, DAMAGE_ZONE_HEIGHT
        )
