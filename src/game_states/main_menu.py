import pygame_gui

from game_states import GameState
from services import Services
from services.game_events import GameEvent
from ui.main_menu import MainMenuUI


class MainMenu(GameState):
    def __init__(self):
        super().__init__(MainMenuUI(self.ui_manager))

    def _enter(self):
        pass

    def _exit(self):
        pass

    def _handle_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.ui.start_button:
                Services.event_bus.emit(GameEvent.START_GAME)
            elif event.ui_element == self.ui.quit_button:
                Services.event_bus.emit(GameEvent.STOP_GAME)

    def _update(self, delta):
        pass

    def _draw(self, screen):
        pass
