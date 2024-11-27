from src.core.interfaces.bmi_category_interpreter_base import BMICategoryInterpreterBase


class BMICategoryInterpreter(BMICategoryInterpreterBase):
    def interpret_bmi(self, bmi: float) -> str:
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 24.9 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"
