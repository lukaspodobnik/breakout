import pygame

from config import DEATH, LEVEL_UP, SPAWN_BALL
from game_elements.ball import Ball
from game_elements.block import Block
from game_elements.player import Player
from game_elements.player.damage_zone import DamageZone
from game_states import GameState
from systems.collision_manager import CollisionManager
from systems.level_manager import LevelManager


class Playing(GameState):
    def __init__(self):
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.damage_zone = pygame.sprite.GroupSingle()
        self.balls = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.damage_sources = pygame.sprite.Group()

        self.collision_manager = CollisionManager(
            self.player, self.balls, self.blocks, self.damage_zone, self.damage_sources
        )
        self.level_manager = LevelManager()

        Player.groups = (self.updatable, self.drawable, self.player)
        Ball.groups = (self.updatable, self.drawable, self.balls, self.damage_sources)
        Block.groups = (self.updatable, self.drawable, self.blocks)
        DamageZone.groups = (self.damage_zone,)

    def enter(self):
        Player()
        Ball()
        DamageZone()

        self.level_manager.set_level("001_level.json")
        self.level_manager.start()

    def exit(self):
        self.level_manager.stop()

    def _handle_event(self, event: pygame.event.Event) -> None:
        if event.type == SPAWN_BALL:
            Ball()
        elif event.type == DEATH:
            print("!!!DEATH!!!")
        elif event.type == LEVEL_UP:
            print("!!!LEVEL_UP!!!")

    def update(self, delta: int) -> None:
        self.updatable.update(delta)
        self.collision_manager.update()
        self.level_manager.update(delta)

    def _draw(self, screen: pygame.Surface) -> None:
        self.drawable.draw(screen)
