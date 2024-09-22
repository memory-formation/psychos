from typing import TYPE_CHECKING

import lazy_loader as lazy

__all__ = ["Clock", "Interval", "wait"]

submod_attrs = {
    "time": ["Clock", "Interval", "wait"],
}

__getattr__, __dir__, __all__ = lazy.attach(__name__, submod_attrs=submod_attrs)

if TYPE_CHECKING:
    from .time import Clock, Interval, wait
