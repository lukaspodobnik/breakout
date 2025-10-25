import time

import pygame

from config import FPS, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE
from game_states import GameState, GameStateID, GameStateMachine
from game_states.game_over import GameOver
from game_states.level_up import LevelUp
from game_states.main_menu import MainMenu
from game_states.pause import Pause
from game_states.playing import Playing


def create_game_state_machine(stop_game) -> GameStateMachine:
    GameState.stop_game = stop_game
    states = {
        GameStateID.MAIN_MENU: MainMenu(),
        GameStateID.PLAYING: Playing(),
        GameStateID.GAME_OVER: GameOver(),
        GameStateID.PAUSE: Pause(),
        GameStateID.LEVEL_UP: LevelUp(),
    }
    return GameStateMachine(states, GameStateID.PLAYING)


class Game:
    def __init__(self):
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = False
        self.game_state_machine = create_game_state_machine(self.stop)

    def run(self) -> None:
        frame_count = sum_handle = sum_update = sum_draw = 0

        self.running = True
        while self.running:
            delta = self.clock.tick(FPS) / 1000.0

            frame_count += 1

            t0 = time.perf_counter()
            self.game_state_machine.handle_events()
            t1 = time.perf_counter()
            self.game_state_machine.update(delta)
            t2 = time.perf_counter()
            self.game_state_machine.draw(self.screen)
            t3 = time.perf_counter()

            sum_handle += t1 - t0
            sum_update += t2 - t1
            sum_draw += t3 - t2

            if frame_count == 60:
                """print(
                    f"handle={sum_handle / frame_count * 1000:.2f}ms  "
                    f"update={sum_update / frame_count * 1000:.2f}ms  "
                    f"draw={sum_draw / frame_count * 1000:.2f}ms "
                    f"combined={(sum_handle + sum_update + sum_draw) / frame_count * 1000:.2f}ms "
                    f"FPS: {self.clock.get_fps():.1f}"
                )"""
                frame_count = sum_handle = sum_update = sum_draw = 0

        pygame.quit()

    def stop(self) -> None:
        self.running = False
