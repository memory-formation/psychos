"""psychos.visual: Module for creating visual elements in a Pyglet window."""

from typing import TYPE_CHECKING

from ..utils.lazy import attach

submod_attrs = {
    "window": ["Window", "get_window"],
    "text": ["Text"],
    "image": ["Image"],
    "units": ["Unit"],
}

__getattr__, __dir__, __all__ = attach(__name__, submod_attrs=submod_attrs)

if TYPE_CHECKING:
    __all__ = ["Window", "Image", "Text", "get_window", "Unit"]

    from .window import Window, get_window
    from .text import Text
    from .image import Image
    from .units import Unit
