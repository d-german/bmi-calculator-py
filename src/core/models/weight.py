from dataclasses import dataclass
from src.core.enums.unit_type import UnitType


@dataclass(frozen=True)
class Weight:
    value: float
    unit_type: UnitType

    def __post_init__(self):
        if self.value <= 0:
            raise ValueError("Weight value must be greater than zero.")
