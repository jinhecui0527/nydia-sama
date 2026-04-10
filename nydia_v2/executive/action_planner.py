"""Action planning + loop/once state machine."""

from dataclasses import dataclass
from typing import Dict

from .goal_system import GoalSystem
from .resource_manager import ResourceManager


@dataclass
class LoopStateMachine:
    state: str = "once"

    def transition(self, mode: str) -> str:
        self.state = "loop" if mode == "realtime" else "once"
        return self.state


class ActionPlanner:
    def __init__(self) -> None:
        self.goals = GoalSystem()
        self.resources = ResourceManager()
        self.loop_machine = LoopStateMachine()

    def plan(self, cognition: Dict[str, object]) -> Dict[str, str]:
        thought = cognition["thought"]
        affect = cognition["affect"]
        mode = self.resources.select_mode(affect)
        loop_state = self.loop_machine.transition(mode)
        goal = self.goals.choose_goal(thought.get("topic", "ambient"))
        return {
            "goal": goal,
            "mode": mode,
            "loop_state": loop_state,
            "instruction": thought.get("intent", "respond in text"),
        }
