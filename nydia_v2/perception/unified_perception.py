"""Unified perception module."""

from typing import Dict

from .attention import AttentionController
from .sensory_fusion import SensoryFusion


class UnifiedPerceptionEngine:
    def __init__(self) -> None:
        self.attention = AttentionController()
        self.fusion = SensoryFusion()

    def perceive(self, payload: Dict[str, str]) -> Dict[str, object]:
        scores = self.attention.score(payload)
        return self.fusion.fuse(payload, scores)
