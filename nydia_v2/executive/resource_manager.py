"""Resource arbitration and execution mode selection."""

from typing import Dict


class ResourceManager:
    def select_mode(self, affect: Dict[str, float]) -> str:
        return "realtime" if affect.get("urgency", 0.5) >= 0.8 else "deliberate"
