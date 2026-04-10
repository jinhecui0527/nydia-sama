"""Emotion-to-expression mapping for natural responses."""

from typing import Dict


class EmotionalExpression:
    def render(self, affect: Dict[str, float]) -> str:
        warmth = affect.get("warmth", 0.5)
        return "gentle" if warmth >= 0.7 else "neutral"
