import pytest
from math import isclose
from psychos.utils.colors import Color


# Helper function for close float comparisons
def is_close_tuple(t1, t2, tol=1e-6):
    return all(isclose(a, b, abs_tol=tol) for a, b in zip(t1, t2))


def test_color_initialization():
    # Test None input
    color = Color()
    assert color.color is None
    assert color.to_rgba() is None
    assert color.to_rgb() is None
    assert color.to_rgba255() is None
    assert color.to_rgb255() is None
    assert color.to_hex() is None

    # Test string input (hex color)
    color = Color("#FF5733")
    assert is_close_tuple(color.to_rgba(), (1.0, 0.341176, 0.2, 1.0))
    assert is_close_tuple(color.to_rgb(), (1.0, 0.341176, 0.2))
    assert color.to_rgba255() == (255, 87, 51, 255)
    assert color.to_rgb255() == (255, 87, 51)
    assert color.to_hex() == "#FF5733"

    # Test string input (named color)
    color = Color("blue")
    assert is_close_tuple(color.to_rgba(), (0.0, 0.0, 1.0, 1.0))
    assert color.to_hex() == "#0000FF"

    # Test iterable input (RGB tuple)
    color = Color((255, 0, 255))
    assert is_close_tuple(color.to_rgba(), (1.0, 0.0, 1.0, 1.0))
    assert is_close_tuple(color.to_rgb(), (1.0, 0.0, 1.0))
    assert color.to_rgba255() == (255, 0, 255, 255)
    assert color.to_rgb255() == (255, 0, 255)
    assert color.to_hex() == "#FF00FF"

    # Test iterable input (RGBA float)
    color = Color((0.5, 0.5, 0.5, 0.5))
    assert is_close_tuple(color.to_rgba(), (0.5, 0.5, 0.5, 0.5))
    assert is_close_tuple(color.to_rgb(), (0.5, 0.5, 0.5))
    assert color.to_rgba255() == (128, 128, 128, 128)
    assert color.to_rgb255() == (128, 128, 128)
    assert color.to_hex() == "#80808080"


def test_invalid_color_inputs():
    with pytest.raises(ValueError):
        Color("invalid_color").to_rgba()

    with pytest.raises(ValueError):
        Color("123456").to_rgba()

    with pytest.raises(ValueError):
        Color((0.5, 0.5, "string")).to_rgba()


def test_color_repr():
    color = Color("red")
    assert repr(color) == "Color(red)"


def test_color_register_list():
    # Test color registration and listing
    Color.register_color("mycolor", "#123456")
    assert Color.list_colors()["mycolor"] == "#123456"


def test_copy_constructor():
    # Test initializing Color with another Color instance
    original = Color("#FF5733")
    copy_color = Color(original)
    assert copy_color.color == original.color
    assert is_close_tuple(copy_color.to_rgba(), original.to_rgba())


def test_boolean_evaluation():
    assert bool(Color(None)) is False
    assert bool(Color("red")) is True
