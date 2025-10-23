import pygame

from game_elements import DamageSource
from game_elements.ball import Ball
from game_elements.block import Block
from game_elements.player import Player
from game_elements.player.damage_zone import DamageZone


class CollisionManager:
    def __init__(self, player, balls, blocks, damage_zone, damage_sources):
        self.player: pygame.sprite.GroupSingle[Player] = player
        self.balls: pygame.sprite.Group[Ball] = balls
        self.blocks: pygame.sprite.Group[Block] = blocks
        self.damage_zone: pygame.sprite.GroupSingle[DamageZone] = damage_zone
        self.damage_sources: pygame.sprite.Group[DamageSource] = damage_sources

    def update(self):
        self._handle_player_balls()
        self._handle_blocks_balls()
        self._handle_damage_zone_source()

    def _handle_player_balls(self):
        player = self.player.sprite
        collisions: list[Ball] = pygame.sprite.spritecollide(player, self.balls, False)
        for ball in collisions:
            if ball.vel.y > 0:
                ball.bounce_from_player(player.rect)

    def _handle_blocks_balls(self):
        collisions: dict[Ball, list[Block]] = pygame.sprite.groupcollide(
            self.balls, self.blocks, False, True
        )
        for ball, blocks in collisions.items():
            for block in blocks:
                ball.bounce_from_block(block.rect)

    def _handle_damage_zone_source(self):
        damage_zone = self.damage_zone.sprite
        collisions: list[DamageSource] = pygame.sprite.spritecollide(
            damage_zone, self.damage_sources, True
        )
        for source in collisions:
            damage_zone.apply_damage(source.get_damage())
