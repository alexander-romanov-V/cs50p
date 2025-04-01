"""Unittest for convert"""

import pytest
from convert import convert


def test_int_conversion():
    """Unittest of convert(int)"""
    assert convert(1) == 149597870700
    assert convert(50) == 7479893535000


def test_error():
    """Unittest of convert() argument type"""
    with pytest.raises(TypeError):
        convert("1")


def test_float_conversion():
    """Unittest of convert(float)"""
    # Can't compare float directly - only aproximately - with some tolerance
    assert convert(0.001) == pytest.approx(149597870.691)
    assert convert(0.001) == pytest.approx(149597870.691, abs=0.1)
    assert convert(0.001) == pytest.approx(149597870.691, abs=1e-2)
