from typing import Callable

from game_states.playing.block_structures import line_1x10, square_3x3


class Spawner:
    def __init__(self):
        self.structures: dict[str, Callable[[tuple[int, int]], None]] = {
            "square_3x3": square_3x3,
            "line_1x10": line_1x10,
        }

    def spawn_structure(self, name: str, position: tuple[int, int]):
        self.structures[name](position)
