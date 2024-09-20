from typing import TYPE_CHECKING, Optional
from pyglet.text import Label

from .window import get_window
from ..utils import coordinates_to_pixel, color_to_rgba_int

if TYPE_CHECKING:
    from ..visual.window import Window
    from ..types import AnchorHorizontal, AnchorVertical, ColorType


class Text(Label):
    def __init__(
        self,
        text: str = "",
        position: tuple[float, float] = (0, 0),
        width: Optional[int] = None,
        height: Optional[int] = None,
        color: Optional["ColorType"] = None,
        anchor_x: "AnchorHorizontal" = "center",
        anchor_y: "AnchorVertical" = "center",
        window: Optional["Window"] = None,
        rotation: float = 0,
        multiline: bool = False,
        font_name: Optional[str] = None,
        font_size: Optional[float] = None,
        bold: bool = False,
        italic: bool = False,
        stretch: bool = False,
        align: "AnchorHorizontal" = "center",
        **kwargs,
    ):

        self.window = window or get_window()
        x, y = coordinates_to_pixel(position, self.window, self.window)
        color = (0, 0, 0, 255) if color is None else color_to_rgba_int(color)

        super(Label, self).__init__(
            text=text,
            x=x,
            y=y,
            width=width,
            height=height,
            anchor_x=anchor_x,
            anchor_y=anchor_y,
            rotation=rotation,
            multiline=multiline,
            font_name=font_name,
            font_size=font_size,
            align=align,
            bold=bold,
            italic=italic,
            stretch=stretch,
            color=color,
            **kwargs,
        )
