import pygame
import pygame_gui

from config import HUD_HEIGHT, SCREEN_WIDTH
from services import Services
from services.game_events import GameEvent
from ui import UserInterface


class PlayingUI(UserInterface):
    def __init__(self, manager):
        super().__init__(manager, pygame.Rect(0, 0, SCREEN_WIDTH, HUD_HEIGHT))

        self.hp_bar = pygame_gui.elements.UIProgressBar(
            relative_rect=pygame.Rect(0, 0, 100, 40),
            manager=manager,
            container=self._panel,
            anchors={"centery": "centery"},
        )

        self.level_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(0, 0, 100, 40),
            manager=manager,
            text="Level: 1",
            container=self._panel,
            anchors={"centery": "centery", "left_target": self.hp_bar},
        )

        self.exp_bar = pygame_gui.elements.UIProgressBar(
            relative_rect=pygame.Rect(0, 0, 100, 40),
            manager=manager,
            container=self._panel,
            anchors={"centery": "centery", "left_target": self.level_label},
        )

        Services.event_bus.subscribe(
            GameEvent.PLAYER_HEALTH_CHANGED, self._on_player_hp_changed
        )

        Services.event_bus.subscribe(
            GameEvent.PLAYER_EXP_CHANGED, self._on_player_exp_changed
        )

    def _on_player_hp_changed(self, hp: int) -> None:
        self.hp_bar.set_current_progress(hp)

    def _on_player_exp_changed(self, exp: int) -> None:
        self.exp_bar.set_current_progress(exp)

    def _on_player_level_up(self, level: int) -> None:
        self.level_label.set_text(f"Level: {level}")
