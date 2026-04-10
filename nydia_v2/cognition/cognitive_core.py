"""Cognitive core combines reasoning and intuition."""

from typing import Dict

from .intuition import IntuitionEngine
from .reasoning import ReasoningEngine


class CognitiveCore:
    def __init__(self) -> None:
        self.reasoning = ReasoningEngine()
        self.intuition = IntuitionEngine()

    def process(self, perception: Dict[str, object]) -> Dict[str, object]:
        thought = self.reasoning.think(perception)
        affect = self.intuition.appraise(perception)
        return {"thought": thought, "affect": affect}
