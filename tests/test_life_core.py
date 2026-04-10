from nydia_v2.config.settings import RuntimeSettings
from nydia_v2.core.life_core import NydiaLifeCore


def test_full_pipeline_generates_expected_sections():
    core = NydiaLifeCore()
    result = core.step({"text": "Thanks for helping!", "audio": "", "visual": "scene"})

    assert set(["identity", "consciousness", "perception", "cognition", "action", "voice", "visual"]).issubset(result.keys())
    assert result["action"]["loop_state"] in {"once", "loop"}


def test_realtime_switches_loop_state():
    core = NydiaLifeCore()
    result = core.step({"text": "urgent!", "audio": "a", "visual": ""})
    assert result["action"]["loop_state"] == "loop"


def test_run_respects_loop_default_setting():
    core = NydiaLifeCore(settings=RuntimeSettings(loop_default="loop", realtime_interval_ms=1))
    outputs = core.run({"text": "normal", "audio": "", "visual": ""}, iterations=2)

    assert isinstance(outputs, list)
    assert len(outputs) == 2
    assert all(item["action"]["loop_state"] == "loop" for item in outputs)
