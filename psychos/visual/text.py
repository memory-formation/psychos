from typing import Optional, Union, TYPE_CHECKING

from pyglet.text import Label

from ..utils import color_to_rgba_int
from .units import Unit, parse_height, parse_width
from .window import get_window

if TYPE_CHECKING:
    from ..visual.window import Window
    from ..types import AnchorHorizontal, AnchorVertical, ColorType, UnitType


class Text(Label):
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
        align: "AnchorHorizontal" = "center",
        rotation: float = 0,
        multiline: bool = False,
        font_name: Optional[str] = None,
        font_size: Optional[float] = None,
        bold: bool = False,
        italic: bool = False,
        stretch: bool = False,
        window: Optional["Window"] = None,
        units: Optional[Union["UnitType", "Unit"]] = None,
        **kwargs,
    ):
        # Retrieve window and set coordinate system
        self.window = window or get_window()
        if units is None:
            self.units = self.window.units
        else:
            self.units = Unit.from_name(units, window=self.window)
            
        x, y = self.units.transform(*position)

        width = parse_width(width, window=self.window)
        height = parse_height(height, window=self.window)

        # Convert color to RGBA
        color = (255, 255, 255, 255) if color is None else color_to_rgba_int(color)

        # Initialize Label (superclass)
        super().__init__(
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
            bold=bold,
            italic=italic,
            stretch=stretch,
            align=align,
            color=color,
            **kwargs,
        )

    @property
    def position(self) -> tuple[float, float]:
        """Get the position of the text."""
        return self.x, self.y

    @position.setter
    def position(self, value: tuple[float, float]):
        """Set the position of the text."""
        x, y = self.coordinate_units(*value)
        self.x = x
        self.y = y

    def draw(self) -> "Text":
        super().draw()
        return self
