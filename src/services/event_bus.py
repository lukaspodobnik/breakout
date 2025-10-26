from typing import Any, Callable

from services.game_events import GameEvent


class EventBus:
    def __init__(self):
        self._subscribers: dict[GameEvent, list[Callable[..., None]]] = {
            event_type: [] for event_type in GameEvent
        }

    def subscribe(self, event_type: GameEvent, callback: Callable[..., None]) -> None:
        self._subscribers[event_type].append(callback)

    def unsubscribe(self, event_type: GameEvent) -> None:
        del self._subscribers[event_type]

    def emit(self, event_type: GameEvent, **kwargs: Any) -> None:
        for callback in self._subscribers[event_type]:
            callback(**kwargs)

    def clear(self):
        self._subscribers.clear()
