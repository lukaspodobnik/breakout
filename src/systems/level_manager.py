from systems.spawner import Spawner


class LevelManager:
    def __init__(self):
        self.level: str = None
        self.time: float = 0.0
        self.events: list[dict] = None
        self.spawner: Spawner = None
        self.running: bool = False

    def update(self, delta):
        if not self.running:
            return

        self.timer += delta
        while self.time >= self.events[0]["time"]:
            event = self.events.pop(0)
            self.spawner.spawn_structure(
                name=event["structure"], position=event["position"]
            )

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def set_level(self, level):
        pass
