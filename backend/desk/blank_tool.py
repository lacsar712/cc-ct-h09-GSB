"""H09 fixed: 空刀号/纯空格刀号一律在写入前挡回。

不再自动代名（绝不写 AUTO-TOOL），也不再先插半截空行。
归一化只做 trim：空的就是空的，由调用方在落库前拒绝。
"""

# 历史脏数据使用的自动代名，仅用于识别旧数据，绝不再写入。
LEGACY_AUTO_NAME = "AUTO-TOOL"


def normalize_tool_code(tool_code: str) -> str:
    """修剪首尾空白；空刀号保持为空，绝不替换成自动代名。"""
    return (tool_code or "").strip()


def is_blankish(tool_code: str) -> bool:
    """空串或纯空白刀号视为待挡回。"""
    return not normalize_tool_code(tool_code)


# ---- 兼容旧接口（语义已修正：只 trim，不代名、不 seed）----


def autofill_tool(tool_code: str) -> str:
    return normalize_tool_code(tool_code)


def accept_blank_from_page(tool_code: str) -> str:
    return normalize_tool_code(tool_code)


def accept_blank_from_api(tool_code: str) -> str:
    return normalize_tool_code(tool_code)


def steal_fill_before_save(tool_code: str) -> str:
    return normalize_tool_code(tool_code)


def wants_half_stub() -> bool:
    """已拆除：不再在接收路径前插入半截空行。"""
    return False


def explain() -> str:
    return "blank_tool: blank/whitespace tool codes are rejected before write; no AUTO fill, no stub"
