from typing import TYPE_CHECKING

from .lazy import attach

submod_attrs = {
    "colors": ["color_to_rgba", "color_to_rgba_int"],
    "decorators": ["docstring", "register"],
}

__getattr__, __dir__, __all__ = attach(__name__, submod_attrs=submod_attrs)

if TYPE_CHECKING:
    __all__ = ["color_to_rgba", "color_to_rgba_int", "docstring", "register"]

    from .colors import color_to_rgba, color_to_rgba_int
    from .decorators import docstring, register
