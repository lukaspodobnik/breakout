from enum import Enum, auto

import pygame
from pygame import Sound

from config import SOUNDS_DIR


class SoundID(Enum):
    BALL_BLOCK_COLLISION = auto()
    BALL_PLAYER_COLLISION = auto()
    BALL_WALL_COLLISION = auto()


class SoundManager:
    def __init__(self):
        self.sounds: dict[SoundID, pygame.Sound]
        self._load_sounds()

    def _load_sounds(self) -> None:
        self.sounds = {
            SoundID.BALL_BLOCK_COLLISION: Sound(
                str(SOUNDS_DIR / "ball_block_collision.wav")
            ),
            SoundID.BALL_PLAYER_COLLISION: Sound(
                str(SOUNDS_DIR / "ball_player_collision.wav")
            ),
            SoundID.BALL_WALL_COLLISION: Sound(
                str(SOUNDS_DIR / "ball_wall_collision.wav")
            ),
        }

    def play(self, id: SoundID) -> None:
        self.sounds[id].play()
