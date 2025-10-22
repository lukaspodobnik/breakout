from systems.block_structures import line_1x10, square_3x3


class Spawner:
    def __init__(self):
        self.structures: dict[str, callable] = {
            "square_3x3": square_3x3,
            "line_1x10": line_1x10,
        }

    def spawn_structure(self, name, position):
        self.structures[name](position)
