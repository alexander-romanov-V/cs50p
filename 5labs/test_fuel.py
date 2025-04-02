"""Unittest for Fuel Gauge - Refueling"""

import pytest
from fuel import convert, gauge


def test_convert_ok():
    """Correct input"""
    assert convert("0/4") == 0
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("4/4") == 100


def test_convert_zero_division():
    """ZeroDivisionError"""
    with pytest.raises(ZeroDivisionError):
        convert("4/0")


def test_convert_value_error():
    """ValueError"""
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ValueError):
        convert("1.5/3")


def test_convert_over_100():
    """Over 100%"""
    with pytest.raises(ValueError):
        convert("5/4")


def test_gauge_empty():
    """E if percentage <= 1"""
    assert gauge(-1) == "E"
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_percentage():
    """x% if 1 < percentage < 99"""
    assert gauge(2) == "2%"
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"


def test_gauge_full():
    """F if percentage >=99"""
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(101) == "F"
