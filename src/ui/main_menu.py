import pygame
import pygame_gui

from config import SCREEN_HEIGHT, SCREEN_WIDTH
from ui import UserInterface


class MainMenuUI(UserInterface):
    def __init__(self, manager: pygame_gui.UIManager):
        super().__init__(manager, pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

        self.title = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(0, 100, 100, 50),
            text="BREAKOUTER",
            manager=manager,
            container=self._panel,
            anchors={"centerx": "centerx"},
        )

        self.start_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(0, 50, 200, 50),
            text="START",
            manager=manager,
            container=self._panel,
            anchors={"centerx": "centerx", "top_target": self.title},
        )

        self.quit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(0, 50, 200, 50),
            text="QUIT",
            manager=manager,
            container=self._panel,
            anchors={"centerx": "centerx", "top_target": self.start_button},
        )
