"""Fuse text, audio, and visual channels into one representation."""

from typing import Dict


class SensoryFusion:
    def fuse(self, payload: Dict[str, str], scores: Dict[str, float]) -> Dict[str, object]:
        dominant = max(scores, key=scores.get) if scores else "text"
        return {
            "dominant_channel": dominant,
            "signals": payload,
            "weights": scores,
        }
