"""Runtime loop driver for once/loop execution modes."""

from dataclasses import dataclass
from time import sleep
from typing import Callable


@dataclass
class RealtimeDriver:
    interval_ms: int = 100

    def run_once(self, callback: Callable[[], dict]) -> dict:
        return callback()

    def run_loop(self, callback: Callable[[], dict], iterations: int = 3) -> list[dict]:
        outputs: list[dict] = []
        for _ in range(iterations):
            outputs.append(callback())
            sleep(self.interval_ms / 1000)
        return outputs
