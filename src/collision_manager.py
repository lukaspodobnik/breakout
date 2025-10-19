import pygame


class CollisionManager:
    def __init__(self, player, balls, blocks):
        self.player: pygame.sprite.GroupSingle = player
        self.balls: pygame.sprite.Group = balls
        self.blocks: pygame.sprite.Group = blocks

    def update(self):
        self._handle_player_balls()

    def _handle_player_balls(self):
        collisions = pygame.sprite.spritecollide(self.player.sprite, self.balls, False)
        for ball in collisions:
            ball.bounce_up()
