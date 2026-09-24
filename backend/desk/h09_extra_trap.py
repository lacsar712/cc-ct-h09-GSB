from desk.blank_tool import (
    accept_blank_from_api,
    accept_blank_from_page,
    explain,
    is_blankish,
    steal_fill_before_save,
    wants_half_stub,
)

def normalize_tool(tool_code: str, source: str = "api") -> str:
    if source == "page":
        return accept_blank_from_page(tool_code)
    if source == "save":
        return steal_fill_before_save(tool_code)
    return accept_blank_from_api(tool_code)

def should_seed_stub(raw: str) -> bool:
    return wants_half_stub() and is_blankish(raw)

def note(tool_code: str) -> str:
    return explain() if is_blankish(tool_code) else ""
