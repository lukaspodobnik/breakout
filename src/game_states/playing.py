import pygame

from collision_manager import CollisionManager
from game_elements.ball import Ball
from game_elements.block import Block
from game_elements.player import Player
from game_states import GameState


class Playing(GameState):
    def __init__(self, stop_game):
        super().__init__(stop_game)
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.balls = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()

        self.collision_manager = CollisionManager(self.player, self.balls, self.blocks)

        Player.groups = (self.updatable, self.drawable, self.player)
        Ball.groups = (self.updatable, self.drawable, self.balls)
        Block.groups = (self.updatable, self.drawable, self.blocks)

        Player()
        Ball()

    def _handle_event(self, event: pygame.event.Event) -> None:
        pass

    def update(self, delta: int) -> None:
        self.updatable.update(delta)
        self.collision_manager.update()

    def _draw(self, screen: pygame.Surface) -> None:
        self.drawable.draw(screen)
