from game_states import GameState
from ui.game_over import GameOverUI


class GameOver(GameState):
    def __init__(self):
        super().__init__(GameOverUI(self.ui_manager))

    def _enter(self):
        print("GameOver entered!")

    def _exit(self):
        pass

    def _handle_event(self, event):
        pass

    def _update(self, delta):
        pass

    def _draw(self, screen):
        pass
