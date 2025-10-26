from enum import Enum, auto
from typing import Any, Callable


class GameEvent(Enum):
    PLAYER_HEALTH_CHANGED = auto()
    PLAYER_EXP_CHANGED = auto()
    PLAYER_DEATH = auto()
    BALL_SPAWN = auto()


class EventBus:
    def __init__(self):
        self._subscribers: dict[GameEvent, list[Callable[..., None]]] = {}

    def subscribe(self, event_type: GameEvent, callback: Callable[..., None]) -> None:
        self._subscribers[event_type].append(callback)

    def unsubscribe(self, event_type: GameEvent) -> None:
        del self._subscribers[event_type]

    def emit(self, event_type: GameEvent, **kwargs: Any) -> None:
        for callback in self._subscribers[event_type]:
            callback(**kwargs)

    def clear(self):
        self._subscribers.clear()
