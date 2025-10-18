from abc import ABC, abstractmethod

import pygame


class GameObject(ABC, pygame.sprite.Sprite):
    groups = ()

    def __init__(
        self,
        width: int,
        height: int,
        color: pygame.Color = pygame.Color("white"),
        pos: pygame.Vector2 = pygame.Vector2(0, 0),
    ):
        super().__init__(*self.groups)
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.pos: pygame.Vector2 = pos

    @abstractmethod
    def update(self, delta: float) -> None:
        pass
