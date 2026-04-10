"""Visual pipeline for green-screen keying and Y-axis compensation."""

from dataclasses import dataclass


@dataclass
class VisualInterface:
    chroma_key_enabled: bool = True
    y_axis_compensation: float = 0.0

    def set_y_compensation(self, value: float) -> None:
        self.y_axis_compensation = value

    def render_frame(self, frame_id: str) -> dict:
        return {
            "frame_id": frame_id,
            "chroma_key": "applied" if self.chroma_key_enabled else "disabled",
            "y_axis_compensation": self.y_axis_compensation,
        }
