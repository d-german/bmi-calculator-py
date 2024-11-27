from abc import ABC, abstractmethod


class IBMICategoryInterpreter(ABC):
    @abstractmethod
    def interpret_bmi(self, bmi: float) -> str:
        pass
