from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Callable

import pygame
import pygame_gui

from config import SCREEN_HEIGHT, SCREEN_WIDTH
from ui import UserInterface


class GameStateID(Enum):
    MAIN_MENU = auto()
    PLAYING = auto()
    GAME_OVER = auto()
    LEVEL_UP = auto()
    PAUSE = auto()


class GameState(ABC):
    stop_game: Callable[[], None]
    ui_manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

    def __init__(self, ui):
        self.ui: UserInterface = ui

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop_game()
            else:
                self._handle_event(event)

            self.ui_manager.process_events(event)

    @abstractmethod
    def _handle_event(self, event: pygame.event.Event) -> None:
        pass

    def update(self, delta) -> None:
        self.ui_manager.update(delta)
        self._update(delta)

    @abstractmethod
    def _update(self, delta) -> None:
        pass

    def draw(self, screen: pygame.Surface) -> None:
        screen.fill(pygame.Color("black"))
        self._draw(screen)
        self.ui_manager.draw_ui(screen)
        pygame.display.flip()

    @abstractmethod
    def _draw(self, screen: pygame.Surface) -> None:
        pass

    def enter(self) -> None:
        self.ui.show()
        self._enter()

    @abstractmethod
    def _enter(self) -> None:
        pass

    def exit(self) -> None:
        self.ui.hide()
        self._exit()

    @abstractmethod
    def _exit(self) -> None:
        pass


class GameStateMachine:
    def __init__(self, states: dict[GameStateID, GameState], init_state: GameStateID):
        self.states: dict[GameStateID, GameState] = states
        self.current_state: GameState = states[init_state]
        self.current_state._enter()

    def change_state(self, new_state_id: GameStateID):
        self.current_state._exit()
        self.current_state = self.states[new_state_id]
        self.current_state._enter()

    def handle_events(self):
        self.current_state.handle_events()

    def update(self, delta):
        self.current_state.update(delta)

    def draw(self, screen):
        self.current_state.draw(screen)
