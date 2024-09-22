from typing import TYPE_CHECKING

from ..utils.lazy import attach

submod_attrs = {
    "time": ["Clock", "Interval", "wait"],
}

__getattr__, __dir__, __all__ = attach(__name__, submod_attrs=submod_attrs)

if TYPE_CHECKING:
    __all__ = ["Clock", "Interval", "wait"]
    from .time import Clock, Interval, wait
