from typing import Optional, Union, TYPE_CHECKING

import pyglet
from pyglet.window import Window as PygletWindow

from .units import Units
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
        The width of the window in pixels.
    height : Optional[int], default=None
        The height of the window in pixels.
    caption : Optional[str], default=None
        The caption or title of the window.
    fullscreen : bool, default=False
        Whether the window should be displayed in fullscreen mode.
    visible : bool, default=True
        Whether the window is visible upon creation.
    clear_after_flip : bool, default=True
        Whether the window should be cleared after flipping the frame buffer.
    background_color : Optional[ColorType], default=None
        The background color of the window.
    mouse_visible : bool, default=True
        Whether the mouse cursor should be visible in the window.
    default_window : bool, default=True
        Whether this window should be set as the default window globally.
    units : Union[UnitType, Units], default="normalized"
        The unit system to be used in the window. Can be a string or a Units object.
    kwargs : dict
        Additional keyword arguments passed to the Pyglet window constructor.

    Attributes
    ----------
    background_color : Optional[ColorType]
        The background color of the window.
    clear_after_flip : bool
        Whether the window should clear its content after each flip.
    units : Units
        The unit system used for transforming coordinates in the window.
    """

    def __init__(
        self,
        width: Optional[int] = None,
        height: Optional[int] = None,
        caption: Optional[str] = None,
        fullscreen: bool = False,
        visible: bool = True,
        clear_after_flip: bool = True,
        background_color: Optional["ColorType"] = None,
        mouse_visible: bool = True,
        units: Union["UnitType", "Units"] = "normalized",
        **kwargs,
    ):
        super().__init__(
            width=width,
            height=height,
            caption=caption,
            fullscreen=fullscreen,
            visible=visible,
            **kwargs,
        )

        self.clear_after_flip = clear_after_flip
        self.background_color = None
        self.set_background_color(background_color)
        if not mouse_visible:
            self.set_mouse_visible(mouse_visible)
        if isinstance(units, str):
            units = Units.from_name(units, self)

        self.units = units

        self.dispatch_events()

    def set_background_color(self, color: Optional["ColorType"]) -> None:
        """
        Set the background color of the window.

        Parameters
        ----------
        color : Optional[ColorType]
            The background color as a tuple (r, g, b, a) or a color name.
        """
        color = color_to_rgba(color)

        if color is not None:
            self.background_color = color
            pyglet.gl.glClearColor(*color)  # Set the OpenGL clear color
            self.clear()  # Clear the window with the new background color

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
