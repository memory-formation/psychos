from typing import Optional, Union, TYPE_CHECKING

import pyglet
from pyglet.window import Window as PygletWindow

from .units import Unit, parse_height, parse_width
from ..utils import color_to_rgba
from ..core.time import wait

if TYPE_CHECKING:
    from ..types import ColorType, UnitType

__all__ = ["Window", "get_window"]


def get_window() -> "Window":
    """
    Retrieve the current default window.

    Returns
    -------
    Window
        The current default window.

    Raises
    ------
    RuntimeError
        If no window has been created yet.
    """
    windows = list(pyglet.app.windows)
    if not windows:
        raise RuntimeError("No window has been created yet.")
    return windows[0]


class Window(PygletWindow):
    """
    A custom Pyglet window class with additional functionality for handling units,
    background color, and event management.

    Parameters
    ----------
    width : Optional[int], default=None
        The width of the window in pixels or another unit type. If None, the default width is used.
    height : Optional[int], default=None
        The height of the window in pixels or another unit type. If None, the default height is used.
    caption : Optional[str], default=None
        The caption or title of the window.
    fullscreen : bool, default=False
        Whether the window should be displayed in fullscreen mode.
    visible : bool, default=True
        Whether the window is visible upon creation.
    background_color : Optional[ColorType], default=None
        The background color of the window as an RGB or RGBA tuple, or a string representing a named color.
    mouse_visible : bool, default=False
        Whether the mouse cursor should be visible in the window.
    units : Union[UnitType, Unit], default="norm"
        The unit system to be used in the window. Can be a string or a Unit object to define how coordinates and sizes are managed.
    distance : Optional[float], default=50
        The viewing distance of the window in centimeters, used to calculate visual angles (e.g., degrees).
    inches : Optional[float], default=None
        The diagonal size of the monitor in inches. This is required for accurate DPI (dots per inch) and physical size calculations.
    clear_after_flip : bool, default=True
        Whether the window should be cleared after flipping the frame buffer, preparing it for the next frame.
    kwargs : dict
        Additional keyword arguments passed to the Pyglet window constructor.

    Attributes
    ----------
    distance : float
        The distance from the viewer to the screen in centimeters, used for certain units like degrees of visual angle.
    inches : float
        The diagonal size of the monitor in inches, used to compute DPI.
    clear_after_flip : bool
        Whether the window will be cleared automatically after each frame flip.
    units : Unit
        The current unit system for the window, used to convert between different coordinate and size units.
    background_color : Optional[ColorType]
        The background color of the window, stored as an RGBA tuple.
    dpi : float
        The calculated dots per inch (DPI) of the screen based on the monitor's diagonal size.
    """

    def __init__(
        self,
        width: Optional[int] = None,
        height: Optional[int] = None,
        caption: Optional[str] = None,
        fullscreen: bool = False,
        visible: bool = True,
        background_color: Optional["ColorType"] = None,
        mouse_visible: bool = False,
        units: Union["UnitType", "Unit"] = "norm",
        distance: Optional[float] = 50,
        inches: Optional[float] = None,
        clear_after_flip: bool = True,
        **kwargs,
    ):
        super().__init__(
            caption=caption,
            fullscreen=fullscreen,
            visible=visible,
            **kwargs,
        )

        self.distance = distance
        self.inches = inches
        if not self.fullscreen and height is not None:
            self.height = parse_height(height, window=self)
        if not self.fullscreen and width is not None:
            self.width = parse_width(width, window=self)
        self.clear_after_flip = clear_after_flip

        self.units = Unit.from_name(units, window=self)
        self.set_background_color(background_color)
        self.set_mouse_visible(mouse_visible)
        self.dispatch_events()

    def set_background_color(self, color: Optional["ColorType"]) -> None:
        """
        Set the background color of the window.

        Parameters
        ----------
        color : Optional[ColorType]
            The background color as a tuple (r, g, b, a) or a color name.
        """
        self.background_color = color_to_rgba(color)
        if self.background_color is not None:
            pyglet.gl.glClearColor(*self.background_color)  # Set the OpenGL clear color
            self.clear()  # Clear the window with the new background color

    @property
    def dpi(self) -> float:
        """
        Get the number of pixels per centimeter in the window, computed from the monitor's diagonal size in inches.

        Returns
        -------
        float
            The number of pixels per centimeter.
        """
        if not self.inches:
            raise ValueError(
                "The diagonal size in inches must be set to calculate DPI. "
                "Specify `inches` to the window constructor."
            )

        # Calculate diagonal resolution in pixels
        diagonal_pixels = (self.screen.width**2 + self.screen.height**2) ** 0.5

        # Calculate pixels per inch (DPI)
        dpi = diagonal_pixels / self.inches

        # Convert DPI to pixels per centimeter
        return dpi

    def wait(
        self, duration: float = 1, sleep_interval: float = 0.8, hog_period: float = 0.02
    ):
        """
        Wait for a specified duration while dispatching window events.

        Parameters
        ----------
        duration : float, default=1
            The duration to wait in seconds.
        sleep_interval : float, default=0.8
            The interval to sleep between event dispatches.
        hog_period : float, default=0.02
            The period to hog the CPU at the end of the wait. This is do to
            increase the accuracy of the wait time.
        """
        wait(duration=duration, sleep_interval=sleep_interval, hog_period=hog_period)

    def flip(self, clear: Optional[bool] = None) -> "Window":
        """
        Flip the window's frame buffer and optionally clear the window after.

        Parameters
        ----------
        clear : Optional[bool], default=None
            Whether to clear the window after flipping. Defaults to the value of
            `self.clear_after_flip`.
        """
        super().flip()

        clear = clear if clear is not None else self.clear_after_flip
        if clear:
            self.clear()

        return self
