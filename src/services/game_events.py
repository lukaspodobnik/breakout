from enum import Enum, auto


class GameEvent(Enum):
    START_GAME = auto()
    STOP_GAME = auto()

    PLAYER_HEALTH_CHANGED = auto()
    PLAYER_EXP_CHANGED = auto()
    PLAYER_DEATH = auto()
    PLAYER_LEVEL_UP = auto()

    BALL_SPAWN = auto()
