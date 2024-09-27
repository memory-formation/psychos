"""psychos.utils.colors: Module with utility functions to handle color conversions."""

import re
from typing import Optional, Tuple, Iterable, Union, Dict

from ..types import ColorType

__all__ = ["Color"]


class Color:
    """
    A class to handle color conversions between different formats.

    Parameters
    ----------
    value : Optional[ColorType]
        The initial color value. Can be:
        - None: This sets the color to None.
        - str: A hex string (e.g., "#FF5733") or color name (e.g., "red").
        - Iterable with 3 or 4 numbers (ints [0,255] or floats).
    """

    def __init__(self, color: Optional[Union[ColorType, "Color"]] = None):
        """Initialize the Color"""
        if isinstance(color, Color):
            color = color.color

        self.color = color

    def to_rgba(self) -> Optional[Tuple[float, float, float, float]]:
        """Convert the color to an RGBA tuple with floats in [0.0, 1.0]."""
        if self.color is None:
            return None

        if isinstance(self.color, str):
            return _from_string(self.color)

        if isinstance(self.color, Iterable):
            return _from_iterable(self.color)

        raise ValueError(f"Unsupported color format: {self.color}")

    def to_rgba255(self) -> Optional[Tuple[int, int, int, int]]:
        """Convert the color to an RGBA tuple with integers in [0, 255]."""

        rgba = self.to_rgba()

        if rgba is None:
            return None

        # Convert each float component to an integer in [0, 255]
        rgba_int = tuple(int(round(c * 255)) for c in rgba)

        # Ensure values are within [0, 255] to handle any floating point precision issues
        rgba_int = tuple(min(max(c, 0), 255) for c in rgba_int)

        return rgba_int

    def to_rgb(self) -> Optional[Tuple[float, float, float]]:
        """Convert the color to an RGB tuple with floats in [0.0, 1.0]."""
        rgba = self.to_rgba()

        return None if rgba is None else rgba[:3]

    def to_rgb255(self) -> Optional[Tuple[int, int, int]]:
        """Convert the color to an RGB tuple with integers in [0, 255]."""
        rgba255 = self.to_rgba255()

        return None if rgba255 is None else rgba255[:3]

    def to_hex(self) -> Optional[str]:
        """Convert the color to a hex string."""
        rgba255 = self.to_rgba255()
        if rgba255 is None:
            return None
        r, g, b, a = rgba255
        return (
            f"#{r:02X}{g:02X}{b:02X}{a:02X}" if a < 255 else f"#{r:02X}{g:02X}{b:02X}"
        )

    def __repr__(self) -> str:
        """Return a string representation of the color."""
        return f"Color({self.color})"

    def __bool__(self) -> bool:
        """Return True if the color is not None."""
        return self.color is not None

    @classmethod
    def register_color(cls, name: str, color: ColorType) -> None:
        """Register a new color name with its value."""
        COLORS[name] = color

    @classmethod
    def list_colors(cls) -> Dict[str, str]:
        """Return a dictionary with all registered color names and values."""
        return dict(COLORS)


def _from_string(color_str: str) -> Tuple[float, float, float, float]:
    """Convert a string color (hex or name) to an RGBA tuple."""
    color_str = color_str.strip()

    # Check if it's a hex color
    hex_match = re.fullmatch(r"#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{8})", color_str)
    if hex_match:
        return _from_hex(hex_match.group(1))

    # Assume it's a color name
    return _from_color_name(color_str)


def _from_hex(hex_digits: str) -> Tuple[float, float, float, float]:
    """Convert hex digits to an RGBA tuple with floats in [0.0, 1.0]."""
    if len(hex_digits) == 6:
        r = int(hex_digits[0:2], 16)
        g = int(hex_digits[2:4], 16)
        b = int(hex_digits[4:6], 16)
        a = 255
    elif len(hex_digits) == 8:
        r = int(hex_digits[0:2], 16)
        g = int(hex_digits[2:4], 16)
        b = int(hex_digits[4:6], 16)
        a = int(hex_digits[6:8], 16)
    else:
        raise ValueError(
            f"Hex color must have 6 or 8 digits, got {len(hex_digits)} digits."
        )

    return (r / 255.0, g / 255.0, b / 255.0, a / 255.0)


