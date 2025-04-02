"""Unittest for Vanity Plates"""

from plates import is_valid


def test_is_valid_ok():
    """Valid plates"""
    assert is_valid("HI") is True
    assert is_valid("CS50") is True
    assert is_valid("TST123") is True


def test_is_valid_no_2_letters():
    """All vanity plates must start with at least two letters"""
    assert is_valid("01234") is False
    assert is_valid("H999") is False


def test_is_valid_oversize():
    """May contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters."""
    assert is_valid("SEVEN77") is False
    assert is_valid("OUTATIME") is False
    assert is_valid("H124") is False
    assert is_valid("H") is False


def test_is_valid_wrong_digits_order():
    """Numbers cannot be used in the middle of a plate; they must come at the end"""
    assert is_valid("CS50P") is False
    assert is_valid("55POOR") is False


def test_is_valid_zero_first():
    """The first number used cannot be a '0'"""
    assert is_valid("CS05") is False
    assert is_valid("CS0") is False
    assert is_valid("CS00") is False


def test_is_valid_extra_signs():
    """No periods, spaces, or punctuation marks are allowed"""
    assert is_valid("PI3.14") is False
    assert is_valid("HEY!?") is False
    assert is_valid("MY 55") is False
