from typing import TYPE_CHECKING
import lazy_loader as lazy

submod_attrs={
    "window": ["Window"],
}

__getattr__, __dir__, __all__ = lazy.attach(__name__, submod_attrs=submod_attrs)

if TYPE_CHECKING:
    from .window import Window

__all__ = ["Window"]