from game_elements import GameObject


class Block(GameObject):
    def __init__(self):
        super().__init__(width=40, height=20)

    def update(self, delta):
        pass
