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
