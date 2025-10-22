import pygame

from game_elements.ball import Ball
from game_elements.block import Block
from game_elements.player import Player
from game_states import GameState
from systems.collision_manager import CollisionManager
from systems.level_manager import LevelManager


class Playing(GameState):
    def __init__(self, stop_game):
        super().__init__(stop_game)
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.balls = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()

        self.collision_manager = CollisionManager(self.player, self.balls, self.blocks)
        self.level_manager = LevelManager()

        Player.groups = (self.updatable, self.drawable, self.player)
        Ball.groups = (self.updatable, self.drawable, self.balls)
        Block.groups = (self.updatable, self.drawable, self.blocks)

        Player()
        Ball()
        for i in range(10):
            Block(pos_x=(i * 25), pos_y=10)

    def _handle_event(self, event: pygame.event.Event) -> None:
        pass

    def update(self, delta: int) -> None:
        self.updatable.update(delta)
        self.collision_manager.update()
        self.level_manager.update(delta)

    def _draw(self, screen: pygame.Surface) -> None:
        self.drawable.draw(screen)
