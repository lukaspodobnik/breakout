from game_elements.block import Block


def square_3x3(position: tuple[int, int]) -> None:
    for i in range(1, 4):
        for j in range(1, 4):
            Block(pos_x=j * position[0], pos_y=i * position[1])


def line_1x10(position: tuple[int, int]) -> None:
    for i in range(1, 11):
        Block(pos_x=i * position[0], pos_y=position[1])
