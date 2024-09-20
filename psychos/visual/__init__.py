from typing import TYPE_CHECKING
import lazy_loader as lazy

submod_attrs = {
    "window": ["Window", "get_window"],
    "text": ["Text"],
}

__getattr__, __dir__, __all__ = lazy.attach(__name__, submod_attrs=submod_attrs)

if TYPE_CHECKING:
    from .window import Window
    from .text import Text

__all__ = ["Window", "Text", "get_window"]
