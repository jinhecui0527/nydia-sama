"""Goal manager for short/long-term drives."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class GoalSystem:
    active_goals: List[str] = field(default_factory=lambda: ["maintain rapport", "be truthful"])

    def choose_goal(self, topic: str) -> str:
        return f"assist on: {topic}" if topic and topic != "ambient" else self.active_goals[0]
