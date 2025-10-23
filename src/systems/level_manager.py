import json

from config import LEVELS_DIR
from systems.spawner import Spawner


class LevelManager:
    def __init__(self):
        self.level: str = ""
        self.events: list[dict] = []
        self.time: float = 0.0
        self.spawner: Spawner = Spawner()
        self.running: bool = False

    def update(self, delta):
        if not self.running:
            return

        self.time += delta
        while len(self.events) > 0 and self.time >= self.events[0]["time"]:
            event = self.events.pop(0)
            self.spawner.spawn_structure(
                name=event["structure"], position=event["position"]
            )

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def set_level(self, file_name):
        with open(LEVELS_DIR / file_name, "r") as f:
            data = json.load(f)

        self.level = data["name"]
        self.events = sorted(data["events"], key=lambda e: e["time"])
        self.time = 0.0
