"""Intuition module for quick affective appraisal."""

from typing import Dict


class IntuitionEngine:
    def appraise(self, perception: Dict[str, object]) -> Dict[str, float]:
        text = perception.get("signals", {}).get("text", "")
        urgency = 0.9 if "!" in text else 0.5
        warmth = 0.8 if any(k in text.lower() for k in ["thanks", "love", "你好"]) else 0.5
        return {"urgency": urgency, "warmth": warmth}
