from services.config import BLOCK_HEIGHT, BLOCK_SPACING, BLOCK_WIDTH
from game_elements.block import Block


def square_3x3(position: tuple[int, int]) -> None:
    x, y = position
    for i in range(3):
        for j in range(3):
            Block(
                pos_x=(j * (BLOCK_WIDTH + BLOCK_SPACING)) + x,
                pos_y=(i * (BLOCK_HEIGHT + BLOCK_SPACING)) + y,
            )


def line_1x10(position: tuple[int, int]) -> None:
    x, y = position
    for i in range(10):
        Block(pos_x=(i * (BLOCK_WIDTH + BLOCK_SPACING)) + x, pos_y=y)
