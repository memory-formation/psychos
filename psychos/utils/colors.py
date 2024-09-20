from typing import Optional, Tuple, Iterable
import re
import webcolors

from ..types import ColorType

__all__ = ["color_to_rgba", "color_to_rgba_int"]


def color_to_rgba(
    color: Optional["ColorType"],
) -> Optional[Tuple[float, float, float, float]]:
    """
    Normalize a color input to an RGBA tuple with float components in [0.0, 1.0].

    Args:
        color (Optional[ColorType]): The color input to normalize. Can be:
            - None: Returns None
            - str: Hex string (e.g., "#FF5733") or color name (e.g., "red")
            - Iterable with 3 or 4 numbers (ints [0,255] or floats)

    Returns:
        Optional[Tuple[float, float, float, float]]:
            Normalized RGBA tuple or None.

    Raises:
        ValueError: If the input color format is invalid or cannot be parsed.
    """
    if color is None:
        return None

    if isinstance(color, str):
        return _from_string(color)

    if isinstance(color, Iterable):
        return _from_iterable(color)

    raise ValueError(f"Unsupported color format: {color}")


def color_to_rgba_int(
    color: Optional[ColorType],
) -> Optional[Tuple[int, int, int, int]]:
    """
    Convert a color input to an RGBA tuple with integer components in [0, 255].

    This function leverages the existing `color_to_rgba` function to first normalize the color
    to RGBA floats in [0.0, 1.0], then scales these floats to integers in [0, 255].

    Args:
        color (Optional[ColorType]): The color input to normalize. Can be:
            - None: Returns None
            - str: Hex string (e.g., "#FF5733") or color name (e.g., "red")
            - Iterable with 3 or 4 numbers (ints [0,255] or floats)

    Returns:
        Optional[Tuple[int, int, int, int]]:
            Normalized RGBA tuple with integers in [0, 255], or None.

    Raises:
        ValueError: If the input color format is invalid or cannot be parsed.
    """
    rgba = color_to_rgba(color)

    if rgba is None:
        return None

    # Convert each float component to an integer in [0, 255]
    rgba_int = tuple(int(round(c * 255)) for c in rgba)

    # Ensure values are within [0, 255] to handle any floating point precision issues
    rgba_int = tuple(min(max(c, 0), 255) for c in rgba_int)

    return rgba_int


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
    try:
        rgb = webcolors.name_to_rgb(name)
        a = 255
    except ValueError:
        raise ValueError(f"Unknown color name: '{name}'")

    return (rgb.red / 255.0, rgb.green / 255.0, rgb.blue / 255.0, 1.0)


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
    else:
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
    except (TypeError, ValueError):
        raise ValueError(f"Color tuple contains non-numeric elements: {color_list}")

    if all(c <= 1.0 for c in numeric_color):
        if len(numeric_color) == 3:
            r, g, b = numeric_color
            a = 1.0
        else:
            r, g, b, a = numeric_color
        return (r, g, b, a)
    else:
        # Assume 0-255 scale
        if len(numeric_color) == 3:
            r, g, b = numeric_color
            a = 255.0
        else:
            r, g, b, a = numeric_color
        return (r / 255.0, g / 255.0, b / 255.0, a / 255.0)
