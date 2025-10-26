from enum import Enum, auto


class GameEvent(Enum):
    PLAYER_HEALTH_CHANGED = auto()
    PLAYER_EXP_CHANGED = auto()
    PLAYER_DEATH = auto()
    PLAYER_LEVEL_UP = auto()
    
    BALL_SPAWN = auto()

