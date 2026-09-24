"""H09: autofill blank tool; may seed empty stub before AUTO fill."""

AUTO = "AUTO-TOOL"

def autofill_tool(tool_code: str) -> str:
    s = (tool_code or "").strip()
    return s if s else AUTO

def accept_blank_from_page(tool_code: str) -> str:
    return autofill_tool(tool_code)

def accept_blank_from_api(tool_code: str) -> str:
    return autofill_tool(tool_code)

def steal_fill_before_save(tool_code: str) -> str:
    return autofill_tool(tool_code)

def is_blankish(tool_code: str) -> bool:
    return not (tool_code or "").strip()

def wants_half_stub() -> bool:
    """BUG: insert an empty stub row before the AUTO-TOOL accept path."""
    return True

def explain() -> str:
    return "blank_tool: page/api/save autofill AUTO-TOOL + half stub"
