"""Unit test calculator's functions with 'pytest'"""

import pytest
from calculator import square

# pip install pytest
# run test: pytest test_calculator.py
# try separate all asserts - all functions will be run separately
# tests will be stopped on FIRST assert for EACH function
# add typechek


def test_positive():
    """Unit test square() function for positive numbers"""
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    """Unit test square() function for negative numbers"""
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    """Unit test square() function for zero"""
    assert square(0) == 0


def test_str():
    """Unit test square() function for str type"""
    # Check what we will get an TypeError exception if passes str argumet
    with pytest.raises(TypeError):
        square("cat")
