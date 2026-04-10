"""Voice interface with GPT-SoVITS adapter contract."""

from dataclasses import dataclass
from typing import Protocol


class TTSAdapter(Protocol):
    def synthesize(self, text: str) -> str: ...


@dataclass
class MockSoVITSAdapter:
    model_name: str = "GPT-SoVITS"

    def synthesize(self, text: str) -> str:
        return f"[voice:{self.model_name}] {text}"


@dataclass
class VoiceInterface:
    model_name: str = "GPT-SoVITS"
    enabled: bool = False

    def __post_init__(self) -> None:
        self.adapter: TTSAdapter = MockSoVITSAdapter(self.model_name)

    def configure(self, enabled: bool = True, model_name: str | None = None) -> None:
        self.enabled = enabled
        if model_name:
            self.model_name = model_name
            self.adapter = MockSoVITSAdapter(model_name)

    def synthesize(self, text: str) -> str:
        if not self.enabled:
            return "[voice-disabled]"
        return self.adapter.synthesize(text)
