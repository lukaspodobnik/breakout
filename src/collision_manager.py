import pygame

from game_elements.ball import Ball
from game_elements.block import Block
from game_elements.player import Player


class CollisionManager:
    def __init__(self, player, balls, blocks):
        self.player: pygame.sprite.GroupSingle[Player] = player
        self.balls: pygame.sprite.Group[Ball] = balls
        self.blocks: pygame.sprite.Group[Block] = blocks

    def update(self):
        self._handle_player_balls()
        self._handle_blocks_balls()

    def _handle_player_balls(self):
        player = self.player.sprite
        collisions = pygame.sprite.spritecollide(player, self.balls, False)
        for ball in collisions:
            offset = ball.rect.centerx - player.rect.centerx
            direction_x = offset / (player.rect.width // 2)
            ball.bounce_up(direction_x)

    def _handle_blocks_balls(self):
        collisions = pygame.sprite.groupcollide(self.blocks, self.balls, True, False)
        for ball, block in collisions.items():
            pass