def _from_color_name(name: str) -> Tuple[float, float, float, float]:
    """Convert a color name to an RGBA tuple with floats in [0.0, 1.0]."""
    name = name.lower().strip().replace(" ", "")

    hex_str = COLORS.get(name)
    if hex_str is None:
        raise ValueError(f"Unknown color name: '{name}'")

    return _from_hex(hex_str[1:])


def _from_iterable(color_iter: Iterable) -> Tuple[float, float, float, float]:
    """Convert an iterable with 3 or 4 numbers to an RGBA tuple with floats in [0.0, 1.0]."""
    color_list = list(color_iter)

    if len(color_list) not in (3, 4):
        raise ValueError(
            f"Color tuple must have 3 (RGB) or 4 (RGBA) elements, got {len(color_list)}"
        )

    # Check if all elements are integers
    if all(isinstance(c, int) for c in color_list):
        return _from_int_tuple(color_list)

    # Check if all elements are floats
    if all(isinstance(c, float) for c in color_list):
        return _from_float_tuple(color_list)

    # Handle mixed types or other numeric types
    return _from_mixed_tuple(color_list)


def _from_int_tuple(color_tuple: Tuple[int, ...]) -> Tuple[float, float, float, float]:
    """Convert an integer RGB/RGBA tuple to RGBA with floats in [0.0, 1.0]."""
    if len(color_tuple) == 3:
        r, g, b = color_tuple
        a = 255
    else:
        r, g, b, a = color_tuple

    return (r / 255.0, g / 255.0, b / 255.0, a / 255.0)


def _from_float_tuple(
    color_tuple: Tuple[float, ...]
) -> Tuple[float, float, float, float]:
    """Convert a float RGB/RGBA tuple to RGBA with floats in [0.0, 1.0]."""
    if all(c <= 1.0 for c in color_tuple):
        if len(color_tuple) == 3:
            r, g, b = color_tuple
            a = 1.0
        else:
            r, g, b, a = color_tuple
        return (r, g, b, a)

    # Assume 0-255 scale
    if len(color_tuple) == 3:
        r, g, b = color_tuple
        a = 255.0
    else:
        r, g, b, a = color_tuple
    return (r / 255.0, g / 255.0, b / 255.0, a / 255.0)


def _from_mixed_tuple(color_list: list) -> Tuple[float, float, float, float]:
    """Convert a mixed-type RGB/RGBA list to RGBA with floats in [0.0, 1.0]."""
    try:
        numeric_color = tuple(float(c) for c in color_list)
    except (TypeError, ValueError) as e:
        raise ValueError(
            f"Color tuple contains non-numeric elements: {color_list}"
        ) from e

    if all(c <= 1.0 for c in numeric_color):
        if len(numeric_color) == 3:
            r, g, b = numeric_color
            a = 1.0
        else:
            r, g, b, a = numeric_color
        return (r, g, b, a)

    # Assume 0-255 scale
    if len(numeric_color) == 3:
        r, g, b = numeric_color
        a = 255.0
    else:
        r, g, b, a = numeric_color
    return (r / 255.0, g / 255.0, b / 255.0, a / 255.0)


