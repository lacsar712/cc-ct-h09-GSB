"""H09 fixed: 归一化只做 trim；空刀号由 API 在写入前挡回。

不再 seed 半截空行，不再把空刀号改写成自动代名。
"""

from desk.blank_tool import is_blankish, normalize_tool_code


def normalize_tool(tool_code: str, source: str = "api") -> str:
    """各来源统一只 trim；空刀号原样返回空串，由 API 挡回。"""
    return normalize_tool_code(tool_code)


def should_seed_stub(raw: str) -> bool:
    """已拆除：任何输入都不再触发半截空行。"""
    return False


def note(tool_code: str) -> str:
    return ""
