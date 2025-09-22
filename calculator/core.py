"""Basic calculator core functions.

Provides simple, well-typed arithmetic helpers used by the CLI and tests.
"""
from __future__ import annotations

from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> float:
    """Return the sum of a and b as a float."""
    return float(a) + float(b)


def subtract(a: Number, b: Number) -> float:
    """Return a minus b as a float."""
    return float(a) - float(b)


def multiply(a: Number, b: Number) -> float:
    """Return the product of a and b as a float."""
    return float(a) * float(b)


def divide(a: Number, b: Number) -> float:
    """Return a divided by b as a float.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    b_f = float(b)
    if b_f == 0.0:
        raise ZeroDivisionError("division by zero")
    return float(a) / b_f
