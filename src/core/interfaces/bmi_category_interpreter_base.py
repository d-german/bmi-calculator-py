from abc import ABC, abstractmethod


class BMICategoryInterpreterBase(ABC):
    @abstractmethod
    def interpret_bmi(self, bmi: float) -> str:
        pass
