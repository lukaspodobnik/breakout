import pygame

from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from game_states import GameState
from game_states.playing import Playing


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Breakout")
        self.screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.running: bool = False
        self.state: GameState = Playing(self.stop)

    def run(self) -> None:
        self.running = True
        delta = 0
        while self.running:
            self.state.handle_events()
            self.state.update(delta)
            self.state.draw(self.screen)
            delta = self.clock.tick(FPS) / 1000.0

        pygame.quit()

    def stop(self) -> None:
        self.running = False
