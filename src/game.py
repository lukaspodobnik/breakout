import time

import pygame

from config import FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from game_states import GameState
from game_states.playing import Playing


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Breakout")
        self.screen: pygame.Surface = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.running: bool = False
        self.state: GameState = Playing(self.stop)

    def run(self) -> None:
        frame_count = sum_handle = sum_update = sum_draw = 0

        self.running = True
        while self.running:
            delta = self.clock.tick(FPS) / 1000.0

            frame_count += 1

            t0 = time.perf_counter()
            self.state.handle_events()
            t1 = time.perf_counter()
            self.state.update(delta)
            t2 = time.perf_counter()
            self.state.draw(self.screen)
            t3 = time.perf_counter()

            sum_handle += t1 - t0
            sum_update += t2 - t1
            sum_draw += t3 - t2

            if frame_count == 60:
                print(
                    f"handle={sum_handle / frame_count * 1000:.2f}ms  "
                    f"update={sum_update / frame_count * 1000:.2f}ms  "
                    f"draw={sum_draw / frame_count * 1000:.2f}ms "
                    f"FPS: {self.clock.get_fps():.1f}"
                )
                frame_count = sum_handle = sum_update = sum_draw = 0

        pygame.quit()

    def stop(self) -> None:
        self.running = False
