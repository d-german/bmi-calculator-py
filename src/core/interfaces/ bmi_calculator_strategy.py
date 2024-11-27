from abc import ABC, abstractmethod
from src.core.models.height import Height


class IBMICalculatorStrategy(ABC):
    @abstractmethod
    def calculate_bmi(self, weight: Weight, height: Height) -> float:
        pass