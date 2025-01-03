﻿from abc import ABC, abstractmethod

from src.core.models.weight import Weight
from src.core.models.height import Height


class BMICalculatorStrategyBase(ABC):
    @abstractmethod
    def calculate_bmi(self, weight: Weight, height: Height) -> float:
        pass
