import math
import pytest
from calculator.core import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 7) == 3

def test_multiply():
    assert multiply(1.5, 4) == 6.0

def test_divide_basic():
    assert divide(9, 3) == 3

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

def test_float_precision():
    assert math.isclose(add(0.1, 0.2), 0.3, rel_tol=1e-9, abs_tol=1e-12)
