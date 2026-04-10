"""Attention controller to prioritize multi-modal signals."""

from dataclasses import dataclass
from typing import Dict


@dataclass
class AttentionController:
    text_weight: float = 0.4
    audio_weight: float = 0.3
    visual_weight: float = 0.3

    def score(self, payload: Dict[str, str]) -> Dict[str, float]:
        return {
            "text": self.text_weight if payload.get("text") else 0.0,
            "audio": self.audio_weight if payload.get("audio") else 0.0,
            "visual": self.visual_weight if payload.get("visual") else 0.0,
        }
