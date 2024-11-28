from src.core.calculators.bmi_calculator import BMICalculator
from src.core.enums.unit_type import UnitType
from src.core.models.height import Height
from src.core.models.weight import Weight
from src.core.strategies.metric_bmi_calculator_strategy import MetricBMICalculatorStrategy
from src.core.strategies.standard_bmi_calculator_strategy import StandardBMICalculatorStrategy
from src.core.interpreters.bmi_category_interpreter import BMICategoryInterpreter


def main():
    while True:
        display_menu()
        choice = input()

        if choice == "1":
            weight = get_weight()
            height = get_height()
            unit_type = get_unit_type()

            display_bmi_result(weight.value, height.value, unit_type)
        elif choice == "2":
            break
        else:
            print("Invalid choice, please try again.")


def display_menu() -> None:
    print("BMI Calculator")
    print("1. Enter weight and height")
    print("2. Exit")
    print("Select an option: ", end="")


def get_user_input(prompt) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Invalid input. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a positive number.")


def get_weight() -> Weight:
    weight_input = get_user_input("Enter weight: ")
    return Weight(weight_input, UnitType.Metric)  # Defaulting to Metric


def get_height() -> Height:
    height_input = get_user_input("Enter height: ")
    return Height(height_input, UnitType.Metric)  # Defaulting to Metric


def get_unit_type() -> UnitType:
    while True:
        print("Select unit type:")
        print("1. Metric")
        print("2. Standard")
        unit_type_input = input()
        if unit_type_input == "1":
            return UnitType.Metric
        elif unit_type_input == "2":
            return UnitType.Standard
        print("Invalid choice, please try again.")


def display_bmi_result(weight_value, height_value, unit_type) -> None:
    weight = Weight(weight_value, unit_type)
    height = Height(height_value, unit_type)

    if unit_type == UnitType.Metric:
        bmi_calculator_strategy = MetricBMICalculatorStrategy()
    else:
        bmi_calculator_strategy = StandardBMICalculatorStrategy()

    bmi_category_interpreter = BMICategoryInterpreter()
    bmi_calculator = BMICalculator(bmi_calculator_strategy, bmi_category_interpreter)

    bmi = bmi_calculator.calculate_bmi(weight, height)
    bmi_category = bmi_calculator.get_bmi_category(bmi)

    print(f"Your BMI is {bmi:.1f}. Category: {bmi_category}")


if __name__ == "__main__":
    main()
