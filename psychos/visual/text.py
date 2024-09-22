from typing import TYPE_CHECKING, Optional, Union
from pyglet.text import Label

from .window import get_window
from ..utils import color_to_rgba_int
from .units import Units

if TYPE_CHECKING:
    from ..visual.window import Window
    from ..types import AnchorHorizontal, AnchorVertical, ColorType, UnitType


class Text:
    """
    A class to represent text in a Pyglet window using a Label component.

    Parameters
    ----------
    text : str, default=""
        The text to display.
    position : tuple[float, float], default=(0, 0)
        The position of the text in the window.
    width : Optional[int], default=None
        The width of the text box.
    height : Optional[int], default=None
        The height of the text box.
    color : Optional[ColorType], default=None
        The color of the text.
    anchor_x : AnchorHorizontal, default="center"
        The horizontal anchor alignment of the text.
    anchor_y : AnchorVertical, default="center"
        The vertical anchor alignment of the text.
    window : Optional[Window], default=None
        The window in which the text will be displayed.
    rotation : float, default=0
        The rotation angle of the text.
    multiline : bool, default=False
        Whether the text can span multiple lines.
    font_name : Optional[str], default=None
        The name of the font to use.
    font_size : Optional[float], default=None
        The size of the font to use.
    bold : bool, default=False
        Whether the text is bold.
    italic : bool, default=False
        Whether the text is italicized.
    stretch : bool, default=False
        Whether the text is stretched.
    align : AnchorHorizontal, default="center"
        The alignment of the text.
    coordinate_units : Optional[Union[UnitType, Units]], default=None
        The unit system to be used for positioning the text.
    kwargs : dict
        Additional keyword arguments to pass to the Pyglet Label.
    """

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
        coordinate_units: Optional[Union["UnitType", "Units"]] = None,
        **kwargs,
    ):

        self.window = window or get_window()

        if coordinate_units is not None:
            if isinstance(coordinate_units, str):
                coordinate_units = Units.from_name(coordinate_units, self.window)
        else:
            coordinate_units = self.window.units

        self.coordinate_units = coordinate_units
        x, y = self.coordinate_units(*position)
        color = (255, 255, 255, 255) if color is None else color_to_rgba_int(color)

        # Instantiate the internal Label component
        self.component = Label(
            text,
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

    def draw(self):
        """Draw the text component."""
        self.component.draw()

    @property
    def text(self) -> str:
        """Get the current text."""
        return self.component.text

    @text.setter
    def text(self, value: str):
        """Set the current text."""
        self.component.text = value

    @property
    def position(self) -> tuple[float, float]:
        """Get the position of the text."""
        return self.component.x, self.component.y

    @position.setter
    def position(self, value: tuple[float, float]):
        """Set the position of the text."""
        x, y = self.coordinate_units(*value)
        self.component.x = x
        self.component.y = y

    @property
    def color(self) -> tuple[int, int, int, int]:
        """Get the color of the text."""
        return self.component.color

    @color.setter
    def color(self, value: Optional["ColorType"]):
        """Set the color of the text."""
        self.component.color = color_to_rgba_int(value)

    @property
    def font_name(self) -> str:
        """Get the font name."""
        return self.component.font_name

    @font_name.setter
    def font_name(self, value: str):
        """Set the font name."""
        self.component.font_name = value

    @property
    def font_size(self) -> float:
        """Get the font size."""
        return self.component.font_size

    @font_size.setter
    def font_size(self, value: float):
        """Set the font size."""
        self.component.font_size = value
