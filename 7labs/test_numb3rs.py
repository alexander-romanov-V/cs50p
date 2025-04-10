"""Unit-test for numb3rs.py"""

from numb3rs import validate


def test_validate_ok():
    """Test valid IPv4 adresses"""
    assert validate("0.0.0.0") is True
    assert validate("1.1.1.1") is True
    assert validate("255.255.255.255") is True
    assert validate("1.100.200.255") is True
    assert validate("255.200.100.1") is True


def test_validate_nok():
    """Test invalid IPv4 adresses"""
    assert validate("275.3.6.28") is False
    assert validate("300.300.300.300") is False
    assert validate("8.9.10.1000") is False
    assert validate("192.168.100.-1") is False
    assert validate("5.4.A.Z") is False
    assert validate("5.4.6") is False
    assert validate("localhost") is False


def test_validate_cs50p_demo():
    """Test IPv4 adresses as cs50p demo"""
    assert validate("1.2.3.4") is True
    assert validate("127.0.0.1") is True
    assert validate("255.255.255.0") is True
    assert validate("275.3.6.28") is False
    assert validate("cat") is False


def test_validate_cs50p_manual_test():
    """Test IPv4 adresses as cs50p manual test"""
    assert validate("127.0.0.1") is True
    assert validate("255.255.255.255") is True
    assert validate("512.512.512.512") is False
    assert validate("1.2.3.1000") is False
    assert validate("cat") is False
