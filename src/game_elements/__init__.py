from abc import ABC, abstractmethod

import pygame


class GameObject(ABC, pygame.sprite.Sprite):
    groups = ()

    def __init__(
        self,
        width: int,
        height: int,
        pos: pygame.Vector2 = None,
        vel: pygame.Vector2 = None,
        color: pygame.Color = pygame.Color("white"),
    ):
        super().__init__(*self.groups)
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.pos: pygame.Vector2 = pos
        self.vel: pygame.Vector2 = vel

    @abstractmethod
    def update(self, delta: float) -> None:
        pass
