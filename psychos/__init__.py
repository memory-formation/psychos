"""
psychos: A Python library for creating and managing psychology experiments.

This software is licensed under the MIT License. See the LICENSE file in the root 
directory for full license terms.

(C) 2024 DMF Research Lab. All rights reserved.
"""

from .__version__ import __version__

from typing import TYPE_CHECKING
import lazy_loader as lazy

__all__ = ["__version__", "visual", "utils", "Window", "Text"]

submodules = ["visual", "utils"]
submod_attrs = {
    "visual": ["Window", "Text"],
}

__getattr__, __dir__, __all__ = lazy.attach(
    __name__, submodules=submodules, submod_attrs=submod_attrs
)

if TYPE_CHECKING:
    from . import visual
    from . import utils

    from .visual import Window, Text
