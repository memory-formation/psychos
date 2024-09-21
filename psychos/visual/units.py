from abc import ABC, abstractmethod
from typing import Tuple, Dict, Type, TYPE_CHECKING, Optional

from ..utils.decorators import docstring

if TYPE_CHECKING:
    from psychos.visual.window import Window


UNIT_SYSTEMS: Dict[str, Type["Units"]] = {}


class Units(ABC):
    """
    Abstract base class for different unit systems that transform
    normalized or other unit types into pixel values.
    """

    @classmethod
    def from_name(cls, name: str, window: "Window") -> "Units":
        """
        Instantiate a unit system class by name.

        Parameters
        ----------
        name : str
            The name of the unit system.
        window : Window
            The window object, used to get the size for the transformation.

        Returns
        -------
        Units
            An instance of the unit system class.
        """
        unit_cls = UNIT_SYSTEMS.get(name)
        if unit_cls is None:
            raise ValueError(
                f"Unknown unit system: {name}. "
                f"Available systems: {list(UNIT_SYSTEMS.keys())}"
            )
        return unit_cls.from_window(window)

    @abstractmethod
    def from_window(cls, window: "Window") -> "Units":
        """
        Create an instance of the unit system based on the window dimensions.

        Parameters
        ----------
        window : Window
            The window object used to retrieve dimensions.

        Returns
        -------
        Units
            The appropriate unit transformation object.
        """
        ...

    @abstractmethod
    def __call__(self, x, y) -> Tuple[int, int]:
        """
        Convert units to pixel values.

        Parameters
        ----------
        x : float
            The x-coordinate.
        y : float
            The y-coordinate.

        Returns
        -------
        tuple[int, int]
            The pixel coordinates.
        """
        ...


def units(name: str):
    """
    Decorator to register a unit system class under a specific name.

    Parameters
    ----------
    name : str
        The name to register the unit system class under.

    Returns
    -------
    function
        A decorator function to register the unit system class.
    """

    def decorator(cls):
        UNIT_SYSTEMS[name] = cls
        return cls

    return decorator


@units("pixel")
class PixelUnits(Units):
    """
    Pixel unit system.

    This class is a no-op, as Pyglet uses pixel units by default.
    """

    @docstring(Units.from_window)
    @classmethod
    def from_window(cls, window: Optional["Window"] = None) -> "Units":
        return cls()

    @docstring(Units.__call__)
    def __call__(self, x: float, y: float) -> Tuple[int, int]:
        return int(x), int(y)


@units("normalized")
class NormalizedUnits(Units):
    """
    Normalized unit system.

    - (1, 1) is the top-right corner of the window.
    - (-1, -1) is the bottom-left corner of the window.
    - (0, 0) is the center of the window.
    - (-1, 1) is the top-left corner of the window.
    - (1, -1) is the bottom-right corner of the window.
    """

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    @docstring(Units.from_window)
    @classmethod
    def from_window(cls, window: "Window") -> "Units":
        return cls(width=window.width, height=window.height)

    @docstring(Units.__call__)
    def __call__(self, x: float, y: float) -> Tuple[int, int]:
        x_pixel = int((x + 1) * self.width / 2)
        x_pixel = min(max(x_pixel, 0), self.width - 1)
        y_pixel = int((1 - y) * self.height / 2)
        y_pixel = min(max(y_pixel, 0), self.height - 1)

        return x_pixel, y_pixel
