from services.event_bus import EventBus


class Services:
    event_bus: EventBus

    @classmethod
    def init(cls) -> None:
        cls.event_bus = EventBus()
