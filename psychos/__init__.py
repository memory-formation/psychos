"""
psychos: A Python library for creating and managing psychology experiments.

This software is licensed under the MIT License. See the LICENSE file in the root 
directory for full license terms.

(C) 2024 DMF Research Lab. All rights reserved.
"""

from typing import TYPE_CHECKING

from .__version__ import __version__
from .utils.lazy import attach


submodules = ["visual", "utils", "core"]
submod_attrs = {
    "visual": ["Window", "get_window", "Text", "Image"],
}

__getattr__, __dir__, __all__ = attach(
    __name__, submodules=submodules, submod_attrs=submod_attrs
)

__all__ += ["__version__"]

if TYPE_CHECKING:
    __all__ = ["__version__", "visual", "utils", "core", "Window", "Text", "Image"]

    from . import visual
    from . import utils
    from . import core

    from .visual import Window, Text, Image
