from typing import Optional

from pyglet.app import EventLoop
from pyglet.gl import glClearColor
from pyglet.window import Window as PygletWindow

from ..utils import color_to_rgba
from ..types import ColorType


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
        mouse_visible: bool = False,
        event_loop: Optional["EventLoop"] = None,
        **kwargs
    ):
        super().__init__(
            width=width,
            height=height,
            caption=caption,
            fullscreen=fullscreen,
            visible=visible,
            **kwargs
        )
        self.event_loop = event_loop or EventLoop()
        self.background_color = None
        self.set_background_color(background_color)
        self.clear_after_flip = clear_after_flip
        if not mouse_visible:
            self.set_mouse_visible(mouse_visible)

    def set_background_color(self, color: Optional[ColorType]) -> None:
        """Set the background color of the window."""
        color = color_to_rgba(color)

        if color is not None:
            self.background_color = color
            glClearColor(*color)  # Set the OpenGL clear color
            self.clear()  # Clear the window with the new background color

    def wait(self, timeout: float = 1):
        self.event_loop.sleep(timeout)

    def flip(self, clear: Optional[bool] = None):
        super().flip()

        clear = clear if clear is not None else self.clear_after_flip
        if clear:
            self.clear()
