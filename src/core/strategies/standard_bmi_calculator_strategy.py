from src.core.enums.unit_type import UnitType
from src.core.exceptions.invalid_operation_exception import InvalidOperationException
from src.core.models.height import Height
from src.core.models.weight import Weight
from src.core.interfaces.bmi_calculator_strategy_base import BMICalculatorStrategyBase


class StandardBMICalculatorStrategy(BMICalculatorStrategyBase):
    def calculate_bmi(self, weight: Weight, height: Height) -> float:
        # Ensure the units are standard, otherwise throw an exception
        if weight.unit_type != UnitType.Standard or height.unit_type != UnitType.Standard:
            raise InvalidOperationException("Both weight and height units must be standard.")

        height_in_inches = height.value
        weight_in_lbs = weight.value
        bmi = (weight_in_lbs / (height_in_inches * height_in_inches)) * 703

        return bmi
