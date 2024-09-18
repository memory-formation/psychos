from typing import Union, TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path

try:  # Compatibility with Python 3.7
    from typing import Literal  # type: ignore
except ImportError:
    from typing_extensions import Literal  # type: ignore

__all__ = ["Literal", "ColorType"]

PathStr = Union["str", "Path"]
ColorType = Union[
    "str",
    "tuple[int, int, int]",
    "tuple[int, int, int, int]",
    "tuple[float, float, float]",
    "tuple[float, float, float, float]",
]
