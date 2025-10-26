from abc import ABC

import pygame
import pygame_gui


class UserInterface(ABC):
    def __init__(self, manager: pygame_gui.UIManager, rect: pygame.Rect):
        self._panel = pygame_gui.elements.UIPanel(relative_rect=rect, manager=manager)
        self.hide()

    def show(self):
        self._panel.show()

    def hide(self):
        self._panel.hide()

    def destroy(self):
        self._panel.kill()
