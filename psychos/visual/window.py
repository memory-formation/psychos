from typing import Optional, Union

import pyglet
from pyglet.app import EventLoop
from pyglet.window import Window as PygletWindow

from .units import Units
from ..utils import color_to_rgba
from ..types import ColorType, UnitType

__all__ = ["Window", "get_window"]

DEFAULT_WINDOW = None


def get_window() -> "Window":

    if DEFAULT_WINDOW is None:
        raise ValueError("No window has been created yet.")
    return DEFAULT_WINDOW


class Window(PygletWindow):
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
        event_loop: Optional["EventLoop"] = None,
        default_window: bool = True,
        units: Union[UnitType, "Units"] = "normalized",
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

        self.event_loop = event_loop or EventLoop()
        self.background_color = None
        self.set_background_color(background_color)
        self.clear_after_flip = clear_after_flip
        if not mouse_visible:
            self.set_mouse_visible(mouse_visible)

        self.dispatch_events()

        if isinstance(units, str):
            units = Units.from_name(units, self)

        self.units = units

        if default_window:
            global DEFAULT_WINDOW
            DEFAULT_WINDOW = self

    def set_background_color(self, color: Optional[ColorType]) -> None:
        """Set the background color of the window."""
        color = color_to_rgba(color)

        if color is not None:
            self.background_color = color
            pyglet.gl.glClearColor(*color)  # Set the OpenGL clear color
            self.clear()  # Clear the window with the new background color

    def wait(self, timeout: float = 1):
        self.dispatch_events()
        self.event_loop.sleep(timeout)
        self.dispatch_events()

    def flip(self, clear: Optional[bool] = None):
        super().flip()

        clear = clear if clear is not None else self.clear_after_flip
        if clear:
            self.clear()
