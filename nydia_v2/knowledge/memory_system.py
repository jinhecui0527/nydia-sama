"""Memory system for episodic traces."""

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class MemorySystem:
    episodes: List[Dict[str, object]] = field(default_factory=list)

    def remember(self, perception: Dict[str, object], cognition: Dict[str, object], action: Dict[str, str]) -> None:
        self.episodes.append(
            {
                "perception": perception,
                "cognition": cognition,
                "action": action,
            }
        )

    def recent(self, n: int = 3) -> List[Dict[str, object]]:
        return self.episodes[-n:]
