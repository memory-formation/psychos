import pytest
from psychos.utils.colors import Color


@pytest.fixture
def sample_colors():
    """Fixture for creating sample colors used in tests."""
    return {
        "hex": "#32cd32",
        "hexa": "#32cd3280",  # 50% opacity
        "name": "limegreen",
        "rgb": (50 / 255, 205 / 255, 50 / 255),
        "rgba": (50 / 255, 205 / 255, 50 / 255, 0.5),
        "rgb255": (50, 205, 50),
        "rgba255": (50, 205, 50, 128),  # 50% opacity
        "hsv": (1 / 3, 0.75, 0.80),
        "cmyk": (0.76, 0.0, 3 / 4, 1 / 5),
        "yiq": (0.55, -0.16, -0.31),
        "hsl": (0.33, 0.60, 0.5),
    }


def test_color_init(sample_colors):
    """Test Color class initialization."""
    color = Color(sample_colors["hex"])
    assert color.color == sample_colors["hex"]
    assert color.space == "hex"


def test_to_rgb(sample_colors):
    """Test conversion to RGB."""
    color = Color(sample_colors["hex"])
    assert color.to_rgb() == pytest.approx(sample_colors["rgb"])


def test_to_rgba(sample_colors):
    """Test conversion to RGBA."""
    color = Color(sample_colors["hexa"])

    assert color.to_rgba() == pytest.approx(sample_colors["rgba"], abs=0.1)


def test_to_rgb255(sample_colors):
    """Test conversion to RGB255."""
    color = Color(sample_colors["hex"])
    assert color.to_rgb255() == pytest.approx(sample_colors["rgb255"])


def test_to_rgba255(sample_colors):
    """Test conversion to RGBA255."""
    color = Color(sample_colors["hexa"])
    assert color.to_rgba255() == pytest.approx(sample_colors["rgba255"])


def test_to_hex(sample_colors):
    """Test conversion to hex."""
    color = Color(sample_colors["rgb255"])
    assert color.to_hex().lower() == sample_colors["hex"].lower()


def test_to_hexa(sample_colors):
    """Test conversion to hexa."""
    color = Color(sample_colors["rgba255"], space="rgba255")

    assert color.to_hexa().lower() == sample_colors["hexa"].lower()


def test_to_name(sample_colors):
    """Test conversion to name."""
    color = Color(sample_colors["hex"])
    assert color.to_name() == sample_colors["name"]


def test_to_hsv(sample_colors):
    """Test conversion to HSV."""
    color = Color(sample_colors["hex"])
    assert color.to_hsv() == pytest.approx(sample_colors["hsv"], abs=0.1)


def test_to_cmyk(sample_colors):
    """Test conversion to CMYK."""
    color = Color(sample_colors["hex"])
    assert color.to_cmyk() == pytest.approx(sample_colors["cmyk"], abs=0.1)


def test_to_yiq(sample_colors):
    """Test conversion to YIQ."""
    color = Color(sample_colors["hex"])
    assert color.to_yiq() == pytest.approx(sample_colors["yiq"], abs=0.1)


def test_to_hsl(sample_colors):
    """Test conversion to HSL."""
    color = Color(sample_colors["hex"])
    assert color.to_hsl() == pytest.approx(sample_colors["hsl"], abs=0.1)


def test_invalid_space():
    """Test invalid color space raises a ValueError."""
    with pytest.raises(ValueError):
        Color("red", space="invalid_space")


def test_conversion_path():
    """Test finding the conversion path between color spaces."""
    color = Color("#ff5733")
    path = color._find_conversion("rgb", "hsv")
    assert isinstance(path, list)
    assert len(path) == 1


def test_direct_conversion():
    """Test a direct conversion function works."""
    color = Color("#ff5733")
    assert color.to_rgb255() == (255, 87, 51)


def test_indirect_conversion(sample_colors):
    """Test a conversion with multiple steps."""
    color = Color("#32cd32")
    assert color.to_yiq() == pytest.approx(sample_colors["yiq"], abs=0.1)
