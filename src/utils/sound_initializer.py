from pygame.mixer import Sound

from config import SOUNDS_DIR
from game_elements.ball import Ball


def load_sounds() -> None:
    _load_ball_sounds()


def _load_ball_sounds() -> None:
    Ball.sounds = {
        "block_collision": Sound(str(SOUNDS_DIR / "ball_block_collision.wav"))
    }
