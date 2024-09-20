from typing import TYPE_CHECKING

import lazy_loader as lazy

__all__ = ["color_to_rgba", "color_to_rgba_int"]

submod_attrs = {
    "colors": ["color_to_rgba", "color_to_rgba_int"],
    "coordinates": ["coordinates_to_pixel"],
}

__getattr__, __dir__, __all__ = lazy.attach(__name__, submod_attrs=submod_attrs)

if TYPE_CHECKING:
    from .colors import color_to_rgba, color_to_rgba_int
    from .coordinates import coordinates_to_pixel