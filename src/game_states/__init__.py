from abc import ABC, abstractmethod
from typing import Callable

import pygame


class GameState(ABC):
    def __init__(self, stop_game: Callable[[], None]):
        self.stop_game: Callable[[], None] = stop_game

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop_game()
            else:
                self._handle_event(event)

    @abstractmethod
    def _handle_event(self, event: pygame.event.Event) -> None:
        pass

    @abstractmethod
    def update(self, delta: int) -> None:
        pass

    def draw(self, screen: pygame.Surface) -> None:
        screen.fill(pygame.Color("black"))
        self._draw(screen)
        pygame.display.flip()

    @abstractmethod
    def _draw(self, screen: pygame.Surface) -> None:
        pass
