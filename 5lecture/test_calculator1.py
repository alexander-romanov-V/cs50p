"""Unit test calculator's functions with 'pytest'"""

from calculator import square

# pip install pytest
# run test: pytest test_calculator.py
# tests will be stopped on FIRST assert 

def test_square():
    """Unit test square() function"""
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
