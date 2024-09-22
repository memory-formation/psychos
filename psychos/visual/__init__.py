from typing import TYPE_CHECKING

from ..utils.lazy import attach

submod_attrs = {
    "window": ["Window", "get_window"],
    "text": ["Text"],
}

__getattr__, __dir__, __all__ = attach(__name__, submod_attrs=submod_attrs)

if TYPE_CHECKING:
    __all__ = ["Window", "Text", "get_window"]

    from .window import Window
    from .text import Text
