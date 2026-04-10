"""Consciousness stream to track current inner state."""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, List


@dataclass
class ConsciousEvent:
    ts: str
    summary: str
    salience: float


@dataclass
class ConsciousnessStream:
    mood: str = "neutral"
    arousal: float = 0.5
    focus: str = "ambient"
    events: List[ConsciousEvent] = field(default_factory=list)

    def ingest(self, summary: str, salience: float = 0.5) -> None:
        salience = max(0.0, min(1.0, salience))
        self.events.append(
            ConsciousEvent(
                ts=datetime.now(timezone.utc).isoformat(),
                summary=summary,
                salience=salience,
            )
        )
        self.arousal = (self.arousal * 0.7) + (salience * 0.3)
        self.focus = summary[:64] if summary else self.focus

    def snapshot(self) -> Dict[str, object]:
        return {
            "mood": self.mood,
            "arousal": round(self.arousal, 3),
            "focus": self.focus,
            "event_count": len(self.events),
        }
