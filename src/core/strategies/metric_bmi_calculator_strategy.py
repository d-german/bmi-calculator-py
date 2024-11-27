from src.core.enums.unit_type import UnitType
from src.core.exceptions.invalid_operation_exception import InvalidOperationException
from src.core.models.height import Height
from src.core.models.weight import Weight
from src.core.interfaces.bmi_calculator_strategy_base import BMICalculatorStrategyBase


class MetricBMICalculatorStrategy(BMICalculatorStrategyBase):
    def calculate_bmi(self, weight: Weight, height: Height) -> float:
        # Ensure the units are metric, otherwise throw an exception
        if weight.unit_type != UnitType.Metric or height.unit_type != UnitType.Metric:
            raise InvalidOperationException("Both weight and height units must be metric.")

        return weight.value / (height.value * height.value)
