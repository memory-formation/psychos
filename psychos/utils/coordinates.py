from typing import Tuple

__all__ = ["coordinates_to_pixel"]


def coordinates_to_pixel(
    normalized_coords: Tuple[float, float], width: int, height: int
) -> Tuple[int, int]:
    """
    Convert normalized coordinates (-1 to 1) to pixel coordinates based on window size.

    Args:
        normalized_coords (Tuple[float, float]): The (x, y) coordinates in normalized system.
        window_width (int): Width of the window in pixels.
        window_height (int): Height of the window in pixels.

    Returns:
        Tuple[float, float]: The (x, y) coordinates in pixel system.
    """
    normalized_x, normalized_y = normalized_coords

    # Clamp the normalized coordinates to [-1, 1]
    normalized_x = max(-1.0, min(1.0, normalized_x))
    normalized_y = max(-1.0, min(1.0, normalized_y))

    # Transform X
    x_pixel = (normalized_x + 1) / 2 * width

    # Transform Y (invert Y-axis)
    y_pixel = (1 - (normalized_y + 1) / 2) * height

    return int(x_pixel), int(y_pixel)
