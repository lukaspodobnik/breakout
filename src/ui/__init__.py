from abc import ABC

import pygame_gui


class UserInterface(ABC):
    def __init__(self):
        self.elements: list[pygame_gui.core.UIElement] = []

    def show(self):
        for element in self.elements:
            element.show()

    def hide(self):
        for element in self.elements:
            element.hide()

    def destroy(self):
        for element in self.elements:
            element.kill()

        self.elements.clear()
