"""Unit-test of Working 9 to 5"""

import pytest
from working import convert


def test_convert_ok():
    """Test valid time range"""
    assert convert("8:00 AM to 6:00 PM") == "08:00 to 18:00"
    assert convert("9 AM to 7 PM") == "09:00 to 19:00"
    assert convert("8 AM to 6:30 PM") == "08:00 to 18:30"


def test_convert_nok():
    """Test invalid time range"""
    with pytest.raises(ValueError):
        convert("24:00 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("4:60 AM to 1 PM")
    with pytest.raises(ValueError):
        convert("2 AM - 1 PM")
    with pytest.raises(ValueError):
        convert("3:00 AM - 7:00 PM")


def test_convert_cs50p_demo():
    """Test IPv4 adresses as cs50p demo"""
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"


def test_convert_cs50p_manual_test():
    """Test IPv4 adresses as cs50p manual test"""
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
