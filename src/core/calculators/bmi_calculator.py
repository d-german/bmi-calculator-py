class BMICalculator:
    def __init__(self, bmi_calculator_strategy, bmi_category_interpreter):
        self._bmi_calculator_strategy = bmi_calculator_strategy
        self._bmi_category_interpreter = bmi_category_interpreter

    def calculate_bmi(self, weight, height):
        return self._bmi_calculator_strategy.calculate_bmi(weight, height)

    def get_bmi_category(self, bmi):
        return self._bmi_category_interpreter.interpret_bmi(bmi)
