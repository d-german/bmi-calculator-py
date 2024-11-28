import pytest

from src.core.enums.unit_type import UnitType
from src.core.models.height import Height


def test_constructor_valid_input_creates_instance():
    height = Height(1.75, UnitType.Metric)
    assert height.value == 1.75
    assert height.unit_type == UnitType.Metric


def test_constructor_negative_value_throws_exception():
    with pytest.raises(ValueError):
        _ = Height(-1.75, UnitType.Metric)