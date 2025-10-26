from game_states import GameState
from ui.main_menu import MainMenuUI


class MainMenu(GameState):
    def __init__(self):
        super().__init__(MainMenuUI(self.ui_manager))

    def _enter(self):
        pass

    def _exit(self):
        pass

    def _handle_event(self, event):
        pass

    def _update(self, delta):
        pass

    def _draw(self, screen):
        pass
