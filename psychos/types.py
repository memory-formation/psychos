"""pychos.types: Type hints and aliases for the psychos package."""

from typing import Union, Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path

__all__ = [
    "Literal",
    "ColorType",
    "AnchorHorizontal",
    "AnchorVertical",
    "PathStr",
    "UnitType",
    "UnitTransformation",
]

PathStr = Union["str", "Path"]

ColorType = Union[
    "str",
    "tuple[int, int, int]",
    "tuple[int, int, int, int]",
    "tuple[float, float, float]",
    "tuple[float, float, float, float]",
]

# Anchor types for alignment
AnchorHorizontal = Literal["left", "center", "right"]
AnchorVertical = Literal["top", "center", "bottom", "baseline"]

# Unit types
UnitType = Literal["px", "norm", "%", "vw", "vh", "vd", "cm", "mm", "in", "pt", "deg"]
UnitTransformation = Literal[
    "transform", "inverse_transform", "transform_size", "inverse_transform_size"
]
