from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Callable

import pygame


class GameStateID(Enum):
    MAIN_MENU = auto()
    PLAYING = auto()
    GAME_OVER = auto()
    LEVEL_UP = auto()
    PAUSE = auto()


class GameState(ABC):
    stop_game: Callable[[], None]

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

    @abstractmethod
    def enter(self) -> None:
        pass

    @abstractmethod
    def exit(self) -> None:
        pass


class GameStateMachine:
    def __init__(self, states: dict[GameStateID, GameState], init_state: GameStateID):
        self.states: dict[GameStateID, GameState] = states
        self.current_state: GameState = states[init_state]
        self.current_state.enter()

    def change_state(self, new_state_id: GameStateID):
        self.current_state.exit()
        self.current_state = self.states[new_state_id]
        self.current_state.enter()

    def handle_events(self):
        self.current_state.handle_events()

    def update(self, delta):
        self.current_state.update(delta)

    def draw(self, screen):
        self.current_state.draw(screen)
