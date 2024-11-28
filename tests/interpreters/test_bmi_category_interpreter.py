import pytest

from src.core.interpreters.bmi_category_interpreter import BMICategoryInterpreter


@pytest.fixture
def interpreter() -> BMICategoryInterpreter:
    return BMICategoryInterpreter()


@pytest.mark.parametrize("bmi, expected_category", [
    (17.5, "Underweight"),
    (18.5, "Normal weight"),
    (25.0, "Overweight"),
    (30.0, "Obese")
])
def test_interpret_bmi_valid_input_returns_correct_category(interpreter, bmi, expected_category) -> None:
    category = interpreter.interpret_bmi(bmi)
    assert category == expected_category
