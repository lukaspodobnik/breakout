from services.event_bus import EventBus
from services.sound_manager import SoundManager


class Services:
    event_bus: EventBus
    sound_manager: SoundManager

    @classmethod
    def init(cls) -> None:
        cls.event_bus = EventBus()
        cls.sound_manager = SoundManager()
