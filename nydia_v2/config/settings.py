"""Runtime settings loader for Nydia v2."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class RuntimeSettings:
    name: str = "Nydia"
    voice_model: str = "GPT-SoVITS"
    loop_default: str = "once"
    realtime_interval_ms: int = 100



def _parse_simple_yaml(raw: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip()
    return result



def load_settings(path: str | Path = "nydia_v2/config/default.yaml") -> RuntimeSettings:
    settings_path = Path(path)
    if not settings_path.exists():
        return RuntimeSettings()

    payload = _parse_simple_yaml(settings_path.read_text(encoding="utf-8"))
    return RuntimeSettings(
        name=payload.get("name", "Nydia"),
        voice_model=payload.get("voice_model", "GPT-SoVITS"),
        loop_default=payload.get("loop_default", "once"),
        realtime_interval_ms=int(payload.get("realtime_interval_ms", 100)),
    )