# The following dictionary contains the most common color names and their hex values.
# Have been taken from the package webcolors, under the BSD 3-Clause license.
# Source code: https://github.com/ubernostrum/webcolors/blob/24.8.0/src/webcolors/_definitions.py
# Copyright (c) James Bennett, and contributors. All rights reserved.
COLORS = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff",
    "blueviolet": "#8a2be2",
    "brown": "#a52a2a",
    "burlywood": "#deb887",
    "cadetblue": "#5f9ea0",
    "chartreuse": "#7fff00",
    "chocolate": "#d2691e",
    "coral": "#ff7f50",
    "cornflowerblue": "#6495ed",
    "cornsilk": "#fff8dc",
    "crimson": "#dc143c",
    "cyan": "#00ffff",
    "darkblue": "#00008b",
    "darkcyan": "#008b8b",
    "darkgoldenrod": "#b8860b",
    "darkgray": "#a9a9a9",
    "darkgreen": "#006400",
    "darkgrey": "#a9a9a9",
    "darkkhaki": "#bdb76b",
    "darkmagenta": "#8b008b",
    "darkolivegreen": "#556b2f",
    "darkorange": "#ff8c00",
    "darkorchid": "#9932cc",
    "darkred": "#8b0000",
    "darksalmon": "#e9967a",
    "darkseagreen": "#8fbc8f",
    "darkslateblue": "#483d8b",
    "darkslategray": "#2f4f4f",
    "darkslategrey": "#2f4f4f",
    "darkturquoise": "#00ced1",
    "darkviolet": "#9400d3",
    "deeppink": "#ff1493",
    "deepskyblue": "#00bfff",
    "dimgray": "#696969",
    "dimgrey": "#696969",
    "dodgerblue": "#1e90ff",
    "eigengrau": "#16161d",
    "firebrick": "#b22222",
    "floralwhite": "#fffaf0",
    "forestgreen": "#228b22",
    "fuchsia": "#ff00ff",
    "gainsboro": "#dcdcdc",
    "ghostwhite": "#f8f8ff",
    "gold": "#ffd700",
    "goldenrod": "#daa520",
    "gray": "#808080",
    "green": "#008000",
    "greenyellow": "#adff2f",
    "grey": "#808080",
    "honeydew": "#f0fff0",
    "hotpink": "#ff69b4",
    "indianred": "#cd5c5c",
    "indigo": "#4b0082",
    "ivory": "#fffff0",
    "khaki": "#f0e68c",
    "lavender": "#e6e6fa",
    "lavenderblush": "#fff0f5",
    "lawngreen": "#7cfc00",
    "lemonchiffon": "#fffacd",
    "lightblue": "#add8e6",
    "lightcoral": "#f08080",
    "lightcyan": "#e0ffff",
    "lightgoldenrodyellow": "#fafad2",
    "lightgray": "#d3d3d3",
    "lightgreen": "#90ee90",
    "lightgrey": "#d3d3d3",
    "lightpink": "#ffb6c1",
    "lightsalmon": "#ffa07a",
    "lightseagreen": "#20b2aa",
    "lightskyblue": "#87cefa",
    "lightslategray": "#778899",
    "lightslategrey": "#778899",
    "lightsteelblue": "#b0c4de",
    "lightyellow": "#ffffe0",
    "lime": "#00ff00",
    "limegreen": "#32cd32",
    "linen": "#faf0e6",
    "magenta": "#ff00ff",
    "maroon": "#800000",
    "mediumaquamarine": "#66cdaa",
    "mediumblue": "#0000cd",
    "mediumorchid": "#ba55d3",
    "mediumpurple": "#9370db",
    "mediumseagreen": "#3cb371",
    "mediumslateblue": "#7b68ee",
    "mediumspringgreen": "#00fa9a",
    "mediumturquoise": "#48d1cc",
    "mediumvioletred": "#c71585",
    "midnightblue": "#191970",
    "mintcream": "#f5fffa",
    "mistyrose": "#ffe4e1",
    "moccasin": "#ffe4b5",
    "navajowhite": "#ffdead",
    "navy": "#000080",
    "oldlace": "#fdf5e6",
    "olive": "#808000",
    "olivedrab": "#6b8e23",
    "orange": "#ffa500",
    "orangered": "#ff4500",
    "orchid": "#da70d6",
    "palegoldenrod": "#eee8aa",
    "palegreen": "#98fb98",
    "paleturquoise": "#afeeee",
    "palevioletred": "#db7093",
    "papayawhip": "#ffefd5",
    "peachpuff": "#ffdab9",
    "peru": "#cd853f",
    "pink": "#ffc0cb",
    "plum": "#dda0dd",
    "powderblue": "#b0e0e6",
    "purple": "#800080",
    "red": "#ff0000",
    "rosybrown": "#bc8f8f",
    "royalblue": "#4169e1",
    "saddlebrown": "#8b4513",
    "salmon": "#fa8072",
    "sandybrown": "#f4a460",
    "seagreen": "#2e8b57",
    "seashell": "#fff5ee",
    "sienna": "#a0522d",
    "silver": "#c0c0c0",
    "skyblue": "#87ceeb",
    "slateblue": "#6a5acd",
    "slategray": "#708090",
    "slategrey": "#708090",
    "snow": "#fffafa",
    "springgreen": "#00ff7f",
    "steelblue": "#4682b4",
    "tan": "#d2b48c",
    "teal": "#008080",
    "thistle": "#d8bfd8",
    "tomato": "#ff6347",
    "turquoise": "#40e0d0",
    "violet": "#ee82ee",
    "wheat": "#f5deb3",
    "white": "#ffffff",
    "whitesmoke": "#f5f5f5",
    "yellow": "#ffff00",
    "yellowgreen": "#9acd32",
}
