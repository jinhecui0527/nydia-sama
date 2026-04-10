"""Main orchestration entrypoint for NydiaSama v2."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from nydia_v2.cognition import CognitiveCore
from nydia_v2.config.settings import RuntimeSettings, load_settings
from nydia_v2.core.consciousness import ConsciousnessStream
from nydia_v2.core.identity import IdentityProfile
from nydia_v2.executive import ActionPlanner, RealtimeDriver
from nydia_v2.interface.emotional_expression import EmotionalExpression
from nydia_v2.interface.visual_interface import VisualInterface
from nydia_v2.interface.voice_interface import VoiceInterface
from nydia_v2.knowledge.knowledge_graph import KnowledgeGraph
from nydia_v2.knowledge.learning import LearningEngine
from nydia_v2.knowledge.memory_system import MemorySystem
from nydia_v2.perception import UnifiedPerceptionEngine


@dataclass
class NydiaLifeCore:
    identity: IdentityProfile = field(default_factory=IdentityProfile)
    settings: RuntimeSettings = field(default_factory=load_settings)

    def __post_init__(self) -> None:
        self.identity.name = self.settings.name
        self.consciousness = ConsciousnessStream()
        self.perception = UnifiedPerceptionEngine()
        self.cognition = CognitiveCore()
        self.executive = ActionPlanner()
        self.runtime = RealtimeDriver(interval_ms=self.settings.realtime_interval_ms)
        self.memory = MemorySystem()
        self.graph = KnowledgeGraph()
        self.learning = LearningEngine(self.graph)
        self.voice = VoiceInterface(model_name=self.settings.voice_model)
        self.visual = VisualInterface()
        self.expression = EmotionalExpression()

    def step(self, payload: Dict[str, str]) -> Dict[str, object]:
        percept = self.perception.perceive(payload)
        cog = self.cognition.process(percept)
        action = self.executive.plan(cog)

        if self.settings.loop_default == "loop" and action["loop_state"] == "once":
            action["loop_state"] = "loop"

        self.memory.remember(percept, cog, action)

        topic = cog["thought"].get("topic", "ambient")
        self.learning.internalize(topic, action["goal"])
        self.consciousness.ingest(summary=topic, salience=cog["affect"]["urgency"])

        tone = self.expression.render(cog["affect"])
        spoken = self.voice.synthesize(f"({tone}) {action['instruction']}")
        frame = self.visual.render_frame(frame_id="live")

        return {
            "identity": self.identity.snapshot(),
            "consciousness": self.consciousness.snapshot(),
            "perception": percept,
            "cognition": cog,
            "action": action,
            "voice": spoken,
            "visual": frame,
        }

    def run(self, payload: Dict[str, str], iterations: int = 3) -> dict | list[dict]:
        if self.settings.loop_default == "loop":
            return self.runtime.run_loop(lambda: self.step(payload), iterations=iterations)
        return self.runtime.run_once(lambda: self.step(payload))


def main() -> None:
    core = NydiaLifeCore()
    demo_input = {"text": "你好 Nydia! Please react in real time!", "audio": "", "visual": "avatar"}
    output = core.run(demo_input, iterations=2)
    print(output)


if __name__ == "__main__":
    main()
