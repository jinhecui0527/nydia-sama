"""Reasoning module for explicit deliberation."""

from typing import Dict


class ReasoningEngine:
    def think(self, perception: Dict[str, object]) -> Dict[str, str]:
        text = perception.get("signals", {}).get("text", "")
        dominant = perception.get("dominant_channel", "text")
        plan_hint = "respond verbally" if dominant == "audio" else "respond in text"
        return {
            "analysis": f"Dominant input: {dominant}.",
            "intent": plan_hint,
            "topic": text[:80] if text else "ambient",
        }
