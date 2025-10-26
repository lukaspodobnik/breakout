from game_states import GameState
from ui.pause import PauseUI


class Pause(GameState):
    def __init__(self):
        super().__init__(PauseUI(self.ui_manager))

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
