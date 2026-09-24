from desk.h09_extra_trap import normalize_tool, should_seed_stub
from desk.blank_tool import wants_half_stub

def test_blank_paths():
    for src in ("api", "page", "save"):
        assert normalize_tool("   ", src) in ("AUTO-TOOL", "")

def test_half_stub_armed():
    assert wants_half_stub() is True
    assert should_seed_stub("   ") is True
    assert should_seed_stub("甲刀") is False
